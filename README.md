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
                            
                    writer.writerow(detalles)# Patrones_Creacionales