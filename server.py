from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

messages = []

@app.route('/messages', methods=['GET', 'POST'])
def handle_messages():
    if request.method == 'POST':
        print("Cabecalho da requsição --> : ", request.headers)
        message = request.json['message']
        messages.append(message)
        return jsonify({'message': 'Message sent successfully!'})
    elif request.method == 'GET':
        print("Cabecalho da requsição --> : ", request.headers)
        return jsonify({'messages': messages})

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)



# O cabeçalho HTTP é definido na RFC 2616 (obsoleta) e na RFC 7230-7237.
# O cabeçalho HTTP consiste em duas partes principais: a primeira linha (também chamada de linha de solicitação ou linha de status) e os cabeçalhos de campo. 
# A primeira linha é usada para identificar o método HTTP usado (no caso de uma solicitação) ou o código de status HTTP retornado (no caso de uma resposta). 