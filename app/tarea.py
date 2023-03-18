import csv
import problema_1

def read_csv(ubicacion):
    with open(ubicacion, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header,row)
            country_dict = {key:value for key, value in iterable}
            data.append(country_dict)
    return data

if __name__ == '__main__':
    data = read_csv('./world_population.csv')
    desicion = int(input('Digite 1. para hacer una busqueda de poblacion por pais \nDigite 2. para hacer un grafico de pastel del total de la poblacion mundial'))
    if desicion == 1:
        datos_grafica = problema_1.busqueda(data)
        labels , values = datos_grafica
        problema_1.generate_bar_chart(labels,values)
    elif desicion ==2:
        datos_percentiles = problema_1.datos_percentiles(data)
        labels , values = datos_percentiles
        print(datos_percentiles)
        problema_1.generate_pie_chart(labels,values)
        
    else:
        print('Esta opcion no es valida')
        