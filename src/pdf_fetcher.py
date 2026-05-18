"""Download a PDF from a public URL and extract its text.

Used for the author's own publications: their green open-access PDF lives at a
public URL (resolved from ORA by fabiogiglietto.github.io's own-publications
feed) rather than in the Paperpile Drive folder that `drive_client` reads.
"""
from __future__ import annotations

import io
import time
from typing import Optional

import requests
from pypdf import PdfReader

_USER_AGENT = "Mozilla/5.0 (compatible; fg-zettelkasten/1.0)"
_MAX_PDF_BYTES = 50 * 1024 * 1024  # 50 MB safety bound
_RETRIES = 3  # repository hosts (e.g. ORA) intermittently reset connections


def _download(url: str) -> Optional[bytes]:
    """GET `url` with a few retries on transient network errors."""
    for attempt in range(_RETRIES):
        try:
            resp = requests.get(
                url, headers={"User-Agent": _USER_AGENT}, timeout=60
            )
            resp.raise_for_status()
            return resp.content
        except requests.RequestException as exc:  # noqa: BLE001 - logged, non-fatal
            if attempt < _RETRIES - 1:
                time.sleep(2 * (attempt + 1))
                continue
            print(f"  pdf: download failed for {url} ({exc})")
    return None


def pdf_text_from_url(url: str, max_chars: int = 80000) -> Optional[str]:
    """Download the PDF at `url` and return its extracted text, or None.

    Never raises: a failed download or unreadable PDF returns None so the
    caller can skip the paper rather than fail the run.
    """
    content = _download(url)
    if content is None:
        return None
    if len(content) > _MAX_PDF_BYTES or content[:4] != b"%PDF":
        print(f"  pdf: {url} is not a usable PDF")
        return None

    try:
        reader = PdfReader(io.BytesIO(content))
        parts = [page.extract_text() for page in reader.pages]
    except Exception as exc:  # noqa: BLE001 - malformed PDF, never fatal
        print(f"  pdf: could not extract text from {url} ({exc})")
        return None

    text = " ".join(" ".join(p.split()) for p in parts if p)
    if not text:
        return None
    return text[:max_chars]
