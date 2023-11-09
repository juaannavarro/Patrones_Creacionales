from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, List
from pizzeria import Pizzeria
from menu import Menu
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
    builder = Menu()
    director.builder = builder
    director.build_personalizada("gruesa", "tomate", ["Jamón", "Queso"], "horno", "caja", "vino tinto", [])
    builder.product.list_parts()
    print("\n")
    director.build_personalizada("gruesa", "tomate", ["Jamón", "Queso"], "horno", "caja", "vino tinto", [])
    builder.product.list_parts()
    print("\n")
    director.build_personalizada("gruesa", "tomate", ["Jamón", "Queso"], "horno", "caja", "vino tinto", [])
    builder.product.list_parts()
    print("\n")
    director.build_personalizada("gruesa", "tomate", ["Jamón", "Queso"], "horno", "caja", "vino tinto", [])
    builder.product.list_parts()
    print("\n")
    director.build_personalizada("gruesa", "tomate", ["Jamón", "Queso"], "horno", "caja", "vino tinto", [])
    builder.product.list_parts()
    print("\n")
    director.build_personalizada("gruesa", "tomate", ["Jamón", "Queso"], "horno", "caja", "vino tinto", [])
    builder.product.list_parts()
    print("\n")
    director.build_personalizada("gruesa", "tomate", ["Jamón", "Queso"], "horno", "caja", "vino tinto", [])
    builder.product.list

    
    




    
    

