from flask import Flask, request

app = Flask(__name__)

faults = {
    "Charging": [
        "Charging nahi ho rahi",
        "Slow charging",
        "Charging connect disconnect"
    ],
    "Battery": [
        "Battery jaldi khatam",
        "Battery percentage stuck"
    ],
    "Display": [
        "Display black",
        "Touch kaam nahi karta",
        "Display lines"
    ],
    "Audio": [
        "Speaker band",
        "Mic kaam nahi karta"
    ],
    "Network": [
        "Signal nahi aa raha",
        "SIM detect nahi hoti",
        "WiFi issue"
    ],
    "Power": [
        "Phone dead",
        "Restart loop",
        "Phone heating"
    ]
}

solutions = {
    "Charging nahi ho rahi": "Cable, adapter, charging port aur charging circuit inspect karein.",
    "Slow charging": "Adapter, cable, port aur battery condition check karein.",
    "Charging connect disconnect": "Charging port aur cable connection inspect karein.",
    "Battery jaldi khatam": "Battery health aur background apps check karein.",
    "Battery percentage stuck": "Battery connection aur monitoring circuit diagnose karein.",
    "Display black": "Display connector aur display assembly check karein.",
    "Touch kaam nahi karta": "Touch panel aur display connector inspect karein.",
    "Display lines": "Display assembly check karein.",
    "Speaker band": "Speaker module aur contacts inspect karein.",
    "Mic kaam nahi karta": "Mic module aur flex check karein.",
    "Signal nahi aa raha": "SIM, network settings aur antenna check karein.",
    "SIM detect nahi hoti": "SIM tray aur SIM reader inspect karein.",
    "WiFi issue": "Software settings aur WiFi hardware diagnose karein.",
    "Phone dead": "Battery, charger aur power circuit check karein.",
    "Restart loop": "Software aur battery stability check karein.",
    "Phone heating": "Phone use band karein aur excessive heating par technician se inspection karwayein."
}

@app.route("/")
def home():
    q = request.args.get("q", "").lower()
    category = request.args.get("category", "")

    results = []

    for cat, items in faults.items():
        for item in items:
            if q in item.lower() and q:
                results.append(item)

    html = """
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
    body{background:#08111f;color:white;font-family:Arial;padding:12px}
    h1{color:#00cfff;text-align:center}
    .box{background:#14283e;padding:15px;margin:10px 0;border-radius:12px}
    button,input{width:100%;padding:13px;margin:5px 0;border:0;border-radius:8px}
    button{background:#087eae;color:white}
    </style>
    </head>
    <body>
    <h1>SAHIL MOBILE REPAIR</h1>

    <div class="box">
    <form>
    <input name="q" placeholder="Search mobile fault">
    <button>Search Fault</button>
    </form>
    </div>

    {% for item in results %}
    <div class="box">
    <b>{{item}}</b>
    <p>{{solutions[item]}}</p>
    </div>
    {% endfor %}

    <h3>Repair Categories</h3>

    {% for cat in categories %}
    <form>
    <button name="category" value="{{cat}}">{{cat}}</button>
    </form>
    {% endfor %}

    {% if selected %}
    <div class="box">
    <h2>{{category}}</h2>
    {% for item in selected %}
    <p><b>{{item}}</b></p>
    <p>{{solutions[item]}}</p>
    {% endfor %}
    </div>
    {% endif %}

    </body>
    </html>
    """

    from flask import render_template_string

    return render_template_string(
        html,
        results=results,
        categories=faults.keys(),
        selected=faults.get(category, []),
        category=category,
        solutions=solutions
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
