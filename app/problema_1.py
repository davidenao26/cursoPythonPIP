import matplotlib.pyplot as plt
import numpy as np

def transformacion(datos):
    data_poblacional = []
    new_dict={}
    for item in datos:
        new_dict.clear()
        for key in item:
            if ('Population' in key) and ('World' not in key):
                new_dict.update({key[:4]:int(item[key])})
        data_poblacional.append(new_dict)
    return data_poblacional

def busqueda(datos):
    country = input('Type Country =>     ')
    new_dict={}
    for item in datos:
        if item['Country/Territory']==country.title():
            for key in item:
                if ('Population' in key) and ('World' not in key):
                    new_dict.update({key[:4]:int(item[key])})
            keys = list(new_dict.keys())
            values = list(new_dict.values())
    return keys, values

def datos_percentiles(datos):
    labels = []
    keys = []
    for item in datos:
        labels.append(item['CCA3'])
        keys.append(item['World Population Percentage'])

    return labels, keys

def generate_bar_chart(labels,values):
    fig, ax = plt.subplots()
    ax.bar(labels,values)
    plt.show()

def generate_pie_chart(labels,values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.show()    
