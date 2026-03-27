import os, signal
from flask import Flask

app = Flask(__name__)
pod = os.environ.get('POD_NAME', 'Unknown')
port = os.environ.get('PORT_NUM', 'Unknown')

@app.route('/')
def home():
    return f"""
    <body style="background:#121212; color:#0f0; font-family:monospace; text-align:center; padding:50px;">
        <h1>I am alive!</h1>
        <h2>Port: {port}</h2>
        <h3>Pod-Name: {pod}</h3>
        <p>Gehe auf Port 6969 um mich zu killen.</p>
    </body>
    """

@app.route('/crash', methods=['POST'])
def crash():
    os.kill(os.getpid(), signal.SIGTERM)
    return "RIP"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
