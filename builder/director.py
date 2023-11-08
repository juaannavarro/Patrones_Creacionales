from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any
from builder.pizza import Pizza
from builder.Jamon_y_Queso import JamonyQueso, ConstructorJamonyQueso
class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Pizza:
        return self._builder

    @builder.setter
    def builder(self, builder: Pizza) -> None:

        self._builder = builder



    def build (self) -> None:
        self.builder.masa()
        self.builder.salsa_base()
        self.builder.ingredientes()
        self.builder.coccion()
        self.builder.presentacion()
        self.builder.maridaje()
        self.builder.extras()


if __name__ == "__main__":


    director = Director()
    builder = ConstructorJamonyQueso()
    director.builder = builder

    director.build()
    builder.product.list_parts()



