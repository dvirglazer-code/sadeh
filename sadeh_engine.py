import requests
from bs4 import BeautifulSoup

SERPAPI_KEY = "b090b5d5fc30627493e8da365f820e5ebed80a6cd6a2894ccb16a66841245484"

def translate_to_english(text):
    try:
        url = "https://translate.googleapis.com/translate_a/single"
        params = {"client": "gtx", "sl": "auto", "tl": "en", "dt": "t", "q": text}
        res = requests.get(url, params=params, timeout=5)
        translated = res.json()[0][0][0]
        return translated
    except:
        return text


def translate_to_english(text):
    try:
        url = "https://translate.googleapis.com/translate_a/single"
        params = {"client": "gtx", "sl": "auto", "tl": "en", "dt": "t", "q": text}
        res = requests.get(url, params=params, timeout=5)
        translated = res.json()[0][0][0]
        return translated
    except:
        return text

import requests
from bs4 import BeautifulSoup

SERPAPI_KEY = "b090b5d5fc30627493e8da365f820e5ebed80a6cd6a2894ccb16a66841245484"

COUNTRY_MAP = {
    "IL": {"name": "Israel",        "shipping": 15, "tax_threshold": 75,  "customs": 0.12, "vat": 0.17},
    "US": {"name": "United States", "shipping": 0,  "tax_threshold": 800, "customs": 0.0,  "vat": 0.0},
    "GB": {"name": "United Kingdom","shipping": 12, "tax_threshold": 135, "customs": 0.04, "vat": 0.20},
    "DE": {"name": "Germany",       "shipping": 12, "tax_threshold": 150, "customs": 0.035,"vat": 0.19},
    "FR": {"name": "France",        "shipping": 12, "tax_threshold": 150, "customs": 0.035,"vat": 0.20},
    "IT": {"name": "Italy",         "shipping": 12, "tax_threshold": 150, "customs": 0.035,"vat": 0.22},
    "ES": {"name": "Spain",         "shipping": 12, "tax_threshold": 150, "customs": 0.035,"vat": 0.21},
    "NL": {"name": "Netherlands",   "shipping": 12, "tax_threshold": 150, "customs": 0.035,"vat": 0.21},
    "SE": {"name": "Sweden",        "shipping": 14, "tax_threshold": 0,   "customs": 0.035,"vat": 0.25},
    "NO": {"name": "Norway",        "shipping": 14, "tax_threshold": 0,   "customs": 0.0,  "vat": 0.25},
    "DK": {"name": "Denmark",       "shipping": 14, "tax_threshold": 0,   "customs": 0.035,"vat": 0.25},
    "FI": {"name": "Finland",       "shipping": 14, "tax_threshold": 150, "customs": 0.035,"vat": 0.24},
    "CH": {"name": "Switzerland",   "shipping": 14, "tax_threshold": 62,  "customs": 0.025,"vat": 0.077},
    "AT": {"name": "Austria",       "shipping": 12, "tax_threshold": 150, "customs": 0.035,"vat": 0.20},
    "BE": {"name": "Belgium",       "shipping": 12, "tax_threshold": 150, "customs": 0.035,"vat": 0.21},
    "PL": {"name": "Poland",        "shipping": 12, "tax_threshold": 150, "customs": 0.035,"vat": 0.23},
    "PT": {"name": "Portugal",      "shipping": 12, "tax_threshold": 150, "customs": 0.035,"vat": 0.23},
    "CZ": {"name": "Czech Republic","shipping": 12, "tax_threshold": 150, "customs": 0.035,"vat": 0.21},
    "HU": {"name": "Hungary",       "shipping": 12, "tax_threshold": 150, "customs": 0.035,"vat": 0.27},
    "RO": {"name": "Romania",       "shipping": 12, "tax_threshold": 150, "customs": 0.035,"vat": 0.19},
    "GR": {"name": "Greece",        "shipping": 12, "tax_threshold": 150, "customs": 0.035,"vat": 0.24},
    "CA": {"name": "Canada",        "shipping": 10, "tax_threshold": 20,  "customs": 0.05, "vat": 0.05},
    "MX": {"name": "Mexico",        "shipping": 15, "tax_threshold": 50,  "customs": 0.15, "vat": 0.16},
    "BR": {"name": "Brazil",        "shipping": 20, "tax_threshold": 50,  "customs": 0.60, "vat": 0.0},
    "AR": {"name": "Argentina",     "shipping": 20, "tax_threshold": 200, "customs": 0.50, "vat": 0.21},
    "CL": {"name": "Chile",         "shipping": 18, "tax_threshold": 30,  "customs": 0.06, "vat": 0.19},
    "CO": {"name": "Colombia",      "shipping": 18, "tax_threshold": 200, "customs": 0.15, "vat": 0.19},
    "JP": {"name": "Japan",         "shipping": 12, "tax_threshold": 10000,"customs": 0.0, "vat": 0.10},
    "CN": {"name": "China",         "shipping": 5,  "tax_threshold": 50,  "customs": 0.10, "vat": 0.13},
    "KR": {"name": "South Korea",   "shipping": 12, "tax_threshold": 150, "customs": 0.08, "vat": 0.10},
    "IN": {"name": "India",         "shipping": 15, "tax_threshold": 40,  "customs": 0.20, "vat": 0.18},
    "SG": {"name": "Singapore",     "shipping": 10, "tax_threshold": 400, "customs": 0.0,  "vat": 0.09},
    "HK": {"name": "Hong Kong",     "shipping": 8,  "tax_threshold": 9999,"customs": 0.0,  "vat": 0.0},
    "TW": {"name": "Taiwan",        "shipping": 10, "tax_threshold": 2000,"customs": 0.05, "vat": 0.05},
    "TH": {"name": "Thailand",      "shipping": 12, "tax_threshold": 40,  "customs": 0.20, "vat": 0.07},
    "MY": {"name": "Malaysia",      "shipping": 12, "tax_threshold": 500, "customs": 0.05, "vat": 0.06},
    "ID": {"name": "Indonesia",     "shipping": 15, "tax_threshold": 75,  "customs": 0.075,"vat": 0.11},
    "PH": {"name": "Philippines",   "shipping": 15, "tax_threshold": 10,  "customs": 0.15, "vat": 0.12},
    "VN": {"name": "Vietnam",       "shipping": 12, "tax_threshold": 1000000,"customs": 0.20,"vat": 0.10},
    "AU": {"name": "Australia",     "shipping": 15, "tax_threshold": 1000,"customs": 0.05, "vat": 0.10},
    "NZ": {"name": "New Zealand",   "shipping": 18, "tax_threshold": 1000,"customs": 0.05, "vat": 0.15},
    "AE": {"name": "UAE",           "shipping": 15, "tax_threshold": 300, "customs": 0.05, "vat": 0.05},
    "SA": {"name": "Saudi Arabia",  "shipping": 15, "tax_threshold": 266, "customs": 0.05, "vat": 0.15},
    "TR": {"name": "Turkey",        "shipping": 15, "tax_threshold": 150, "customs": 0.20, "vat": 0.18},
}

