from flask import Flask, render_template
import subprocess  # Untuk menjalankan script Python Turtle

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_hbd', methods=['POST'])
def run_hbd():
    # Jalankan file turtle_hbd.py sebagai proses terpisah
    subprocess.Popen(["python", "turtle_hbd.py"])
    return "🎉 Animasi Python dijalankan! 🎉"

if __name__ == '__main__':
    app.run(debug=True)