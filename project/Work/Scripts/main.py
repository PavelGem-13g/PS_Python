"""
Сервер на Flask
"""

# -*- coding: utf-8 -*-
import os
import sys
import pickle
import webbrowser
from pandas import DataFrame
from flask import Flask, render_template, request, redirect, send_file, jsonify

library_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Library'))
sys.path.append(library_path)
import data_loader
import plots
import sorter
import predictor
import saver

app = Flask(__name__)
DF = []
MODEL = []


@app.route('/')
def upload_dataset():
    """
    Страница загрузки датасета

    Returns
    -------
    HTML
        Страница.

    """
    return render_template("index.html", message="")


@app.route('/senddataset', methods=['POST'])
def success():
    """
    Загрузка датасета

    Returns
    -------
    HTML
        Страница.

    """
    global DF
    if request.method == 'POST':
        _f = request.files['file']
        if _f.filename == '':
            return render_template("index.html", message="Файл не найден")
        _f.save(_f.filename)
        os.replace(_f.filename, "../Data/" + _f.filename)
        DF = data_loader.get_database(_f.filename)
        if not data_loader.check_dataset(DF):
            return render_template("index.html", message="Неверный датасет")
    return redirect('/work')


@app.route('/work')
def work():
    """
    Страница работы приложения

    Returns
    -------
    HTML
        Страница.

    """
    global DF
    plt = plots.generate_plots(DF)
    tab = sorter.makeOutputs(DF)
    data = DF.to_html()
    return render_template("work.html", plots=plt, tables=tab, data=data)


@app.route('/downloaddataset')
def downloaddataset():
    """
    Скачивание датасета

    Returns
    -------
    File
        Запрошенный файл.

    """
    global DF
    saver.saveDataFrameToCSV('Edited', DF)
    return send_file('../Outputs/' + 'Edited.csv')


