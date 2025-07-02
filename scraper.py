import requests
import json
import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup

BASE_URL = "https://firstjob.me"
LISTINGS_PATH = "/ofertas"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/115.0.0.0 Safari/537.36"
    )
}

def Firstjob_Scraper(limit=10):
    """
    Scrapea las primeras `limit` ofertas de FirstJob.
    Devuelve lista de dicts: title, company, location, url.
    """
    # 1. Obtener enlaces de las ofertas
    list_url = urljoin(BASE_URL, LISTINGS_PATH)
    resp = requests.get(list_url, headers=HEADERS, timeout=10)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")
    anchors = []
    for a in soup.select("a[href^='/oferta/']"):
        href = a.get('href')
        if not href:
            continue
        if href not in {x.get('href') for x in anchors}:
            anchors.append(a)
        if len(anchors) >= limit:
            break

    results = []
    # 2. Extraer datos desde cada detalle
    for a in anchors:
        detail_url = urljoin(BASE_URL, a['href'])
        title = company = location = ""
        try:
            dresp = requests.get(detail_url, headers=HEADERS, timeout=10)
            dresp.raise_for_status()
            dsoup = BeautifulSoup(dresp.text, "html.parser")

            header = dsoup.select_one("div.job-single-header")
            if header:
                # Título en <h3 class="mb-15">
                title_tag = header.select_one("h3.mb-15")
                title = title_tag.get_text(strip=True) if title_tag else ""

                # Empresa: puede ser <span> o <a> con clase company text-md
                comp_tag = header.select_one("span.company.text-md, a.company.text-md")
                company = comp_tag.get_text(strip=True) if comp_tag else ""

                # Ubicación en <span class="location text-md">
                loc_tag = header.select_one("span.location.text-md")
                location = loc_tag.get_text(strip=True) if loc_tag else ""
        except Exception:
            # En caso de fallo, dejamos campos vacíos
            pass

        results.append({
            "title": title,
            "company": company,
            "location": location,
            "url": detail_url
        })

    return results


def save_to_json(data, filename="Listado_Trabajos.json"):
    """Guarda la lista de ofertas en un archivo JSON."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Guardadas {len(data)} ofertas en '{filename}'")


if __name__ == "__main__":
    jobs = Firstjob_Scraper(limit=10)
    save_to_json(jobs)
