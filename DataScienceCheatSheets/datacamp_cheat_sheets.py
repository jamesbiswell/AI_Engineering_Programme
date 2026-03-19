"""
Download DataCamp cheat sheet PDFs from listing pages 1 through 7.

What it does:
- Scrapes:
    https://www.datacamp.com/cheat-sheet
    https://www.datacamp.com/cheat-sheet/page/2
    ...
    https://www.datacamp.com/cheat-sheet/page/7
- Collects individual cheat sheet article URLs
- Visits each cheat sheet page
- Finds the PDF link
- Downloads the PDFs into ./datacamp_cheat_sheets

Requirements:
    pip install playwright
    playwright install chromium

Usage:
    python datacamp_cheat_sheets.py
"""

from pathlib import Path
from urllib.parse import urljoin, urlparse
import re

from playwright.sync_api import sync_playwright


BASE = "https://www.datacamp.com"
HUB = f"{BASE}/cheat-sheet"
OUTDIR = Path("datacamp_cheat_sheets")


def listing_url(page_num: int) -> str:
    return HUB if page_num == 1 else f"{HUB}/page/{page_num}"


def safe_filename(name: str) -> str:
    forbidden = '<>:"/\\|?*'
    name = "".join("" if ch in forbidden else ch for ch in name)
    name = "".join(ch for ch in name if ord(ch) >= 32)
    name = name.replace("&", "and")
    name = re.sub(r"\s+", " ", name).strip()
    name = name.rstrip(".")
    return name or "datacamp_cheat_sheet"


def is_article_url(url: str) -> bool:
    parsed = urlparse(url)
    if parsed.netloc not in {"www.datacamp.com", "datacamp.com"}:
        return False

    path = parsed.path.rstrip("/")

    if path == "/cheat-sheet":
        return False

    if re.fullmatch(r"/cheat-sheet/page/\\d+", path):
        return False

    return re.fullmatch(r"/cheat-sheet/[^/]+", path) is not None


def collect_article_links(page) -> list[str]:
    urls = set()

    anchors = page.locator("a[href]")
    count = anchors.count()

    for i in range(count):
        try:
            href = anchors.nth(i).get_attribute("href")
            if not href:
                continue
            full = urljoin(BASE, href)
            if is_article_url(full):
                urls.add(full)
        except Exception:
            pass

    return sorted(urls)


def first_matching_href(page, selectors: list[str]) -> str | None:
    for selector in selectors:
        loc = page.locator(selector)
        if loc.count() > 0:
            try:
                href = loc.first.get_attribute("href")
                if href:
                    return urljoin(page.url, href)
            except Exception:
                pass
    return None


def main():
    OUTDIR.mkdir(exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            slow_mo=150,
        )
        context = browser.new_context(accept_downloads=True)
        page = context.new_page()

        all_articles = set()

        print("Collecting article links from pages 1 to 7...")

        for page_num in range(1, 8):
            url = listing_url(page_num)
            print(f"Opening listing page {page_num}: {url}")
            page.goto(url, wait_until="domcontentloaded", timeout=90000)

            # Give client-side rendering a moment if needed
            page.wait_for_timeout(2500)

            articles = collect_article_links(page)
            print(f"  Found {len(articles)} candidate article links")
            all_articles.update(articles)

        all_articles = sorted(all_articles)
        print(f"\\nTotal unique article pages found: {len(all_articles)}\\n")

        downloaded = 0
        skipped = 0
        failed = 0

        for idx, article_url in enumerate(all_articles, start=1):
            print(f"[{idx}/{len(all_articles)}] Opening article: {article_url}")

            try:
                page.goto(article_url, wait_until="domcontentloaded", timeout=90000)
                page.wait_for_timeout(2000)

                title = page.locator("h1").first.text_content() if page.locator("h1").count() else article_url.rsplit("/", 1)[-1]
                title = safe_filename(title)

                # Try likely download selectors first
                pdf_url = first_matching_href(page, [
                    'a:has-text("Download PDF")',
                    'a:has-text("Download pdf")',
                    'a:has-text("PDF")',
                    'a[href$=".pdf"]',
                    'a[href*="media.datacamp.com"]',
                    'a[href*="assets.datacamp.com"]',
                    'a[href*="images.datacamp.com"]',
                ])

                if not pdf_url:
                    print("  No PDF link found; skipping")
                    skipped += 1
                    continue

                print(f"  PDF link: {pdf_url}")

                # Download via browser
                with page.expect_download(timeout=90000) as download_info:
                    page.evaluate(
                        """
                        (url) => {
                            const a = document.createElement('a');
                            a.href = url;
                            a.target = '_self';
                            document.body.appendChild(a);
                            a.click();
                            a.remove();
                        }
                        """,
                        pdf_url,
                    )

                download = download_info.value
                target = OUTDIR / f"{title}.pdf"
                download.save_as(str(target))

                print(f"  Saved: {target}")
                downloaded += 1

            except Exception as exc:
                print(f"  ERROR: {exc}")
                failed += 1

        print("\\nDone.")
        print(f"Downloaded: {downloaded}")
        print(f"Skipped:    {skipped}")
        print(f"Failed:     {failed}")
        print(f"Folder:     {OUTDIR.resolve()}")

        browser.close()


if __name__ == "__main__":
    main()