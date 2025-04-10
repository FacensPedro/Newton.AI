from flask import Flask, request, jsonify, render_template
import google.generativeai as genai

app = Flask(__name__, static_folder='static', template_folder='templates')

# Substitua 'SUA_API_KEY_AQUI' pela sua chave de API real
genai.configure(api_key='Obtenha sua api em https://aistudio.google.com/apikey') 

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.form.get('message')
        if user_input:
            model = genai.GenerativeModel('gemini-2.0-flash')
            response = model.generate_content(
                f"""
                Seu nome é Newton.AI e você é um assistente de IA que ajuda nos estudos.
                Você é um especialista em calculos e em programação.
                Você está em estado alpha.
                Responda em português a seguinte pergunta: {user_input}
                """
            )
            return jsonify({"response": response.text})
        return jsonify({"response": "Envie uma mensagem válida."})
    except Exception as e:
        return jsonify({"response": f"Erro ao processar a solicitação: {str(e)}"}), 500