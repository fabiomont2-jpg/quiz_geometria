from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "equacoes_segundo_grau"

questoes = [

    {
        "pergunta": "Um cilindro possui raio de 3 cm e altura de 5 cm. Qual é seu volume?",
        "opcoes": {
            "a": "15π cm³",
            "b": "30π cm³",
            "c": "45π cm³",
            "d": "60π cm³"
        },
        "correta": "c",
        "explicacao": """
        V = πr²h

        V = π·3²·5

        V = π·9·5

        V = 45π cm³
        """
    },

    {
        "pergunta": "Um cone e um cilindro possuem a mesma altura e o mesmo raio da base. Qual a relação entre seus volumes?",
        "opcoes": {
            "a": "O volume será o mesmo",
            "b": "O volume do cone será três vezes menor que o volume do cilindro",
            "c": "O volume do cone será três vezes maior que o volume do cilindro",
            "d": "Não tem nenhuma relação"
        },
        "correta": "b",
        "explicacao": """
        Vcone = (1/3)πr²h

        Vcilindro = πr²h

        Portanto, o volume do cone é 1/3 do volume do cilindro.
        """
    },

    {
        "pergunta": "Um prisma reto possui área da base igual a 12 cm² e altura igual a 8 cm. Qual é o volume desse prisma?",
        "opcoes": {
            "a": "20 cm³",
            "b": "48 cm³",
            "c": "96 cm³",
            "d": "192 cm³"
        },
        "correta": "c",
        "explicacao": """
        V = Área da Base × Altura

        V = 12 × 8

        V = 96 cm³
        """
    },

    {
        "pergunta": "Uma pirâmide possui área da base igual a 30 cm² e altura igual a 9 cm. Qual é o volume da pirâmide?",
        "opcoes": {
            "a": "90 cm³",
            "b": "60 cm³",
            "c": "120 cm³",
            "d": "270 cm³"
        },
        "correta": "a",
        "explicacao": """
        V = (Área da Base × Altura) ÷ 3

        V = (30 × 9) ÷ 3

        V = 90 cm³
        """
    },

    {
        "pergunta": "Um cilindro possui raio de 4 cm e altura de 10 cm. Qual é o volume desse cilindro?",
        "opcoes": {
            "a": "80π cm³",
            "b": "120π cm³",
            "c": "160π cm³",
            "d": "200π cm³"
        },
        "correta": "c",
        "explicacao": """
        V = πr²h

        V = π·4²·10

        V = π·16·10

        V = 160π cm³
        """
    },

    {
        "pergunta": "Um cone possui raio da base igual a 3 cm e altura igual a 12 cm. Qual é o volume desse cone?",
        "opcoes": {
            "a": "12π cm³",
            "b": "24π cm³",
            "c": "36π cm³",
            "d": "48π cm³"
        },
        "correta": "c",
        "explicacao": """
        V = (πr²h) ÷ 3

        V = (π·3²·12) ÷ 3

        V = (108π) ÷ 3

        V = 36π cm³
        """
    },

    {
        "pergunta": "Qual sólido geométrico possui duas bases paralelas e congruentes?",
        "opcoes": {
            "a": "Cone",
            "b": "Pirâmide",
            "c": "Prisma",
            "d": "Esfera"
        },
        "correta": "c",
        "explicacao": """
        Os prismas possuem duas bases paralelas e congruentes.
        """
    },

    {
        "pergunta": "Qual é a unidade utilizada para expressar volume?",
        "opcoes": {
            "a": "cm",
            "b": "cm²",
            "c": "cm³",
            "d": "m"
        },
        "correta": "c",
        "explicacao": """
        O volume é medido em unidades cúbicas.

        Exemplo: cm³, m³.
        """
    },

    {
        "pergunta": "Uma caixa em formato de prisma retangular possui comprimento de 5 cm, largura de 4 cm e altura de 3 cm. Qual é seu volume?",
        "opcoes": {
            "a": "12 cm³",
            "b": "20 cm³",
            "c": "60 cm³",
            "d": "120 cm³"
        },
        "correta": "c",
        "explicacao": """
        V = comprimento × largura × altura

        V = 5 × 4 × 3

        V = 60 cm³
        """
    },

    {
        "pergunta": "Ao dobrar a altura de um cilindro sem alterar o raio da base, o volume:",
        "opcoes": {
            "a": "Permanece igual",
            "b": "Diminui pela metade",
            "c": "Dobra",
            "d": "Quadruplica"
        },
        "correta": "c",
        "explicacao": """
        V = πr²h

        Como o volume é diretamente proporcional à altura, ao dobrar a altura o volume também dobra.
        """
    }

]

@app.route('/')
def index():

    session.clear()
    session['pontuacao'] = 0
    session['questao'] = 0

    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():

    indice = session.get('questao', 0)

    if indice >= len(questoes):
        return redirect(url_for('resultado'))

    if request.method == 'POST':

        resposta = request.form.get('resposta')

        if resposta == questoes[indice]['correta']:
            session['pontuacao'] += 1

        session['questao'] += 1

        return redirect(url_for('quiz'))

    progresso = int((indice / len(questoes)) * 100)

    return render_template(
        'quiz.html',
        questao=questoes[indice],
        numero=indice + 1,
        total=len(questoes),
        progresso=progresso
    )

@app.route('/resultado')
def resultado():

    pontuacao = session['pontuacao']
    total = len(questoes)

    percentual = round((pontuacao / total) * 100)

    if percentual >= 90:
        medalha = "🥇 Ouro"
    elif percentual >= 70:
        medalha = "🥈 Prata"
    else:
        medalha = "🥉 Bronze"

    return render_template(
        'resultado.html',
        pontuacao=pontuacao,
        total=total,
        percentual=percentual,
        medalha=medalha
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
