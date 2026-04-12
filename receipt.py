receipts = [
    {
        "restaurant": "McDonald's",
        "date": "2024-06-20",
        "items": [
            {"name": "Hamburger", "price": 25000},
            {"name": "French Fries", "price": 15000},
            {"name": "Coca Cola", "price": 10000},
        ],
        "total": 50000
    },
    {
        "restaurant": "KFC",
        "date": "2024-06-19",  # yesterday
        "items": [
            {"name": "Ayam Goreng", "price": 35000},
            {"name": "Nasi", "price": 10000},
        ],
        "total": 45000
    },
    {
        "restaurant": "Burger King",
        "date": "2024-06-15",  # last 7 days
        "items": [
            {"name": "Hamburger Whopper", "price": 45000},
            {"name": "Onion Rings", "price": 20000},
        ],
        "total": 65000
    },
    {
        "restaurant": "Alfamart",
        "date": "2024-02-20",  # last 7 days
        "items": [
            {"name": "Biskuat", "price": 5000},
            {"name": "Pepsodent", "price": 20000},
            {"name": "Aqua", "price": 5000},
            {"name": "Minyak Bimoli", "price": 43000},
            {"name": "Permen Mentos", "price": 7000},
        ],
        "total": 80000
    },
    {
        "restaurant": "Warung Bu Made",
        "date": "2024-01-1",  # last 7 days
        "items": [
            {"name": "Sosis Kenzler", "price": 100000},
            {"name": "Saus BBQ", "price": 20000},
        ],
        "total": 120000
    },
    {
        "restaurant": "Mie Gacoan",
        "date": "2024-06-20",  # last 7 days
        "items": [
            {"name": "Gacoan Level 1", "price": 15000},
            {"name": "Udang Keju", "price": 10000},
            {"name": "Siomay", "price": 10000},
            {"name": "Pangsit", "price": 10000},
            {"name": "Bola Rambutan", "price": 10000},
            {"name": "Gacoan Level 10", "price": 15000},
        ],
        "total": 70000
    },
    {
        "restaurant": "Mie Yamin",
        "date": "2024-06-20",  # last 7 days
        "items": [
            {"name": "Pangsit Goreng", "price": 10000},
            {"name": "Bola Rambutan Krispi", "price": 10000},
            {"name": "Yamin Pedes", "price": 15000},
        ],
        "total": 35000
    },
    {
        "restaurant": "Warteg Saribunda",
        "date": "2024-04-10",  # last 7 days
        "items": [
            {"name": "Es Teh Goceng", "price": 3000},
            {"name": "Gorengan Bakwan", "price": 50000},
        ],
        "total": 8000
    },
    {
        "restaurant": "Kopi Kenangan",
        "date": "2026-04-10",  # last 7 days
        "items": [
            {"name": "Mantan Latte", "price": 25000},
            {"name": "Pistachio Butter Latte", "price": 27000},
        ],
        "total": 52000
    },
]

for i, r in enumerate(receipts):
    items_html = ""
    for item in r['items']:
        items_html += f"""
        <tr>
            <td>{item['name']}</td>
            <td>Rp {item['price']:,}</td>
        </tr>"""

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ font-family: monospace; width: 300px; margin: 20px auto; }}
            h2   {{ text-align: center; }}
            hr   {{ border-top: 1px dashed black; }}
            table {{ width: 100%; }}
            .total {{ font-weight: bold; font-size: 1.2em; }}
        </style>
    </head>
    <body>
        <h2>{r['restaurant']}</h2>
        <p style="text-align:center">{r['date']}</p>
        <hr>
        <table>{items_html}</table>
        <hr>
        <table>
            <tr class="total">
                <td>TOTAL</td>
                <td>Rp {r['total']:,}</td>
            </tr>
        </table>
        <hr>
        <p style="text-align:center">Terima Kasih!</p>
    </body>
    </html>
    """
    with open(f"./Dummy Receipt/receipt_{i+1}_{r['restaurant'].replace(' ', '_')}.html", "w") as f:
        f.write(html)
    print(f"✅ Generated: receipt_{i+1}.html")