import path from "path"
import { FilePath } from "./path"
import { globby } from "globby"

export function toPosixPath(fp: string): string {
  return fp.split(path.sep).join("/")
}

export async function glob(
  pattern: string,
  cwd: string,
  ignorePatterns: string[],
): Promise<FilePath[]> {
  const fps = (
    await globby(pattern, {
      cwd,
      ignore: ignorePatterns,
      // fg-zettelkasten: vendored edit. The site content lives in
      // quartz/content/, which is .gitignored (it is regenerated from vault/
      // by `python -m src.main export-site`). With gitignore:true Quartz would
      // skip the whole content tree. `ignorePatterns` from quartz.config.ts
      // still filters independently. Re-apply this on Quartz upgrades.
      gitignore: false,
    })
  ).map(toPosixPath)
  return fps as FilePath[]
}
