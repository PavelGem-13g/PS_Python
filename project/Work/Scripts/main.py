# -*- coding: utf-8 -*-

import sys
import os
os.chdir("../Library")
import data_loader
import plots


if __name__ == "__main__":
    data, country, sectors, date, ranked_values = data_loader.load_data()
    plots.generate_plots(data, country, sectors, date, ranked_values)