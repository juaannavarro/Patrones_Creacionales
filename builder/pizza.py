from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class Pizza(ABC):
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