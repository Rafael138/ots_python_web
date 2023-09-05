from flask import Flask, render_template

app = Flask("Meu app")

posts = [
    {"titulo":"Minha primeira postagem",
     "texto":"teste"
    },
    {"titulo":"Minha segunda postagem",
     "texto":"teste 2"
    }
]

@app.route('/')
def exibir_entradas():
    entradas=posts
    return render_template('exibir_entradas.html', entradas=entradas)