from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any
from builder.pizza import Pizza
class ConstructorJamonyQueso(Pizza):
    """
    The Concrete Builder classes follow the Builder interface and provide
    specific implementations of the building steps. Your program may have
    several variations of Builders, implemented differently.
    """

    def __init__(self) -> None:
        """
        A fresh builder instance should contain a blank product object, which is
        used in further assembly.
        """
        self.reset()

    def reset(self) -> None:
        self._product = JamonyQueso()

    @property
    def product(self) -> JamonyQueso:
        """
        Concrete Builders are supposed to provide their own methods for
        retrieving results. That's because various types of builders may create
        entirely different products that don't follow the same interface.
        Therefore, such methods cannot be declared in the base Builder interface
        (at least in a statically typed programming language).

        Usually, after returning the end result to the client, a builder
        instance is expected to be ready to start producing another product.
        That's why it's a usual practice to call the reset method at the end of
        the `getProduct` method body. However, this behavior is not mandatory,
        and you can make your builders wait for an explicit reset call from the
        client code before disposing of the previous result.
        """
        product = self._product
        self.reset()
        return product

    def pizza(self) -> None:
        return self._product

    def masa(self) -> None:
        self._product.add("Masa")

    def salsa_base(self) -> None:
        self._product.add("Salsa de tomate")
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




class JamonyQueso():
    """
    It makes sense to use the Builder pattern only when your products are quite
    complex and require extensive configuration.

    Unlike in other creational patterns, different concrete builders can produce
    unrelated products. In other words, results of various builders may not
    always follow the same interface.
    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"La pizza lleva: {', '.join(self.parts)}", end="")

