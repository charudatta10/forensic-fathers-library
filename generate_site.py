import json, os

with open("data/people.json") as f:
    people = json.load(f)

os.makedirs("people", exist_ok=True)

index_links = []

for p in people:
    d = f"people/{p['slug']}"
    os.makedirs(d, exist_ok=True)

    links_html = "".join([f'<li><a href="{l}">{l}</a></li>' for l in p["links"]])

    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>{p['name']}</title>
<link rel="stylesheet" href="../../assets/css/style.css">
</head>
<body>
<div class="card">
<h1>{p['name']}</h1>
<h2>{p['title']}</h2>
<p>{p['bio']}</p>
<blockquote>{p['quote']}</blockquote>
<ul>{links_html}</ul>
<a href="../../index.html">← Back</a>
</div>
</body>
</html>"""

    with open(f"{d}/index.html","w",encoding="utf-8") as f:
        f.write(html)

    index_links.append(f'<li><a href="people/{p["slug"]}/">{p["name"]}</a></li>')

with open("index.html","w",encoding="utf-8") as f:
    f.write(f"""<!DOCTYPE html>
<html><head>
<meta charset="utf-8">
<title>Forensic Science Fathers</title>
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
<div class="container">
<h1>Fathers of Forensic Science</h1>
<ul>{"".join(index_links)}</ul>
</div>
</body></html>""")
