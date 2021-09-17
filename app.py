import numpy as np
import pandas as pd
from flask import Flask,render_template,request
import pickle
import datetime

app=Flask(__name__,template_folder='templates')
mod=pickle.load(open('linear_pkl.pkl','rb'))

@app.route('/')
@app.route('/index')
def Index():
    return render_template('index.html')
	
	
@app.route('/result',methods=['GET','POST'])

def result():
    if request.method=='POST':
        year= int(request.form['year'])
        month= int(request.form['month'])
        day= int(request.form['day'])
        k=datetime.date(year,month,day)
        k=k.toordinal()
        predict=mod.predict([[k]])
        return render_template('index.html',prediction=predict)	
		
		
if __name__=='__main__':
    app.run(debug=True,use_reloader=False)		