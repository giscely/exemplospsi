from flask import Flask, request, render_template, make_response, redirect, url_for
import uuid

app = Flask(__name__)

# Lista para armazenar mensagens e um dicionário para associar identificadores únicos
mensagens = []
visitantes = {}

# Rota da página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para enviar mensagens
@app.route('/enviar_mensagem', methods=['GET', 'POST'])
def enviar_mensagem():
    if request.method == 'POST':
        mensagem = request.form.get('mensagem')
        
        # Validação: cheque se a mensagem não está vazia
        if not mensagem:
            error_message = "A mensagem não pode estar vazia."
            return render_template('enviar_mensagem.html', error=error_message)

        # Gerar um identificador único para o visitante
        visitante_id = request.cookies.get('visitante_id')
        if not visitante_id:
            visitante_id = str(uuid.uuid4())  # Gera um novo ID se não existir
            resp = make_response(redirect(url_for('mensagens')))
            resp.set_cookie('visitante_id', visitante_id)
            visitantes[visitante_id] = []  # Cria uma nova lista para o visitante
            visitantes[visitante_id].append(mensagem)
            return resp
        
        # Armazenar mensagem associada ao visitante
        visitantes[visitante_id].append(mensagem)

        return redirect(url_for('mensagens'))

    return render_template('enviar_mensagem.html')

# Rota para mostrar mensagens
@app.route('/mensagens')
def mensagens():
    # Compilar todas as mensagens para exibição
    todas_mensagens = []
    for mensagens_usuario in visitantes.values():
        todas_mensagens.extend(mensagens_usuario)

    return render_template('mensagens.html', lista_mensagem=todas_mensagens)

if __name__ == '__main__':
    app.run(debug=True)