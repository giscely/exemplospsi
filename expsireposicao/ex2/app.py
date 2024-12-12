from flask import Flask, request, render_template, make_response, redirect, url_for

app = Flask(__name__)

# Rota da página inicial
@app.route('/')
def home():
    return render_template('index.html')

# Rota do formulário de feedback
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        comentario = request.form.get('comentario')

        # Validação simples
        if not nome or not email:
            error_message = "Nome e email são obrigatórios."
            return render_template('feedback.html', error=error_message, nome=nome, email=email, comentario=comentario)

        # Armazenar nome em um cookie
        resp = make_response(f"Obrigado pelo feedback, {nome}! Comentário recebido: {comentario}. Seu email: {email}.")
        resp.set_cookie('username', nome)
        return resp

    return render_template('feedback.html')

# Rota para acessar o cookie
@app.route('/welcome')
def welcome():
    nome = request.cookies.get('username', 'Visitante')
    return f"Bem-vindo de volta, {nome}!"

if __name__ == '__main__':
    app.run(debug=True)
