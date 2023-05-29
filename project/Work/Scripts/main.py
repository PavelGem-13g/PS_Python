# -*- coding: utf-8 -*-

import os

os.chdir("../Library")

import data_loader
import plots
import sorter
import predictor

os.chdir("../Scripts")

# if __name__ == "__main__":
#     df = data_loader.get_database()
#     sorter.makeOutputs(df)
#     plots.generate_plots(df)

import webbrowser
from pandas import DataFrame
from flask import Flask, render_template, request, redirect, url_for, send_file, jsonify

app = Flask(__name__)
df = []
model=[]

@app.route('/')
def upload_dataset():
    return render_template("index.html", message="")

@app.route('/senddataset', methods=['POST'])
def success():
    global df
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        os.replace(f.filename, "../Data/"+f.filename)
        df = data_loader.get_database(f.filename)
        # print(f.filename, data_loader.check_dataset(df))
        
        if(not data_loader.check_dataset(df)):
            # print("redirect")
            return render_template("index.html", message="Неверный датасет")
        
        return redirect('/work')

@app.route('/work')
def work():
    global df
    plt = plots.generate_plots(df)
    tab = sorter.makeOutputs(df)
    return render_template("work.html", plots=plt, tables=tab)


@app.route('/addrow', methods=['POST'])
def addrow():
    global df
    if request.method == 'POST':
        print(request)
        df.loc[len(df.index)] = [len(df.index)+1,
                                  request.form.get('Name'),
                                  request.form.get('Ranked2021'),
                                  request.form.get('Ranked2020'),
                                  request.form.get('Country'),
                                  request.form.get('Sector'),
                                  float(request.form.get('CAGR')),
                                  float(request.form.get('Revenue2020')),
                                  float(request.form.get('Revenue2017')),
                                  int(request.form.get('Employees2020')),
                                  int(request.form.get('Employees2017')),
                                  int(request.form.get('FoundingYear'))
                                  ]
    return redirect('/work')
    
    
@app.route('/download/<file>', methods=['GET', 'POST'])
def downloading(file):
    return send_file('../Outputs/'+file)


@app.route('/model/learn', methods=['POST'])
def learn():
    global model, df
    model_df = df
    model_df = predictor.normalize(df)
    X = predictor.get_X(model_df)
    Y = predictor.get_Y(model_df)
    model = predictor.train_model(model_df)
    return jsonify({'status':'ok'})#redirect('/work')

@app.route('/model/predict', methods=['POST'])
def predict():
    global model
    result = predictor.predict(model, 
                               DataFrame({
                                   'Ranked2021':int(request.form.get('Ranked2021')),
                                   'Ranked2020':int(request.form.get('Ranked2020')),
                                   'Country':int(request.form.get('Country')),
                                   'Sector':int(request.form.get('Sector')),
                                   'CAGR':int(request.form.get('CAGR')),
                                   'Revenue2017':int(request.form.get('Revenue2017')),
                                   'Employees2020':int(request.form.get('Employees2020')),
                                   'Employees2017':int(request.form.get('Employees2017')),
                                   'FoundingYear':int(request.form.get('FoundingYear'))
                                   }, index=[0]))
    print(result)
    return jsonify({'result':result[0]})


if __name__=="__main__":
    webbrowser.open_new("http://127.0.0.1:5000/")
    app.run()
