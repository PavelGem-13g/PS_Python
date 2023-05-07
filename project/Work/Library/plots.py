# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

import data_loader


def generate_plots(data, country, sectors, date, ranked_values):
    for i in range(1,len(data)):
        country[str(data[i][4])]+=int(data[i][7])
        sectors[str(data[i][5])]+=int(data[i][7])
        date[str(data[i][11])]+=int(data[i][7])
   
    plt.plot(country.keys(), country.values())
    plt.savefig('../Graphics/country.png')
    plt.show()

    plt.plot(sectors.keys(), sectors.values())
    plt.savefig('../Graphics/sectors.png')
    plt.show()
 
    plt.plot(date.keys(), date.values())
    plt.savefig('../Graphics/date.png')
    plt.show()


if __name__ == "__main__":
    data, country, sectors, date, ranked_values = data_loader.load_data()
    generate_plots(data, country, sectors, date, ranked_values)