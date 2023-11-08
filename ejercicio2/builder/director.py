from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, List
from personalizada import Personalizada, ConstructorPersonalizada
from pizzeria import Pizzeria
from barbacoa import Barbacoa, ConstructorBarbacoa

class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Pizzeria:
        return self._builder

    @builder.setter
    def builder(self, builder: Pizzeria) -> None:
        self._builder = builder

    def build_personalizada(self, masa: str, salsa: str, ingredientes: List[str], coccion: str, presentacion: str, maridaje: str, extras: List[str]) -> None:
        self.builder.masa(masa)
        self.builder.salsa_base(salsa)
        self.builder.ingredientes(ingredientes)
        self.builder.coccion(coccion)
        self.builder.presentacion(presentacion)
        self.builder.maridaje(maridaje)
        self.builder.extras(extras)


if __name__ == "__main__":
    director = Director()
    builder = ConstructorPersonalizada()
    director.builder = builder

    print("Elija el tipo de masa:")
    print("1. Masa gruesa")
    print("2. Masa fina")
    masa_opcion = input("Elija una opción: ")
    masa_seleccionada = "gruesa" if masa_opcion == "1" else "fina"

    print("\nElija el tipo de salsa:")
    print("1. Salsa de tomate")
    print("2. Salsa BBQ")
    salsa_opcion = input("Elija una opción: ")
    salsa_seleccionada = "tomate" if salsa_opcion == "1" else "BBQ"

    print("\nElija los ingredientes:")
    print("1. Jamón y queso")
    print("2. Atún y cebolla")
    print("3. Pollo y Cebolla crujiente")
    ingredientes_opcion = input("Elija una opción: ")
    ingredientes_seleccionados = []

    if ingredientes_opcion == "1":
        ingredientes_seleccionados = ["Jamón", "Queso"]
    elif ingredientes_opcion == "2":
        ingredientes_seleccionados = ["Atún", "Cebolla"]
    elif ingredientes_opcion == "3":
        ingredientes_seleccionados = ["Pollo", "Cebolla crujiente"]
    else:
        print("Opción no válida")
    
    print("\nElija el tipo de cocción:")
    print("1. Horno")
    print("2. Microondas")
    coccion_opcion = input("Elija una opción: ")
    coccion_seleccionada = "horno" if coccion_opcion == "1" else "microondas"

    print("\nElija el tipo de presentación:")
    print("1. Caja")
    print("2. Plato")
    presentacion_opcion = input("Elija una opción: ")
    presentacion_seleccionada = "caja" if presentacion_opcion == "1" else "plato"

    print("\nElija el tipo de maridaje:")
    print("1. Vino tinto")
    print("2. Cerveza")
    maridaje_opcion = input("Elija una opción: ")
    maridaje_seleccionado = "vino tinto" if maridaje_opcion == "1" else "cerveza"
    
    print("\nElija los extras:")
    print("1. Aceitunas")
    print("2. Queso extra")
    extras_opcion = input("Elija una opción: ")
    extras_seleccionados = []

    if extras_opcion == "1":
        extras_seleccionados = ["Aceitunas"]
    elif extras_opcion == "2":  
        extras_seleccionados = ["Queso extra"]
    else:
        print("Opción no válida")

    director.build_personalizada(masa_seleccionada, salsa_seleccionada, ingredientes_seleccionados, coccion_seleccionada, presentacion_seleccionada, maridaje_seleccionado, extras_seleccionados)
    builder.product.list_parts()
    print("\n")

    
    


