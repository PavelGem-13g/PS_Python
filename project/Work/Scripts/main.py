# -*- coding: utf-8 -*-

import sys
import os

os.chdir("../Library")
import data_loader
import plots
import sorter

import pandas

if __name__ == "__main__":
    df = data_loader.get_database()
    sorter.makeOutputs(df)
    plots.generate_plots(df)