@app.route('/addrow', methods=['POST'])
def addrow():
    """
    Добавление записи

    Returns
    -------
    HTML
        Страница.

    """
    global DF
    if request.method == 'POST':
        print(request)
        DF.loc[DF.index[-1] + 1] = [DF.index[-1] + 2,
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


@app.route('/deleterow', methods=['POST'])
def deleterow():
    """
    Удаление записи

    Returns
    -------
    HTML
        Страница.

    """
    global DF
    if request.method == 'POST':
        DF = DF.drop(DF.index[DF['Rank'] == int(request.form.get('delete-number'))])
    return redirect('/work')


@app.route('/updaterow', methods=['POST'])
def updaterow():
    """
    Обновление записи

    Returns
    -------
    HTML
        Страница.

    """
    global DF
    if request.method == 'POST':
        DF.loc[DF.index[DF['Rank'] == int(request.form.get('update-number'))]]=[
            int(request.form.get('update-number')),
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


@app.route('/plot/common/<title>')
def get_plot_common(title):
    """
    Генерация графиков

    Parameters
    ----------
    title : str
        Атрибут 1.

    Returns
    -------
    JSON
        Результат работы.

    """
    fig = plots.common_plot(DF, title)
    return jsonify({'data': fig.to_html()})


@app.route('/plot/box/<name1>/<name2>')
def get_plot_box(name1, name2):
    """
    Генерация графиков box

    Parameters
    ----------
    name1 : str
        Атрибут 1.
    name2 : str
        Атрибут 2.

    Returns
    -------
    JSON
        Результат работы.

    """
    fig = plots.box_plot(DF, name1, name2)
    return jsonify({'data': fig.to_html()})


@app.route('/plot/scatter/<x_name>/<y_name>/<color_name>/<size_name>/<animation_name>')
def get_plot_scatter(x_name, y_name, color_name, size_name, animation_name):
    """
    Генерация графиков scatter

    Parameters
    ----------
    x_name : str
        Атрибут 1.
    y_name : str
        Атрибут 2.
    color_name : str
        Атрибут 3.
    size_name : str
        Атрибут 4.
    animation_name : str
        Атрибут 5.

    Returns
    -------
    JSON
        Результат работы.

    """
    fig = plots.scatter_plot(DF, x_name, y_name, color_name, size_name, animation_name)
    return jsonify({'data': fig.to_html()})


@app.route('/plot/pie/<names>')
def get_plot_pie(names):
    """    
    Parameters
    ----------
    names : str
        Атрибут 1.

    Returns
    -------
    JSON
        Результат работы.

    """
    fig = plots.pie_plot(DF, names)
    return jsonify({'data': fig.to_html()})


@app.route('/download/<file>', methods=['GET', 'POST'])
def downloading(file):
    """
    Скачивание отчета

    Parameters
    ----------
    file : str
        Название файла.

    Returns
    -------
    File
        Запрашиваемый файл.

    """
    return send_file('../Outputs/' + file)


@app.route('/filtration', methods=['GET', 'POST'])
def filtration():
    """
    Фильтрация значений

    Returns
    -------
    JSON
        Результат работы.

    """
    global DF
    saver.saveDataFrameToCSV(
        request.form.get('filtration-filename'),
        sorter.filterByValue(
            DF,
            request.form.get('filtration-answer'),
            int(request.form.get('filtration-value')),
            request.form.get('filtration-sign')))
    return jsonify({'filename': request.form.get('filtration-filename')})


@app.route('/crosstab', methods=['GET', 'POST'])
def crosstab():
    """
    Перечение значений

    Returns
    -------
    JSON
        Результат работы.

    """
    print(request.form.get('crosstab-filename'),
          request.form.get("crosstab-select-1"),
          request.form.get('crosstab-select-2'))
    saver.saveDataFrameToCSV(
        request.form.get('crosstab-filename'),
        sorter.crosstab(
            DF,
            request.form.get("crosstab-select-1"),
            request.form.get("crosstab-select-2")
        ))
    return jsonify({'filename': request.form.get('crosstab-filename')})


@app.route('/model/learn', methods=['POST'])
def learn():
    """
    Обучение модели

    Returns
    -------
    JSON
        Результат работы.

    """
    global MODEL, DF
    model_df = predictor.normalize(DF)
    MODEL = predictor.train_model(model_df)
    return jsonify({'status': 'ok'})


@app.route('/model/model.pkl')
def downloadmodel():
    """
    Скачивание модели

    Returns
    -------
    File
        Запрашиваемый файл.

    """
    global MODEL
    saver.save_model('model', MODEL)
    return send_file('../Outputs/' + 'model.pkl')


@app.route('/model/upload', methods=['POST'])
def load_model():
    """
    Загрузка модели

    Returns
    -------
    JSON
        Результат работы.

    """
    global MODEL
    _f = request.files['learn-model']
    _f.save(_f.filename)
    os.replace(_f.filename, "../Data/" + _f.filename)
    with open("../Data/" + _f.filename, 'rb') as file:
        MODEL = pickle.load(file)
    saver.save_model('model', MODEL)
    return jsonify({'message': 'Model successfully loaded!'})


@app.route('/model/predict', methods=['POST'])
def predict():
    """
    Предсказывание результата

    Returns
    -------
    JSON
        Результат работы.

    """
    global MODEL
    result = predictor.predict(MODEL,
                               DataFrame({
                                   'Ranked2021': int(request.form.get('Ranked2021')),
                                   'Ranked2020': int(request.form.get('Ranked2020')),
                                   'Country': int(request.form.get('Country')),
                                   'Sector': int(request.form.get('Sector')),
                                   'CAGR': int(request.form.get('CAGR')),
                                   'Revenue2017': int(request.form.get('Revenue2017')),
                                   'Employees2020': int(request.form.get('Employees2020')),
                                   'Employees2017': int(request.form.get('Employees2017')),
                                   'FoundingYear': int(request.form.get('FoundingYear'))
                               }, index=[0]))
    print(result)
    return jsonify({'result': result[0]})


if __name__ == "__main__":
    """
    Запуск
    """
    webbrowser.open_new("http://127.0.0.1:5000/")
    app.run()
