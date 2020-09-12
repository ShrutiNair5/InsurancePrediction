# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 16:44:45 2020

@author: User
"""

from flask import Flask, render_template, request
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('random_forest.pkl', 'rb'))
@app.route('/',methods=['GET','POST'])

def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['GET','POST'])

def predict():
    # Fuel_Type_Diesel=0
    if request.method == 'POST':
        age = int(request.form['age'])
        sex = request.form['gender']
        if(sex=='Male'):
            sex=1
        else:
            sex=0
        bmi = float(request.form['bmi'])
        children = int(request.form['children'])
        smoker = request.form['smoker']
        if(smoker=='Yes'):
            smoker=1
        else:
            smoker=0
        region = int(request.form['region'])
        
        prediction=model.predict([[age,sex,bmi,children,smoker,region]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction="Sorry, No insurance")
        else:
            return render_template('index.html',prediction="Insurance Expense is: ${}".format(output))
if __name__=="__main__":
    app.run(debug=True)
