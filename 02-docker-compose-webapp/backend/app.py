from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend Flask rodando no Docker!"

if __name__ == "__main__":
    # IMPORTANTE: host=0.0.0.0 permite acesso externo
    # debug=False evita que o processo termine automaticamente
    app.run(host="0.0.0.0", port=5000, debug=False)
