import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Quartz 4 Configuration
 *
 * See https://quartz.jzhao.xyz/configuration for more information.
 */
const config: QuartzConfig = {
  configuration: {
    pageTitle: "fg-zettelkasten",
    pageTitleSuffix: "",
    enableSPA: true,
    enablePopovers: true,
    analytics: null,
    locale: "en-US",
    baseUrl: "fabiogiglietto.github.io/fg-zettelkasten",
    ignorePatterns: ["private", "templates", ".obsidian"],
    defaultDateType: "modified",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      // FG brand identity — Saira (DIN-style grotesque) for display/text/UI,
      // IBM Plex Mono for the "machine voice" (code, metadata). See the brand
      // sheet at static/brand.html for the full token set.
      typography: {
        header: { name: "Saira", weights: [300, 400, 500, 600, 700] },
        body: { name: "Saira", weights: [300, 400, 500, 600] },
        code: { name: "IBM Plex Mono", weights: [400, 500, 600] },
      },
      colors: {
        // Light = the cream identity. ink (#232A5C) on cream (#F1EBDE),
        // gold (#A9772B) as the signal/accent.
        lightMode: {
          light: "#f1ebde", // page background — cream
          lightgray: "#c9c0ad", // borders / hr — rule (strong)
          gray: "#6d6a5e", // muted / mono voice
          darkgray: "#43455e", // body text
          dark: "#232a5c", // headings / strong — ink
          secondary: "#232a5c", // links — ink
          tertiary: "#a9772b", // link hover / visited — accent gold
          highlight: "rgba(169, 119, 43, 0.12)", // internal-link / search bg — accent wash
          textHighlight: "#a9772b44", // ==mark== — accent wash
        },
        // Dark = the brand's "reversed on ink" treatment: ink-deep ground,
        // cream text, accent gold preserved as the signal.
        darkMode: {
          light: "#16182b", // page background — ink deep
          lightgray: "#3a3c52", // borders / hr
          gray: "#9a9383", // muted
          darkgray: "#d8d2c4", // body text — warm cream-grey
          dark: "#f1ebde", // headings / strong — cream
          secondary: "#c3b9f0", // links — light blue-violet
          tertiary: "#caa25e", // link hover / visited — brightened gold
          highlight: "rgba(202, 162, 94, 0.15)",
          textHighlight: "#caa25e44",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "git", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      // parseTags off: the vault carries no frontmatter tags, and inline
      // `#…` in this corpus is a hashtag under study (#StayWoke,
      // #IStandWithPutin), not a tag — Quartz was turning each into a tag
      // link inside the title and minting a /tags/ page for it.
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false, parseTags: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
      // Comment out CustomOgImages to speed up build time
      Plugin.CustomOgImages(),
    ],
  },
}

export default config
