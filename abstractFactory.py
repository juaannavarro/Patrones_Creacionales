from abc import ABC, abstractmethod
import pandas as pd
import matplotlib.pyplot as plt


# Asumimos que ya tienes la URL del CSV
URL = "https://datos.madrid.es/egob/catalogo/212504-0-emergencias-activaciones.csv"

# Leer los datos del CSV
data = pd.read_csv(URL, sep=';', encoding='ISO-8859-1')

# Transformación de columnas específicas a numéricas
# Supongamos que 'unidades_asignadas' es una columna que debería ser numérica
data['unidades_asignadas'] = pd.to_numeric(data['unidades_asignadas'], errors='coerce')

# Convertir columnas de fecha y hora
data['fecha'] = pd.to_datetime(data['fecha'], errors='coerce')
data['hora'] = pd.to_datetime(data['hora'], errors='coerce').dt.time

# Transformación de columnas específicas a categóricas
# Supongamos que 'tipo_emergencia' es una columna que debería ser categórica
data['tipo_emergencia'] = data['tipo_emergencia'].astype('category')

# Limpieza de datos numéricos: manejar o eliminar valores NaN
data['unidades_asignadas'] = data['unidades_asignadas'].fillna(0)  # Reemplazar NaN por 0
# O podrías querer eliminar esas filas completamente
# data = data.dropna(subset=['unidades_asignadas'])

# Ahora tus datos han sido transformados, con 'unidades_asignadas' como numéricos y 'tipo_emergencia' como categóricos.

# Verificar los tipos de datos para confirmar
print(data.dtypes)

# Realizar alguna operación con los datos numéricos
print("Media de unidades asignadas:", data['unidades_asignadas'].mean())

# Realizar alguna operación con los datos categóricos
print("Moda de tipo de emergencia:", data['tipo_emergencia'].mode()[0])

# Guardar los datos transformados en un nuevo CSV si es necesario
data.to_csv('transformed_data.csv', index=False)




class AbstractAnalysisFactory(ABC):
    
    @abstractmethod
    def create_statistical_analysis(self):
        pass

    @abstractmethod
    def create_visual_representation(self):
        pass


class StatisticalAnalysis:
    def __init__(self, data):
        self.data = data

    def mean(self):
        return self.data.mean()

    def median(self):
        return self.data.median()

    def mode(self):
        return self.data.mode()

class VisualRepresentation:
    def __init__(self, data):
        self.data = data

    def histogram(self, column):
        self.data[column].hist()
        plt.show()

    def bar_chart(self, column):
        self.data[column].value_counts().plot(kind='bar')
        plt.show()

class SAMURStatisticalFactory(AbstractAnalysisFactory):
    def __init__(self, data):
        self.data = data

    def create_statistical_analysis(self):
        return StatisticalAnalysis(self.data)

    def create_visual_representation(self):
        return VisualRepresentation(self.data)


def main():
    URL = "https://datos.madrid.es/egob/catalogo/212504-0-emergencias-activaciones.csv"
    data = pd.read_csv(URL, sep=';', encoding='ISO-8859-1')

    statistical_factory = SAMURStatisticalFactory(data)

    statistical_analysis = statistical_factory.create_statistical_analysis()
    visual_representation = statistical_factory.create_visual_representation()

    print("Media:", statistical_analysis.mean())
    print("Mediana:", statistical_analysis.median())
    print("Moda:", statistical_analysis.mode())

    # Generar algunas visualizaciones
    visual_representation.histogram('unidades_asignadas')
    visual_representation.bar_chart('tipo_emergencia')

if __name__ == "__main__":
    main()
