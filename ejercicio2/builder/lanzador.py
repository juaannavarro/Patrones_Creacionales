from pizzeria import Pizzeria
from director import Director
from menu import Menu

if __name__ == '__main__':
    
#ejecutar el programa

    director = Director()
    builder = Pizzeria()
    director.builder = builder
    menu = Menu()
