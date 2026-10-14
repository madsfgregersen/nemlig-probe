import urllib.request, ssl

ctx = ssl.create_default_context()
targets = [
    "https://www.nemlig.com/",
    "https://www.nemlig.com/webapi/basket/GetBasket",
    "https://webapi.prod.knl.nemlig.it/searchgateway/api/quick?query=maelk",
]
for url in targets:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        r = urllib.request.urlopen(req, timeout=20, context=ctx)
        body = r.read(400).decode("utf-8", "replace")
        print(f"\n=== {url}\nHTTP {r.status}")
        print("first 400 chars:", body.replace("\n", " ")[:400])
    except urllib.error.HTTPError as e:
        print(f"\n=== {url}\nHTTP {e.code} (HTTPError)")
        print("first 400 chars:", e.read(400).decode('utf-8','replace').replace('\n',' ')[:400])
    except Exception as e:
        print(f"\n=== {url}\nFAILED: {type(e).__name__}: {e}")

print("\n--- probe done ---")