from flask import Flask, request, render_template, make_response, redirect, url_for

app = Flask(__name__)

# Dicionário para armazenar mensagens por usuário
usuarios_mensagens = {}

# Rota da página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        resp = make_response(redirect(url_for('enviar_mensagem')))
        resp.set_cookie('username', username)
        return resp
    return render_template('login.html')

# Rota para enviar mensagens
@app.route('/enviar_mensagem', methods=['GET', 'POST'])
def enviar_mensagem():
    username = request.cookies.get('username')
    if not username:
        return redirect(url_for('login'))

    if request.method == 'POST':
        mensagem = request.form.get('mensagem')
        if username not in usuarios_mensagens:
            usuarios_mensagens[username] = []
        usuarios_mensagens[username].append(mensagem)
        return redirect(url_for('mensagens'))

    return render_template('enviar_mensagem.html')

# Rota para mostrar mensagens
@app.route('/mensagens')
def mensagens():
    username = request.cookies.get('username')
    if not username:
        return redirect(url_for('login'))
    
    # Lista de mensagens do usuário
    lista_mensagem = usuarios_mensagens.get(username, [])
    return render_template('mensagens.html', lista_mensagem=lista_mensagem)

if __name__ == '__main__':
    app.run(debug=True)