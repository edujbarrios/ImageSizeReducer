import os
from PIL import Image

def reduce_image_size(image_path, size_mb=1):
    # Abrir imagen
    image = Image.open(image_path)
    
    # Calcular el tamaño actual de la imagen en MB
    original_size = os.path.getsize(image_path) / (1024 * 1024)
    
    # Calcular la relación de tamaño deseada
    ratio = size_mb / original_size
    
    # Reducir el tamaño de la imagen
    new_size = tuple(map(int, (image.size[0] * ratio, image.size[1] * ratio)))
    image = image.resize(new_size, Image.ANTIALIAS)
    
    # Guardar la imagen con calidad 80
    image.save(image_path, quality=80)

def menu():
    # Mostrar el menú
    print("Menú de Reducción de Tamaño de Imágenes")
    print("1. Reducir tamaño de una imagen")
    print("2. Salir")
    opcion = int(input("Seleccione una opción: "))
    
    # Realizar acción según la opción seleccionada
    if opcion == 1:
        # Obtener la ruta de la imagen
        image_path = input("Ingrese la ruta de la imagen: ")
        
        # Reducir tamaño de la imagen
        reduce_image_size(image_path)
        
        # Mostrar mensaje de éxito
        print("El tamaño de la imagen ha sido reducido con éxito.")
        
        # Volver al menú
        menu()
    elif opcion == 2:
        # Salir del programa
        exit()
    else:
        # Mostrar mensaje de error
        print("Opción inválida, seleccione una opción válida.")
        
        # Volver al menú
        menu()

# Ejecutar el menú
menu()