def get_usd_to_ils():
    try:
        res = requests.get("https://open.er-api.com/v6/latest/USD", timeout=5)
        return res.json()["rates"]["ILS"]
    except:
        return 3.7

def calculate_total_usd(price_usd, country_info):
    shipping = country_info["shipping"]
    threshold = country_info["tax_threshold"]
    customs_rate = country_info["customs"]
    vat_rate = country_info["vat"]
    total = price_usd + shipping
    if price_usd > threshold:
        customs = price_usd * customs_rate
        vat = (price_usd + customs) * vat_rate
        total += customs + vat
    return round(total, 2)

def build_store_link(store_name, product):
    q = requests.utils.quote(product)
    store = store_name.lower()
    if "amazon" in store:
        return f"https://www.amazon.com/s?k={q}"
    if "ebay" in store:
        return f"https://www.ebay.com/sch/i.html?_nkw={q}"
    if "walmart" in store:
        return f"https://www.walmart.com/search?q={q}"
    if "best buy" in store:
        return f"https://www.bestbuy.com/site/searchpage.jsp?st={q}"
    if "target" in store:
        return f"https://www.target.com/s?searchTerm={q}"
    if "newegg" in store:
        return f"https://www.newegg.com/p/pl?d={q}"
    if "costco" in store:
        return f"https://www.costco.com/CatalogSearch?keyword={q}"
    if "aliexpress" in store:
        return f"https://www.aliexpress.com/wholesale?SearchText={q}"
    if "cricket" in store:
        return f"https://www.google.com/search?tbm=shop&q={q}+cricket+wireless"
    if "gazelle" in store:
        return f"https://www.google.com/search?tbm=shop&q={q}+gazelle"
    if "back market" in store:
        return f"https://www.backmarket.com/en-us/search?q={q}"
    if "swappa" in store:
        return f"https://www.google.com/search?tbm=shop&q={q}+swappa"
    # fallback: Google Shopping for that store
    return f"https://www.google.com/search?tbm=shop&q={q}+{requests.utils.quote(store_name)}"

