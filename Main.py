from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route('/calcular', methods=['POST'])
def calcular():
    nome = request.form['nome']
    idade = int(request.form['idade'])
    invest_inicial = float(request.form['invest_inicial'])
    invest_time = int(request.form['invest_time'])
    taxa = float(request.form['taxa']) / 100  # Convertendo para percentual
    aporte = float(request.form['aporte'])
    renda_desejada = float(request.form['renda_desejada'])

    # O código de cálculo (baseado no seu código anterior)
    montante = invest_inicial
    for tempo_decorrido in range(invest_time):
        montante = (montante + aporte) * (1 + taxa)
        montante = round(montante, 2)

    renda_mensal_final = round(montante * taxa, 2)

    if renda_mensal_final >= renda_desejada:
        resultado = f"Parabéns, {nome}! No fim do período de investimento, você terá R$ {montante}. Seu salário mensal será de R$ {renda_mensal_final}, atingindo sua meta."
    else:
        resultado = f"Infelizmente, {nome}, seu salário mensal será de R$ {renda_mensal_final}, que é menor que o desejado de R$ {renda_desejada}."

    return render_template('resultado.html', resultado=resultado)


@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)




if __name__ == "__main__":
    app.run(debug=True)


pip freeze requirements