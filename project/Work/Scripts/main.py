# -*- coding: utf-8 -*-

import os

os.chdir("../Library")
import data_loader
import plots
import sorter

os.chdir("../Scripts")

# if __name__ == "__main__":
#     df = data_loader.get_database()
#     sorter.makeOutputs(df)
#     plots.generate_plots(df)

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def upload_dataset():
    return render_template("index.html")

@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        os.replace(f.filename, "../Data/"+f.filename)
        
        df = data_loader.get_database()
        plt = plots.generate_plots(df)
        return render_template("work.html", name=f.filename, plots=plt)

if __name__=="__main__":
    app.run()
