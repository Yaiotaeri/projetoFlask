from flask import Flask, render_template, request, redirect, session
import json
import os

app = Flask(__name__)
app.secret_key = 'chave-secreta-qualquer'  # Necessário para usar sessões

@app.route('/')
def index():
    # Tenta carregar o conteúdo do site salvo (ex: de um JSON)
    try:
        with open('site_data.json', 'r') as f:
            site_data = json.load(f)
    except FileNotFoundError:
        site_data = {
            "titulo": "Bem-vindo ao site!",
            "descricao": "Descrição padrão...",
            "imagem": "",
            "imagemTwo": "",
            "tituloCor": "#000000",
            "produtos": [
                {
                    "nome": "Produto 1",
                    "preco": "R$ 100,00",
                    "imagem": "",
                    "corNome": "#000000",
                    "corPreco": "#ff0000"
                }
            ]
        }

    is_admin = session.get('usuario') == 'Jorge'
    return render_template('index.html', site=site_data, admin=is_admin)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')  # Corrigido para exibir o formulário

    usuario = request.form.get('usuario')
    senha = request.form.get('senha')

    try:
        with open('usuarios.json', 'r') as f:
            dados = json.load(f)
    except FileNotFoundError:
        dados = []

    for user in dados:
        if user['usuario'] == usuario and user['senha'] == senha:
            session['usuario'] = usuario
            return redirect('/')
    
    return "Usuário ou senha incorretos!"

@app.route('/salvar', methods=['POST'])
def salvar():
    if session.get('usuario') != 'Jorge':
        return "Acesso negado!"

    # Pega os dados do formulário de edição geral
    titulo = request.form.get('titulo')
    descricao = request.form.get('descricao')
    imagem = request.form.get('imagem')
    imagemTwo = request.form.get('imagemTwo')
    tituloCor = request.form.get('tituloCor')

    site_data = {
        "titulo": titulo,
        "descricao": descricao,
        "imagem": imagem,
        "imagemTwo": imagemTwo,
        "tituloCor": tituloCor
    }

    # Processar produtos
    produtos = []
    for i in range(3):  # Ajuste conforme a quantidade de produtos suportados
        nome = request.form.get(f'produtos[{i}][nome]')
        imagem_produto = request.form.get(f'produtos[{i}][imagem]')
        preco = request.form.get(f'produtos[{i}][preco]')
        corNome = request.form.get(f'produtos[{i}][corNome]')
        corPreco = request.form.get(f'produtos[{i}][corPreco]')

        if nome and preco:
            produtos.append({
                "nome": nome,
                "imagem": imagem_produto,
                "preco": preco,
                "corNome": corNome or "#000000",
                "corPreco": corPreco or "#000000"
            })

    site_data["produtos"] = produtos

    with open('site_data.json', 'w') as f:
        json.dump(site_data, f)

    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
