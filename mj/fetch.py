#!/usr/bin/env python3
"""Fetch Midjourney docs and save as JSON."""
import urllib.request, json, time, os

ARTICLES = [
    # Getting Started
    ("Getting Started", 33329261836941),
    # Prompting Basics
    ("Prompting Basics", 32023408776205),
    ("Prompting Basics", 33329329805581),
    ("Prompting Basics", 31894244298125),
    ("Prompting Basics", 33329374594957),
    ("Prompting Basics", 32835253061645),
    # Using Your Own Images
    ("Using Your Own Images", 37460773864589),
    ("Using Your Own Images", 32040250122381),
    ("Using Your Own Images", 32180011136653),
    ("Using Your Own Images", 36285124473997),
    ("Using Your Own Images", 32162917505293),
    ("Using Your Own Images", 32497889043981),
    ("Using Your Own Images", 32764383466893),
    # Using the Website
    ("Using the Website", 33329460426765),
    ("Using the Website", 33390732264589),
    ("Using the Website", 33329462451469),
    ("Using the Website", 34580542725645),
    ("Using the Website", 35577175650957),
    ("Using the Website", 32433330574221),
    ("Using the Website", 39193335040013),
    ("Using the Website", 41308374558221),
    ("Using the Website", 41117938447629),
    # Midjourney Controls
    ("Midjourney Controls", 32859204029709),
    ("Midjourney Controls", 32099348346765),
    ("Midjourney Controls", 33329788681101),
    ("Midjourney Controls", 32658968492557),
    ("Midjourney Controls", 32173351982093),
    ("Midjourney Controls", 32570788043405),
    ("Midjourney Controls", 32761322355597),
    ("Midjourney Controls", 32176522101773),
    ("Midjourney Controls", 32634113811853),
    ("Midjourney Controls", 32799074515213),
]

BASE = "https://docs.midjourney.com/api/v2/help_center/en-us/articles/{}.json"
sections = {}

for section_name, article_id in ARTICLES:
    url = BASE.format(article_id)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.loads(r.read())["article"]
    entry = {
        "id": data["id"],
        "title": data["title"],
        "url": data["html_url"],
        "updated_at": data["updated_at"],
        "body": data["body"],
    }
    sections.setdefault(section_name, []).append(entry)
    print(f"  ✓ {data['title']}")
    time.sleep(0.15)

result = {"sections": [{"name": k, "articles": v} for k, v in sections.items()]}
out = os.path.join(os.path.dirname(__file__), "midjourney-docs.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

size = os.path.getsize(out)
total = sum(len(s["articles"]) for s in result["sections"])
print(f"\nSaved {total} articles → {out}")
print(f"File size: {size:,} bytes ({size // 1024} KB)")
