import pandas as pd

data = pd.read_csv('connection.csv', names=['LATITUD', 'LONGITUD', 'CATEGORIA'], sep=",", comment="#")
data['CATEGORIA'] = data['CATEGORIA'].astype('|S')
vertex_data = tuple(zip(data['LATITUD'].values, data['LONGITUD'].values, data['CATEGORIA'].values))

for d in vertex_data:
    x,y,z = d
    if z.decode('UTF-8') != 'nan':
        print(z.decode('UTF-8'))