import os
import sys

from model.cabbage_model import CabbageModel
from model.calculator_model import CalculatorModel
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('cabbage.html')

@app.route("/calc", methods=["post"])
def calc():
     num1 = request.form['num1']
     num2 = request.form['num2']
     opcode = request.form['opcode']
     calc = CalculatorModel()
     result = calc.calc(num1,num2,opcode)
     render_params ={}
     render_params['result'] = result
     return render_template('index.html', **render_params)

@app.route("/cabbage", methods=["post"])
def cabbage():
     avg_temp = request.form['avg_temp']
     min_temp = request.form['min_temp']
     max_temp = request.form['max_temp']
     rain_fall = request.form['rain_fall']
     cabbage = CabbageModel()
     result = cabbage.load_model(avg_temp,min_temp,max_temp,rain_fall)
     render_params ={}
     render_params['result'] = result
     return render_template('cabbage.html', **render_params)
     
          

if __name__ == '__main__':
     print(f'Started Server')
     app.run()