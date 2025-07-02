from flask import Flask, render_template_string, request
from scraper import Firstjob_Scraper, save_to_json

app = Flask(__name__)

# Plantilla HTML con CSS inline para diseño azul-blanco y botones redondeados
TEMPLATE = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FirstJob Scraper</title>
    <style>
        body { margin:0; font-family: Arial, sans-serif; background-color: #f4f7fa; }
        .header { background-color: #0052cc; color: white; padding: 20px; text-align: center; }
        .container { max-width: 800px; margin: 30px auto; background: white; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); padding: 20px; }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; font-weight: bold; }
        input[type=number] { width: 80px; padding: 8px; border: 1px solid #ccc; border-radius: 4px; }
        button { background-color: #0052cc; color: white; border: none; padding: 10px 20px; border-radius: 20px; cursor: pointer; font-size: 1rem; }
        button:hover { background-color: #003d99; }
        .job { border-bottom: 1px solid #eee; padding: 10px 0; }
        .job:last-child { border: none; }
        .job-title { font-size: 1.1rem; color: #0052cc; font-weight: bold; }
        .job-company { font-size: 1rem; color: #333; margin: 5px 0; }
        .job-location { font-size: 0.9rem; color: #666; }
        a { text-decoration: none; }
    </style>
</head>
<body>
    <div class="header">
        <h1>FirstJob Scraper</h1>
    </div>
    <div class="container">
        <form method="POST">
            <div class="form-group">
                <label for="limit">Cantidad de ofertas:</label>
                <input type="number" id="limit" name="limit" value="10" min="1" max="100" required>
            </div>
            <button type="submit">Buscar Ofertas</button>
        </form>
        {% if jobs %}
            <h2>Resultados ({{ jobs|length }})</h2>
            {% for job in jobs %}
                <div class="job">
                    <a href="{{ job.url }}" target="_blank">
                        <div class="job-title">{{ job.title }}</div>
                    </a>
                    <div class="job-company">{{ job.company }}</div>
                    <div class="job-location">{{ job.location }}</div>
                </div>
            {% endfor %}
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    jobs = []
    if request.method == 'POST':
        try:
            limit = int(request.form.get('limit', 10))
        except ValueError:
            limit = 10
        # Ejecutar scraper
        jobs = Firstjob_Scraper(limit=limit)
        save_to_json(jobs)
    return render_template_string(TEMPLATE, jobs=jobs)

if __name__ == '__main__':
    app.run(debug=True, port=5000)