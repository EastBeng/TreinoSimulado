from flask import Flask,render_template
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    url = 'https://meme-api.herokuapp.com/gimme'
    lista =[]
    for x in range(3):
        response = requests.get(url)
        dados = response.json()
        lista.append(dados)
    if dados['url']:
        urlMeme = dados['url']
        return render_template('index.html', url=urlMeme, dados = dados,lista = lista)
    return render_template('index.html', url="",dados=dados)



if __name__ == '__main__':
    app.run(debug=True, use_reload=True)
