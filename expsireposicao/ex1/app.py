from flask import Flask, render_template, request, make_response, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    
    # Criar um cookie
    resp = make_response(render_template('response.html', name=name, email=email))
    resp.set_cookie('username', name)
    
    return resp

@app.route('/email')
def email():
    email = request.args.get('email', 'Email não fornecido')
    return render_template('response.html', name=None, email=email)

if __name__ == '__main__':
    app.run(debug=True)
