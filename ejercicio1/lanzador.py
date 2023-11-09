from __future__ import annotations
from abc import ABC, abstractmethod
import pandas as pd
from statistics import mode
from AbstractFactory import *

if __name__ == "__main__":
    archivo = 'ejercicio1/activaciones_samur_2023.csv'
    data = pd.read_csv(archivo, sep=';', encoding='ISO-8859-1')    
    meses = {
        'ENERO': 1, 'FEBRERO': 2, 'MARZO': 3, 'ABRIL': 4, 'MAYO':5, 'JUNIO':6, 'JULIO':7,
        'AGOSTO':8, 'SEPTIEMBRE':9, 'OCTUBRE':10, 'NOVIEMBRE':11, 'DICIEMBRE':12
    }
    
    data['Mes'] = data['Mes'].map(meses)


    
#ahora convertimos el resto de datos en minutos

    data['Hora Solicitud'] = data['Hora Solicitud'].dt.hour*60 + data['Hora Solicitud'].dt.minute
    data['Hora Intervención'] = data['Hora Intervención'].dt.hour*60 + data['Hora Intervención'].dt.minute

    
    print('Hora Solicitud')
    factory_horasolicitud = ConcreteFactory_horasolicitud(data)
    client_code_media(factory_horasolicitud)
    client_code_moda(factory_horasolicitud)
    
    print('Hora Intervención')
    factory_horaintervencion = ConcreteFactory_horaintervencion(data)
    client_code_media(factory_horaintervencion)
    client_code_moda(factory_horaintervencion)
    
    print("Mes")
    factory_mes = ConcreteFactory_mes(data)
    client_code_media(factory_mes)
    client_code_moda(factory_mes)