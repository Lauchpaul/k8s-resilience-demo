import requests
from flask import Flask, render_template_string

app = Flask(__name__)
targets = {
    "Opfer 1 (Port 4000)": "http://victim-1:8080",
    "Opfer 2 (Port 4001)": "http://victim-2:8080",
    "Opfer 3 (Port 4002)": "http://victim-3:8080"
}

html = """
<!DOCTYPE html>
<html>
<body style="background:#121212; color:white; font-family:monospace; text-align:center;">
    <h1>K8s Kill-Switch (Port 6969)</h1>
    <div style="display:flex; justify-content:center; gap:20px;">
        {% for name, url in targets.items() %}
        <div style="border:1px solid #444; padding:20px; width:200px; background:#1e1e1e;">
            <h3>{{ name }}</h3>
            <button onclick="fetch('/kill/{{ loop.index }}', {method:'POST'}).then(() => alert('Kill-Signal gesendet! K8s startet den Pod jetzt neu.'))" 
                    style="background:red; color:white; padding:10px 20px; border:none; cursor:pointer; font-weight:bold;">
                KILLEN
            </button>
        </div>
        {% endfor %}
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html, targets=targets)

@app.route('/kill/<int:idx>', methods=['POST'])
def kill(idx):
    url = list(targets.values())[idx-1]
    try: 
        requests.post(url + '/crash', timeout=1)
    except: 
        pass # Wenn er schon tot ist, juckt uns das nicht
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
