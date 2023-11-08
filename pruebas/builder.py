from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class Pizzeria(ABC):
    @property
    @abstractmethod
    def pizza(self) -> None:
        pass
    @abstractmethod
    def masa(self) -> None:
        pass
    @abstractmethod
    def salsa_base(self) -> None:
        pass

    @abstractmethod
    def ingredientes(self) -> None:
        pass

    @abstractmethod
    def coccion(self) -> None:
        pass
    @abstractmethod
    def presentacion(self) -> None:
        pass
    @abstractmethod
    def maridaje(self) -> None:
        pass
    @abstractmethod
    def extras(self) -> None:
        pass

class ConstructorPersonalizada(Pizzeria):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Personalizada()

    @property
    def product(self) -> Personalizada:
        product = self._product
        self.reset()
        return product

    def pizza(self) -> None:
        return self._product

    def masa(self, tipo: str) -> None:
        self._product.add(f"Masa {tipo}")

    def salsa_base(self, tipo: str) -> None:
        self._product.add(f"Salsa de {tipo}")
    def ingredientes(self) -> None:
        self._product.add("Jamón y queso")
    def coccion(self) -> None:
        self._product.add("Horno")
    def presentacion(self) -> None:
        self._product.add("Caja")
    def maridaje(self) -> None:
        self._product.add("Vino tinto")
    def extras(self) -> None:
        self._product.add("Aceitunas")




class Personalizada():
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Personalizada: {', '.join(self.parts)}", end="")


class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Pizzeria:
        return self._builder

    @builder.setter
    def builder(self, builder: Pizzeria) -> None:
        self._builder = builder

    def build_personalizada (self, masa: str, salsa_base : str) -> None:
        self.builder.masa(masa)
        self.builder.salsa_base(salsa_base)
        self.builder.ingredientes()
        self.builder.coccion()
        self.builder.presentacion()
        self.builder.maridaje()
        self.builder.extras()


if __name__ == "__main__":
    director = Director()
    builder = ConstructorPersonalizada()
    director.builder = builder

    #creame un pequeño menu para que el usuario elija el tipo de masa
    print("Bienvenido a la pizzeria")
    print("Elija el tipo de masa")
    print("1. Masa gruesa")
    print("2. Masa fina")
    masa_cliente = input("Elija una opcion: ")
    if masa_cliente == "1":
        director.build_personalizada("Masa gruesa", '')
    elif masa_cliente == "2":
        director.build_personalizada("Masa fina", '')       
    else:
        print("Opcion no valida")

        print("Elija el tipo de salsa")
    print("1. Salsa de tomate")
    print("2. Salsa de barbacoa")
    salsa_cliente = input("Elija una opcion: ")
    if salsa_cliente == "1":
        director.build_personalizada('', "tomate")      
    elif salsa_cliente == "2":
        director.build_personalizada('', "barbacoa")
    else:
        print("Opcion no valida")
    
    director.build_personalizada(masa_cliente, salsa_cliente)
    builder.product.list_parts()
    print("\n")
    
    


