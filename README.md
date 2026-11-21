# cappuccino.dev

Source repository for the [Cappuccino](https://cappuccino.dev) web site.

## Migrating site to Hugo static site generator

This migration replaces a heavy Docker, Ruby, and Middleman build pipeline—along with legacy Bootstrap theme dependencies—with a fast, deterministic Hugo site built on semantic HTML5, native CSS, and zero client-side JavaScript.

The original Sofa visual identity is retained as far as practical while adding dark mode support. Authoring is standardized on Markdown so contributors can focus on communication rather than markup mechanics.

The site also shifts Cappuccino's positioning away from the now largely solved problem of cross-browser compatibility toward productivity and architectural longevity in the construction of large-scale web applications.

Hosting is entirely static, enabling deployment on GitHub Pages or, preferentially, Cloudflare Pages at zero hosting cost.

## Local Development

Requires [Hugo](https://gohugo.io/) (`hugo.toml` uses `locale` rather than the deprecated `languageCode`).

Preview locally:

```sh
hugo server
```

Build for production:

```sh
hugo --gc --minify
```

## Adding a Blog Post

Create a new Markdown file under `content/blog/` with YAML front matter (`title`, `date`, `author`) and post body content:

```markdown
---
title: "Post Title"
date: 2026-11-21
author: "Author Name"
---

Post body goes here.
```

## Deployment

Target hosting is not finalized. The site is fully static and compatible with GitHub Pages or Cloudflare Pages (free tiers), traditional web servers, or a custom purpose-built Golang/Lisette server appliance accessed from the Cloudflare edge via `cloudflared` tunnels.

## History and Legacy Build

The legacy site was a Middleman and Ruby application built inside a Docker container (`middleman` image, `bundle _1.17.3_ exec middleman build` / `server` on port `4567`), with deployment via `rsync` of `build/` and a Cloudflare cache purge.

Its original visual design was created by Sofa on top of the Bootstrap *Measure* theme (whose upstream source is no longer available). Legacy assets and credits from that era included:

- Bootstrap and the *Measure* Bootstrap theme
- Lato Google webfont (`http://www.google.com/webfonts/specimen/Lato`)
- Icons by Brankic1979 (`http://www.brankic1979.com/icons/`)
- Social icons from Medialoot (`http://medialoot.com/item/round-social-media-icons/`)
- `furley_bg.png` by Dan Kruse
- `1154865_61618748.jpeg` (`http://www.sxc.hu/photo/1154865`)

The vendored `vendor/pygments-main` copy originated from a Mercurial checkout with local Objective-J syntax-highlighting tweaks for the legacy toolchain, and is superseded by Hugo's built-in syntax highlighting.

## Migration Status

Content, data, and static assets under `content/`, `data/`, and `static/` originate from a mechanical conversion pass over the legacy source tree. Legacy front-matter issues (such as duplicate YAML keys), raw HTML fragments, and `.erb` templates are being audited and cleaned up incrementally alongside semantic HTML5 and native CSS layout work.