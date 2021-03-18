from flask import Flask

app = Flask("microblog")

#aqui vai comentario
@app.route("/")
def index():
    return "Olá Mundo"

app.run()