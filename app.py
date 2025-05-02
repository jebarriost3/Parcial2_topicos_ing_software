from flask import Flask, render_template
import math

app = Flask(__name__)

@app.route('/factorial/<int:num>')
def calcular_factorial(num):
    try:
        resultado = math.factorial(num)
        return render_template('factorial.html', numero=num, resultado=resultado)
    except ValueError:
        return "Número inválido"

if __name__ == '__main__':
    app.run(debug=True)
