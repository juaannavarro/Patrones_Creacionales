

from jamonyqueso import jamonyqueso, Constructorjamonyqueso
from cuatroquesos import cuatroQuesos, ConstructorcuatroQuesos
from director import Director
from personalizada import Personalizada, ConstructorPersonalizada
from pizzeria import Pizzeria
from barbacoa import Barbacoa, ConstructorBarbacoa

#creame una funcion que ejecute el menu y haga elegir entre las pizzas
class Menu(Pizzeria):
    def Menu():
        
        print("Bienvenido a la pizzeria")
        print("Elija el tipo de pizza:")
        print("1. Jamón y queso")
        print("2. Cuatro quesos")
        print("3. Barbacoa")
        print("4. Personalizada")
        pizza_opcion = input("Elija una opción: ")
        pizza_seleccionada = []

        if pizza_opcion == "1":
            pizza_seleccionada = ["Jamón y Queso"]
            director = Director()
            builder = Constructorjamonyqueso()
            director.builder = builder
            
            print("\nElija el tipo de masa:")
            print("1. Masa gruesa")
            print("2. Masa fina")
            masa_opcion = input("Elija una opción: ")
            masa_seleccionada = "gruesa" if masa_opcion == "1" else "fina"

            print("\nElija el tipo de coccion:")
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
            print("3. Sin extras")
            extras_opcion = input("Elija una opción: ")
            extras_seleccionados = []
        
            if extras_opcion == "1":
                extras_seleccionados = ["Aceitunas"]
            elif extras_opcion == "2":
                extras_seleccionados = ["Queso extra"]
            elif extras_opcion == "3":
                extras_seleccionados = ["Sin extras"]
            else:
                print("Opción no válida")
                
            director.build_jamonyqueso(masa_seleccionada, coccion_seleccionada, presentacion_seleccionada, maridaje_seleccionado, extras_seleccionados)
            builder.product.list_parts()
            print("\n")
        elif pizza_opcion == "2":
            pizza_seleccionada = ["Cuatro quesos"]
            director = Director()
            builder = ConstructorcuatroQuesos()
            director.builder = builder
        
            print("\nElija el tipo de masa:")
            print("1. Masa gruesa")
            print("2. Masa fina")
            masa_opcion = input("Elija una opción: ")
            masa_seleccionada = "gruesa" if masa_opcion == "1" else "fina"
        
            print("\nElija el tipo de coccion:")
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
            print("2. Prosciutto")
            print("3. Sin extras")
            extras_opcion = input("Elija una opción: ")
            extras_seleccionados = []
        
            if extras_opcion == "1":
                extras_seleccionados = ["Aceitunas"]
            elif extras_opcion == "2":
                extras_seleccionados = ["Prosciutto"]
            elif extras_opcion == "3": 
                extras_seleccionados = ["Sin extras"]
            else:
                print("Opción no válida")
            
            director.build_cuatroQuesos(masa_seleccionada, coccion_seleccionada, presentacion_seleccionada, maridaje_seleccionado, extras_seleccionados)
            builder.product.list_parts()
            print("\n")
        elif pizza_opcion == "3":
            pizza_seleccionada = ["Barbacoa"]
            director = Director()
            builder = ConstructorBarbacoa()
            director.builder = builder
        
            print("\nElija el tipo de masa:")
            print("1. Masa gruesa")
            print("2. Masa fina")
            masa_opcion = input("Elija una opción: ")
            masa_seleccionada = "gruesa" if masa_opcion == "1" else "fina"
        
            print("\nElija el tipo de coccion:")
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
            print("1. Borde rellenos de queso")
            print("2. Maíz")
            print("3. Sin extras")
            extras_opcion = input("Elija una opción: ")
            extras_seleccionados = []
        
            if extras_opcion == "1":
                extras_seleccionados = ["Borde rellenos de queso"]
            elif extras_opcion == "2":
                extras_seleccionados = ["Maíz"]
            elif extras_opcion == "3":
                extras_seleccionados = ["Sin extras"]
            else:
                print("Opción no válida")
            
            director.build_barbacoa(masa_seleccionada, coccion_seleccionada, presentacion_seleccionada, maridaje_seleccionado, extras_seleccionados)
            builder.product.list_parts()
            print("\n")
        elif pizza_opcion == "4":
                pizza_seleccionada = ["Personalizada"]
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
                print("1. Jamón")
                print("2. Queso")
                print("3. Champiñones")
                print("4. Cebolla")
                print("5. Pimiento")
                print("6. Tomate")
                print("7. Piña")
                print("8. Pollo")
                print("9. Carne picada")
                print("10. Bacon")
                ingredientes_opcion = None
                ingredientes_seleccionados = []
                while ingredientes_opcion != "0":
                    ingredientes_opcion = input("Elija una opción o presione 0 para finalizar: ")
                    if ingredientes_opcion == "1":
                        ingredientes_seleccionados.append("Jamón")
                    elif ingredientes_opcion == "2":
                        ingredientes_seleccionados.append("Queso")
                    elif ingredientes_opcion == "3":
                        ingredientes_seleccionados.append("Champiñones")
                    elif ingredientes_opcion == "4":
                        ingredientes_seleccionados.append("Cebolla")
                    elif ingredientes_opcion == "5":
                        ingredientes_seleccionados.append("Pimiento")
                    elif ingredientes_opcion == "6":
                        ingredientes_seleccionados.append("Tomate")
                    elif ingredientes_opcion == "7":
                        ingredientes_seleccionados.append("Piña")
                    elif ingredientes_opcion == "8":
                        ingredientes_seleccionados.append("Pollo")
                    elif ingredientes_opcion == "9":
                        ingredientes_seleccionados.append("Carne picada")
                    elif ingredientes_opcion == "10":
                        ingredientes_seleccionados.append("Bacon")
                    elif ingredientes_opcion == "0":
                        print("Finalizando selección de ingredientes.")
                    else:
                        print("Opción no válida. Por favor, intente de nuevo.")
                        
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
                print("1. Cebolla caramelizada")
                print("2. Queso extra")
                print("3. Borde relleno de queso")
                print("4. Aceitunas")
                print("5. Sin extras")
                extras_opcion = input("Elija una opción: ")
                extras_seleccionados = []

                if extras_opcion == "1":
                    extras_seleccionados = ["Cebolla caramelizada"]
                elif extras_opcion == "2":  
                    extras_seleccionados = ["Queso extra"]
                elif extras_opcion == "3":
                    extras_seleccionados = ["Borde relleno de queso"]
                elif extras_opcion == "4":
                    extras_seleccionados = ["Aceitunas"]
                elif extras_opcion == "5":
                    extras_seleccionados = ["Sin extras"]
                else:
                    print("Opción no válida")
                director.build_personalizada(masa_seleccionada, salsa_seleccionada, ingredientes_seleccionados, coccion_seleccionada, presentacion_seleccionada, maridaje_seleccionado, extras_seleccionados)
                builder.product.list_parts()
                print("\n")

        else:
            print("Opción no válida")
            
        print('Has elegido', pizza_seleccionada)


Menu.Menu()