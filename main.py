import os 

# Crea la estructura de carpetas básica para un nuevo proyecto.
# Recibe el nombre del proyecto y genera las subcarpetas 'src', 'docs' y 'assets' dentro de él.
# Devuelve True si todas las carpetas se crearon correctamente, o False si hubo algún error.
def inicializar_carpetas(nombre_proyecto):  
    carpetas = ['src', 'docs', 'assets']
    try:
        for carpeta in carpetas: 
            ruta = os.path.join(nombre_proyecto, carpeta)  # Arma la ruta completa de cada subcarpeta
            os.makedirs(ruta)  # Crea la carpeta en el sistema de archivos
            print(ruta) 
        return True 
        
    except:
            return False

resultado = inicializar_carpetas('C:/Users/ulica/OneDrive/Desktop')

lista_tarea = []


    
