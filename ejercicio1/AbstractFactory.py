from __future__ import annotations
from abc import ABC, abstractmethod
import pandas as pd
from statistics import mode

class AbstractFactory(ABC):

    @abstractmethod
    def media(self) -> AbstractMedia:
        pass

    @abstractmethod
    def moda(self) -> AbstractModa:
        pass
class ConcreteFactory_horasolicitud(AbstractFactory):
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def media(self) -> AbstractMedia:
        return ConcreteMedia_horasolicitud(self.data)

    def moda(self) -> AbstractModa:
        return ConcreteModa_horasolicitud(self.data)
    
class ConcreteFactory_horaintervencion(AbstractFactory):
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def media(self) -> AbstractMedia:
        return ConcreteMedia_horaintervencion(self.data)

    def moda(self) -> AbstractModa:
        return ConcreteModa_horaintervencion(self.data)
    
class ConcreteFactory_mes(AbstractFactory):
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def media(self) -> AbstractMedia:
        return ConcreteMedia_mes(self.data)

    def moda(self) -> AbstractModa:
        return ConcreteModa_mes(self.data)

class AbstractMedia(ABC):
    @abstractmethod
    def useful_function_a(self) -> pd.Series:
        pass

class ConcreteMedia_horasolicitud(AbstractMedia):
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def useful_function_a(self) -> float:
        # Asumimos que 'horasolicitud' es una columna en tu DataFrame y queremos la media
        return self.data['Hora Solicitud'].mean()


class ConcreteMedia_horaintervencion(AbstractMedia):
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def useful_function_a(self) -> float:
        # Asumimos que 'horaintervencion' es una columna en tu DataFrame y queremos la media
        return self.data['Hora Intervención'].mean()


class ConcreteMedia_mes(AbstractMedia):
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def useful_function_a(self) -> float:
        # Asumimos que 'mes' es una columna en tu DataFrame y queremos la media
        return self.data['Mes'].mean()

class AbstractModa(ABC):

    @abstractmethod
    def useful_function_b(self) -> pd.Series:
        pass


class ConcreteModa_horasolicitud(AbstractModa):
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def useful_function_b(self) -> int:
        # Asumimos que 'Hora Solicitud' es una columna en tu DataFrame y queremos la moda
        return self.data['Hora Solicitud'].mode().iloc[0]

# ...

class ConcreteModa_horaintervencion(AbstractModa):
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def useful_function_b(self) -> int:
        # Asumimos que 'horaintervencion' es una columna en tu DataFrame y queremos la moda
        return (self.data['Hora Intervención']).mode().iloc[0]

# ...

class ConcreteModa_mes(AbstractModa):
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def useful_function_b(self) -> int:
        # Asumimos que 'mes' es una columna en tu DataFrame y queremos la moda
        return (self.data['Mes']).mode().iloc[0]

def client_code_media(factory: AbstractFactory) -> None:
        media_product = factory.media()
        print(f"Media: {media_product.useful_function_a()}")

def client_code_moda(factory: AbstractFactory) -> None:
        moda_product = factory.moda()
        print(f"Moda: {moda_product.useful_function_b()}")




    

    
    