def search_google_shopping(product):
    try:
        url = "https://serpapi.com/search"
        params = {
            "engine": "google_shopping",
            "q": product,
            "api_key": SERPAPI_KEY,
            "gl": "us",
            "hl": "en",
            "num": 10
        }
        res = requests.get(url, params=params, timeout=10)
        data = res.json()
        results = []
        for item in data.get("shopping_results", [])[:6]:
            price_str = item.get("price", "")
            price = parse_price_usd(price_str)
            if price:
                store_name = item.get("source", "")
                link = build_store_link(store_name, product)
                results.append({
                    "store": store_name or "Unknown",
                    "title": item.get("title", product),
                    "price_usd": price,
                    "rating": item.get("rating", None),
                    "link": link
                })
        return results
    except:
        return []

def parse_price_usd(price_str):
    try:
        cleaned = price_str.replace("$", "").replace(",", "").replace("£","").replace("€","").strip()
        cleaned = cleaned.split(" ")[0]
        return float(cleaned)
    except:
        return None

def search_zap(product):
    try:
        url = f"https://www.zap.co.il/search.aspx?keyword={requests.utils.quote(product)}"
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers, timeout=8)
        soup = BeautifulSoup(res.text, "html.parser")
        price_el = soup.find("span", class_="price")
        if price_el:
            return float(price_el.get_text(strip=True).replace("₪","").replace(",","").strip())
        return None
    except:
        return None

def search_ksp(product):
    try:
        url = f"https://ksp.co.il/web/cat/search?q={requests.utils.quote(product)}"
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers, timeout=8)
        soup = BeautifulSoup(res.text, "html.parser")
        price_el = soup.find("span", class_="price")
        if price_el:
            return float(price_el.get_text(strip=True).replace("₪","").replace(",","").strip())
        return None
    except:
        return None

def search_bug(product):
    try:
        url = f"https://www.bug.co.il/search/?q={requests.utils.quote(product)}"
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers, timeout=8)
        soup = BeautifulSoup(res.text, "html.parser")
        price_el = soup.find("span", class_="price")
        if price_el:
            return float(price_el.get_text(strip=True).replace("₪","").replace(",","").strip())
        return None
    except:
        return None

def sadeh_search(product, country_code="IL"):
    product = translate_to_english(product)
    rate = get_usd_to_ils()
    results = []
    country_info = COUNTRY_MAP.get(country_code, COUNTRY_MAP["IL"])

    # Always search with gl=us for best results
    intl_results = search_google_shopping(product)
    for item in intl_results:
        price_usd = item["price_usd"]
        total_usd = calculate_total_usd(price_usd, country_info)
        total_ils = round(total_usd * rate)
        results.append({
            "store": item["store"],
            "region": country_info["name"],
            "flag": "🌍",
            "price_display": f"${total_usd:,.0f}",
            "price_ils": total_ils,
            "note": "incl. shipping + tax",
            "rating": item.get("rating"),
            "link": item.get("link", "")
        })

    # Israeli stores only for IL
    if country_code == "IL":
        zap_price = search_zap(product)
        if zap_price:
            results.append({
                "store": "ZAP", "region": "Israel", "flag": "🇮🇱",
                "price_display": f"₪{zap_price:,.0f}",
                "price_ils": round(zap_price), "note": "local price", "rating": None,
                "link": f"https://www.zap.co.il/search.aspx?keyword={requests.utils.quote(product)}"
            })
        ksp_price = search_ksp(product)
        if ksp_price:
            results.append({
                "store": "KSP", "region": "Israel", "flag": "🇮🇱",
                "price_display": f"₪{ksp_price:,.0f}",
                "price_ils": round(ksp_price), "note": "local price", "rating": None,
                "link": f"https://ksp.co.il/web/cat/search?q={requests.utils.quote(product)}"
            })
        bug_price = search_bug(product)
        if bug_price:
            results.append({
                "store": "BUG", "region": "Israel", "flag": "🇮🇱",
                "price_display": f"₪{bug_price:,.0f}",
                "price_ils": round(bug_price), "note": "local price", "rating": None,
                "link": f"https://www.bug.co.il/search/?q={requests.utils.quote(product)}"
            })

    if not results:
        return {"error": "No results found. Try a different product name."}

    results.sort(key=lambda x: x["price_ils"])
    best = results[0]

    return {
        "product": product,
        "exchange_rate": round(rate, 2),
        "results": results,
        "best_store": best["store"],
        "best_price_ils": best["price_ils"],
        "best_flag": best["flag"],
        "verdict": f"Best price at {best['store']} — {best['price_display']} ({best['flag']} {best['region']})"
    }
