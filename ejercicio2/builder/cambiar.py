import csv
import os.path







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
            
def main():
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