# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 18:06:38 2020

@author: NILAY
"""
from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np
import pandas as pd
app = Flask(__name__)

model=pickle.load(open('suicide_model_pipe.pkl','rb'))
X_obt=pd.read_csv('new_deploy.csv')

@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    data1=request.form['State_UT']
    data3=request.form['Type']
    data4=request.form['gender']
    data5=request.form['age']
    d={'State':[data1],'Type':[data3],'Gender':[data4],'Age_group':[data5]}
    test=pd.DataFrame(d)
    prediction_test=model.predict(test).round()
    return render_template('index.html',Make_Prediction='The number of people who commited suicide due to {} in {} is {}'.format(data3,data1,int(prediction_test[0])))



if __name__=='__main__':
    app.run(debug=True)
