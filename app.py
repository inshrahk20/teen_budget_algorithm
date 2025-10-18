from flask import Flask, render_template_string, request
import json

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>✨ Teen Budgeting Tool 💅</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<style>
body {
    background-color: #ffeaf4;
    font-family: 'Poppins', 'Comic Sans MS', cursive;
    color: #333;
    text-align: center;
    margin: 0;
    padding: 20px;
}
h1 {
    color: #ff4fae;
    text-shadow: 1px 1px #ffd6e8;
}
input, button, textarea {
    padding: 10px;
    border-radius: 12px;
    border: 1px solid #ccc;
    margin: 5px;
    width: 230px;
    background-color: #fff9fc;
}
button {
    background-color: #ff90c2;
    color: white;
    border: none;
    cursor: pointer;
    transition: 0.3s;
}
button:hover {
    background-color: #ff64a7;
}
.container {
    background-color: #ffffffcc;
    border-radius: 20px;
    box-shadow: 0 0 15px rgba(255, 143, 193, 0.4);
    padding: 20px;
    display: inline-block;
}
canvas {
    margin-top: 15px;
    width: 250px !important;
    height: 250px !important;
}
table {
    margin: 10px auto;
    border-collapse: collapse;
    background-color: #fff9fc;
    border-radius: 15px;
}
td, th {
    padding: 8px 15px;
    border: 1px solid #ffc4dc;
}
th {
    background-color: #ffb6d9;
}
textarea {
    height: 80px;
}
</style>
</head>
<body>
<div class="container">
<h1>🎀 Teen Budget Tracker ✨</h1>
<p>Hey sup 👀💅 let’s make sure your money isn’t crying this month 💸😭</p>

<form method="POST">
  💰 Allowance (Rs): <input type="number" name="allowance" required><br>
  💳 Expenses (Rs): <input type="number" name="expenses" required><br>
  🏦 Emergency Fund (Rs): <input type="number" name="emergency" value="0"><br>
  🛍️ Wishlist item(s) & cost (e.g. Phone=30000, Bag=5000):<br>
  <textarea name="wishlist"></textarea><br>
  🧾 Things you’ve already spent on (e.g. Snacks=500, Movie=1000):<br>
  <textarea name="spent_items"></textarea><br>
  <button type="submit">Calculate 💕</button>
</form>

{% if result %}
<h2>{{ result|safe }}</h2>

{% if report %}
<h3>📊 Monthly Budget Summary</h3>
<table>
<tr><th>Category</th><th>Amount (Rs)</th></tr>
{% for key, value in report.items() %}
<tr><td>{{ key }}</td><td>{{ value }}</td></tr>
{% endfor %}
</table>

<canvas id="budgetChart"></canvas>
<script>
const data = {
    labels: {{ chart_labels|safe }},
    datasets: [{
        label: 'Budget Allocation',
        data: {{ chart_data|safe }},
        backgroundColor: ['#ff90c2','#ffc8dd','#ffd6e8','#ffb6c1','#ffe5ec'],
        borderWidth: 1
    }]
};

const config = {
    type: 'pie',
    data: data,
};

new Chart(
    document.getElementById('budgetChart'),
    config
);
</script>

{% if wishlist_items %}
<h3>💖 Wishlist Breakdown</h3>
<ul>
{% for item, price in wishlist_items.items() %}
<li>{{ item }} — Rs.{{ price }}</li>
{% endfor %}
</ul>
{% endif %}

{% if spent_breakdown %}
<h3>🧾 Spent Items Breakdown</h3>
<ul>
{% for item, price in spent_breakdown.items() %}
<li>{{ item }} — Rs.{{ price }}</li>
{% endfor %}
</ul>
{% endif %}

{% endif %}
{% endif %}
</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    report = None
    chart_labels = chart_data = None
    wishlist_items = {}
    spent_breakdown = {}

    if request.method == "POST":
        allowance = float(request.form["allowance"])
        expenses = float(request.form["expenses"])
        emergency = float(request.form["emergency"])

        def parse_items(text):
            items = {}
            if text.strip():
                for pair in text.split(","):
                    if "=" in pair:
                        name, price = pair.split("=")
                        items[name.strip()] = float(price.strip())
            return items

        wishlist_items = parse_items(request.form["wishlist"])
        spent_breakdown = parse_items(request.form["spent_items"])

        wishlist_total = sum(wishlist_items.values())
        spent_total = sum(spent_breakdown.values())

        leftover = allowance - (expenses + emergency + spent_total)
        result_msg = ""

        if leftover < 0:
            result_msg = f"😭 Broke alert! You’re short by Rs.{abs(leftover):.2f} 🔫"
        elif leftover == 0:
            result_msg = "💀 You broke even — impressive balance!"
        else:
            result_msg = f"🎀 Yay! You saved Rs.{leftover:.2f}! 💅"

        result = result_msg

        report = {
            "Allowance": allowance,
            "Expenses": expenses,
            "Emergency Fund": emergency,
            "Spent Items": spent_total,
            "Leftover": max(leftover, 0)
        }

        chart_labels = json.dumps(list(report.keys()))
        chart_data = json.dumps(list(report.values()))

    return render_template_string(HTML, result=result, report=report,
                                  chart_labels=chart_labels, chart_data=chart_data,
                                  wishlist_items=wishlist_items, spent_breakdown=spent_breakdown)

if __name__ == "__main__":
    app.run(debug=True)
