import os
import csv
from jamonyqueso import jamonyqueso, Constructorjamonyqueso
from cuatroquesos import cuatroQuesos, ConstructorcuatroQuesos
from director import Director
from personalizada import Personalizada, ConstructorPersonalizada
from pizzeria import Pizzeria
from barbacoa import Barbacoa, ConstructorBarbacoa
from usuario import UsuarioBuilder, UsuarioDirector


class Menu(Pizzeria):

    def buscar_pedidos_usuario(nombre):
        pedidos = []
        with open('pedidos.csv', 'r') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                if row['nombre'] == nombre:
                    pedidos.append(row)
        return pedidos
    def reconstruir_pizza(pedido):
        pizza = {
            'tipo': pedido['Tipo de Pizza'],
            'masa': pedido['Masa'],
            'coccion': pedido['Cocción'],
            'presentacion': pedido['Presentación'],
            'maridaje': pedido['Maridaje'],
            'extras': pedido['Extras'].split(', '),
            'ingredientes': pedido.get('Ingredientes', '').split(', '),
            'salsa': pedido.get('Salsa', '')
        }
        return pizza
    def visualizar_pizza(pizza):
        print(f"Tipo de Pizza: {pizza['tipo']}")
        print(f"Masa: {pizza['masa']}")
        print(f"Cocción: {pizza['coccion']}")
        print(f"Presentación: {pizza['presentacion']}")
        print(f"Maridaje: {pizza['maridaje']}")
        print(f"Extras: {', '.join(pizza['extras'])}")
        if pizza['ingredientes']:
            print(f"Ingredientes: {', '.join(pizza['ingredientes'])}")
        if pizza['salsa']:
            print(f"Salsa: {pizza['salsa']}")
        print("\n")
    
    def editar_pizza(pizza):
        print("¿Qué te gustaría editar?")
        print("1. Tipo de masa")
        print("2. Tipo de cocción")
        print("3. Tipo de presentación")
        print("4. Tipo de maridaje")
        print("5. Extras")

        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            nueva_masa = input("Introduce el nuevo tipo de masa (gruesa/fina): ")
            pizza['masa'] = nueva_masa
        elif opcion == "2": 
            nueva_coccion = input("Introduce el nuevo tipo de cocción (horno/microondas): ")
            pizza['coccion'] = nueva_coccion
        elif opcion == "3":
            nueva_presentacion = input("Introduce el nuevo tipo de presentación (caja/plato): ")
            pizza['presentacion'] = nueva_presentacion
        elif opcion == "4":
            nuevo_maridaje = input("Introduce el nuevo tipo de maridaje (vino tinto/cerveza): ")
            pizza['maridaje'] = nuevo_maridaje
        elif opcion == "5":
            print("Extras:")
            print("1. Cebolla caramelizada")
            print("2. Queso extra")
            print("3. Borde relleno de queso")
            print("4. Aceitunas")
            print("5. Sin extras")
            nueva_lista_extras = []
            opcion_extras = None
            while opcion_extras != "0":
                opcion_extras = input("Elija una opción o presione 0 para finalizar: ")
                if opcion_extras == "1":
                    nueva_lista_extras.append("Cebolla caramelizada")
                elif opcion_extras == "2":
                    nueva_lista_extras.append("Queso extra")
                elif opcion_extras == "3":
                    nueva_lista_extras.append("Borde relleno de queso")
                elif opcion_extras == "4":
                    nueva_lista_extras.append("Aceitunas")
                elif opcion_extras == "5":
                    nueva_lista_extras.append("Sin extras")
                elif opcion_extras == "0":
                    print("Finalizando selección de extras.")
                else:
                    print("Opción no válida. Por favor, intente de nuevo.")
            pizza['extras'] = nueva_lista_extras
        return pizza

    def guardar_pizza(pizza, nombre):
        archivo_pedidos = 'pedidos.csv'
        archivo_existe = os.path.isfile(archivo_pedidos) and os.path.getsize(archivo_pedidos) > 0

        with open(archivo_pedidos, 'a', newline="") as file:
            writer = csv.writer(file, delimiter=';')
    
            if not archivo_existe:
                writer.writerow(['Usuario','Tipo de Pizza', 'Masa', 'Cocción', 'Presentación', 'Maridaje', 'Extras', 'Ingredientes', 'Salsa'])
            detalles = [nombre, pizza['tipo'], pizza['masa'], pizza['coccion'], pizza['presentacion'], pizza['maridaje']]
            detalles.extend([', '.join(pizza['extras'])])
            if pizza['ingredientes']:
                detalles.append(', '.join(pizza['ingredientes']))
            if pizza['salsa']:
                detalles.append(pizza['salsa'])
            writer.writerow(detalles)

    def Menu(buscar_pedidos_usuario, reconstruir_pizza, visualizar_pizza):
        
        print("Bienvenido a la pizzeria")
        builder = UsuarioBuilder()
        director = UsuarioDirector(builder)
        print("Introduce el nombre del usuario: ")
        nombre = input()
        print("Introduce el apellido del usuario: ")
        apellido = input()
        print("Introduce el email del usuario: ")
        email = input()
        print("Introduce el telefono del usuario: ")
        telefono = input()
        director.crear_usuario(nombre, apellido, email, telefono)
        usuario = director.get_usuario()
        print(usuario)
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

                archivo_pedidos = 'pedidos.csv'
                archivo_existe = os.path.isfile(archivo_pedidos) and os.path.getsize(archivo_pedidos) > 0

                with open(archivo_pedidos, 'a', newline="") as file:
                            writer = csv.writer(file, delimiter=';')
                    
                            if not archivo_existe:
                                writer.writerow(['nombre','apellido','email','telefono','Tipo de Pizza', 'Masa', 'Cocción', 'Presentación', 'Maridaje', 'Extras', 'Ingredientes', 'Salsa'])
                            detalles = [nombre, pizza_seleccionada[0], masa_seleccionada, coccion_seleccionada, presentacion_seleccionada, maridaje_seleccionado]
                            detalles.extend([', '.join(extras_seleccionados)])
                            if pizza_seleccionada == ["Personalizada"]:
                                detalles.append(', '.join(ingredientes_seleccionados))
                                detalles.append(salsa_seleccionada)
                            elif pizza_seleccionada == ["Barbacoa"]:
                                detalles.extend(['Ingredientes: carne, queso, bacon, cebolla, salsa barbacoa ', 'Salsa de barbacoa'])
                            elif pizza_seleccionada == ["Cuatro quesos"]:
                                detalles.extend(['Ingredientes: Mozzarella, Cheddar, Parmesano, Gorgonzola', 'Salsa de tomate'])
                            elif pizza_seleccionada == ["Jamón y Queso"]:
                                detalles.extend(['Ingredientes: Jamón, queso', 'Salsa de tomate'])
                            else:
                                print("Opción no válida")
                            writer.writerow(detalles)

        else:
            print("Opción no válida")
                
        print('Has elegido', pizza_seleccionada)
        print("¿Quieres ver tus pedidos anteriores? (s/n)")
        if input().lower() == 's':
            print("Introduce tu nombre:")
            nombre = input()
            pedidos_usuario = buscar_pedidos_usuario(nombre)
            if pedidos_usuario:
                for idx, pedido in enumerate(pedidos_usuario):
                    pizza = reconstruir_pizza(pedido)
                    print(f"Pedido {idx+1}:")
                    visualizar_pizza(pizza)
            
        else:
            print("No se encontraron pedidos anteriores.")
Menu.Menu('', '', '')

