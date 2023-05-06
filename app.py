from flask import Flask, render_template, request
import openai

app = Flask(__name__)
openai.api_key = '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'  # Reemplaza con tu propia API Key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reverte', methods=['POST'])
def reverte():
    text = request.form['text']  # Obtiene el texto ingresado por el usuario desde el formulario

    # Utiliza la API de OpenAI para generar el texto con el estilo de Arturo Pérez-Reverte
    generated_text = openai.Completion.create(
        engine='text-davinci-003',
        prompt=text,
        max_tokens=100,
        temperature=0.7
    ).choices[0].text.strip()

    return render_template('index.html', generated_text=generated_text, input_text=text)


if __name__ == '__main__':
    app.run()