import requests
from bs4 import BeautifulSoup

SERPAPI_KEY = "b090b5d5fc30627493e8da365f820e5ebed80a6cd6a2894ccb16a66841245484"

def get_usd_to_ils():
    try:
        res = requests.get("https://open.er-api.com/v6/latest/USD", timeout=5)
        return res.json()["rates"]["ILS"]
    except:
        return 3.7

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
                results.append({
                    "store": item.get("source", "Unknown"),
                    "title": item.get("title", product),
                    "price_usd": price,
                    "currency": "USD",
                    "link": item.get("link", "")
                })
        return results
    except Exception as e:
        return []

def parse_price_usd(price_str):
    try:
        cleaned = price_str.replace("$", "").replace(",", "").strip()
        cleaned = cleaned.split(" ")[0]
        return float(cleaned)
    except:
        return None

def search_zap(product):
    try:
        url = f"https://www.zap.co.il/search.aspx?keyword={requests.utils.quote(product)}"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        res = requests.get(url, headers=headers, timeout=8)
        soup = BeautifulSoup(res.text, "html.parser")
        price_el = soup.find("span", class_="price")
        if price_el:
            price_text = price_el.get_text(strip=True).replace("₪", "").replace(",", "").strip()
            return float(price_text)
        return None
    except:
        return None

def search_ksp(product):
    try:
        url = f"https://ksp.co.il/web/cat/search?q={requests.utils.quote(product)}"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        res = requests.get(url, headers=headers, timeout=8)
        soup = BeautifulSoup(res.text, "html.parser")
        price_el = soup.find("span", class_="price")
        if price_el:
            price_text = price_el.get_text(strip=True).replace("₪", "").replace(",", "").strip()
            return float(price_text)
        return None
    except:
        return None

def search_bug(product):
    try:
        url = f"https://www.bug.co.il/search/?q={requests.utils.quote(product)}"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        res = requests.get(url, headers=headers, timeout=8)
        soup = BeautifulSoup(res.text, "html.parser")
        price_el = soup.find("span", class_="price")
        if price_el:
            price_text = price_el.get_text(strip=True).replace("₪", "").replace(",", "").strip()
            return float(price_text)
        return None
    except:
        return None

def sadeh_search(product):
    rate = get_usd_to_ils()
    results = []

    # חיפוש בינלאומי דרך Google Shopping
    intl_results = search_google_shopping(product)
    for item in intl_results:
        price_usd = item["price_usd"]
        shipping_usd = 15  # משלוח ממוצע
        total_usd = price_usd + shipping_usd
        base_ils = total_usd * rate
        tax = base_ils * 0.17 if price_usd > 75 else 0
        final_ils = base_ils + tax
        results.append({
            "store": item["store"],
            "region": "International",
            "flag": "🌍",
            "price_display": f"${price_usd:,.0f}",
            "price_ils": round(final_ils),
            "note": "incl. shipping & tax",
            "link": item.get("link", "")
        })

    # חיפוש בארץ
    zap_price = search_zap(product)
    if zap_price:
        results.append({
            "store": "ZAP",
            "region": "Israel",
            "flag": "🇮🇱",
            "price_display": f"₪{zap_price:,.0f}",
            "price_ils": round(zap_price),
            "note": "local price",
            "link": f"https://www.zap.co.il/search.aspx?keyword={requests.utils.quote(product)}"
        })

    ksp_price = search_ksp(product)
    if ksp_price:
        results.append({
            "store": "KSP",
            "region": "Israel",
            "flag": "🇮🇱",
            "price_display": f"₪{ksp_price:,.0f}",
            "price_ils": round(ksp_price),
            "note": "local price",
            "link": f"https://ksp.co.il/web/cat/search?q={requests.utils.quote(product)}"
        })

    bug_price = search_bug(product)
    if bug_price:
        results.append({
            "store": "BUG",
            "region": "Israel",
            "flag": "🇮🇱",
            "price_display": f"₪{bug_price:,.0f}",
            "price_ils": round(bug_price),
            "note": "local price",
            "link": f"https://www.bug.co.il/search/?q={requests.utils.quote(product)}"
        })

    if not results:
        return {"error": "No results found. Try a different product name."}

    # מיין לפי מחיר
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
