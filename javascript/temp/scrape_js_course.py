# /// script
# dependencies = [
#   "requests",
#   "beautifulsoup4",
#   "markdownify",
#   "rich",
# ]
# ///

import os
import re
import time
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from rich import print
from rich.progress import track

BASE_URL = "https://www.luisllamas.es"
COURSE_PREFIX = f"{BASE_URL}/curso-javascript/"
SITEMAP_URL = f"{BASE_URL}/sitemap.xml"
OUTPUT_DIR = "js_course_md"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; CursoJS-Scraper/3.0)"
}


# ---------------------------------------------------
# Utils
# ---------------------------------------------------

def fetch(url: str) -> requests.Response:
    r = requests.get(url, headers=HEADERS, timeout=20)
    r.raise_for_status()
    return r


def clean_filename(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text.lower().strip("-")


# ---------------------------------------------------
# 1️⃣ Extraer URLs del sitemap
# ---------------------------------------------------

def extract_course_urls():
    print("[bold cyan]Descargando sitemap...[/bold cyan]")
    xml = fetch(SITEMAP_URL).text
    soup = BeautifulSoup(xml, "xml")

    urls = []
    for loc in soup.find_all("loc"):
        url = loc.text.strip()

        if not url.startswith(COURSE_PREFIX):
            continue

        # excluir la página índice
        if url.rstrip("/") == COURSE_PREFIX.rstrip("/"):
            continue

        urls.append(url)

    return sorted(set(urls))


# ---------------------------------------------------
# 2️⃣ Scraping
# ---------------------------------------------------

def scrape_section(url: str):
    soup = BeautifulSoup(fetch(url).text, "html.parser")

    title_tag = soup.find("h1")
    title = title_tag.get_text(strip=True) if title_tag else url.split("/")[-1]

    content = soup.select_one("div.entry-content")
    if not content:
        print(f"[red]No se encontró contenido en {url}[/red]")
        return None

    for tag in content(["script", "style", "noscript"]):
        tag.decompose()

    markdown = md(str(content), heading_style="ATX")

    filename = clean_filename(title) + ".md"
    filepath = os.path.join(OUTPUT_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        f.write(markdown)

    return filename, title


# ---------------------------------------------------
# MAIN
# ---------------------------------------------------

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    urls = extract_course_urls()

    print(f"[green]🔗 Found {len(urls)} articles to scrape.[/green]")

    if not urls:
        print("[red]No se encontraron URLs en el sitemap.[/red]")
        return

    index_md = ["# Curso JavaScript - Índice\n"]

    for url in track(urls, description="Scrapeando..."):
        try:
            result = scrape_section(url)
            if result:
                filename, title = result
                index_md.append(f"- [{title}]({filename})")
            time.sleep(0.6)
        except Exception as e:
            print(f"[red]Error en {url}: {e}[/red]")

    with open(os.path.join(OUTPUT_DIR, "00_indice.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(index_md))

    print("\n[bold green]✔ Curso descargado correctamente[/bold green]")
    print(f"[yellow]Archivos guardados en: {OUTPUT_DIR}/[/yellow]")


if __name__ == "__main__":
    main()
