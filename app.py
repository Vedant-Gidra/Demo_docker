# docker build -t vedantgidra/table_app .
# docker run -p 8000:5000 vedantgidra/table_app

from flask import Flask, request, render_template_string

app = Flask(__name__)

TEMPLATE = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Multiplication Table</title>
    <style>
      body { font-family: Arial, sans-serif; margin: 40px; }
      input[type=number] { width: 80px; padding: 6px; }
      button { padding: 6px 12px; }
      table { border-collapse: collapse; margin-top: 20px; }
      td, th { border: 1px solid #ccc; padding: 8px 12px; }
    </style>
  </head>
  <body>
    <h1>Multiplication Table</h1>
    <form method="post">
      <label for="number">Enter a number:</label>
      <input id="number" name="number" type="number" min="1" required value="{{ number or '' }}" />
      <button type="submit">Show Table</button>
    </form>

    {% if table %}
      <h2>Table for {{ number }}</h2>
      <table>
        <thead>
          <tr><th>Multiplier</th><th>Result</th></tr>
        </thead>
        <tbody>
          {% for row in table %}
            <tr><td>{{ row.multiplier }}</td><td>{{ row.product }}</td></tr>
          {% endfor %}
        </tbody>
      </table>
    {% endif %}
  </body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    number = None
    table = None

    if request.method == 'POST':
        try:
            number = int(request.form.get('number', 0))
            if number > 0:
                table = [
                    {'multiplier': i, 'product': number * i}
                    for i in range(1, 11)
                ]
        except (ValueError, TypeError):
            number = None
            table = None

    return render_template_string(TEMPLATE, number=number, table=table)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
