import requests

def obtener_coordenadas(ciudad, api_key):
    """Obtener las coordenadas (lat, lon) de una ciudad usando la API de Graphhopper Geocoding"""
    url = f"https://graphhopper.com/api/1/geocode?q={ciudad}&limit=1&key={api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if not data.get('hits'):
            print(f"No se encontraron resultados para la ciudad: {ciudad}")
            return None
            
        location = data['hits'][0]['point']
        return location['lat'], location['lng']
    
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API de Graphhopper: {e}")
        return None

def obtener_medios_transporte():
    """Desplegar los medios de transporte soportados por Graphhopper"""
    return {
        '1': {'codigo': 'car', 'nombre': 'Automóvil'},
        '2': {'codigo': 'bike', 'nombre': 'Bicicleta'},
        '3': {'codigo': 'foot', 'nombre': 'A pie'},
        '4': {'codigo': 'hike', 'nombre': 'Senderismo'},
        '5': {'codigo': 'mtb', 'nombre': 'Bicicleta de montaña'},
        '6': {'codigo': 'racingbike', 'nombre': 'Bicicleta de carreras'},
        '7': {'codigo': 'scooter', 'nombre': 'Scooter'},
        '8': {'codigo': 'truck', 'nombre': 'Camión'}
    }

def mostrar_medios_transporte(transportes):
    """Desplegar los medios de transporte disponibles"""
    print("\nMedios de transporte disponibles:")
    for codigo, transporte in transportes.items():
        print(f"{codigo}. {transporte['nombre']}")

def calcular_ruta(origen, destino, api_key, vehiculo):
    """Calcula la ruta entre dos ubicaciones usando la API de Graphhopper"""
    url = f"https://graphhopper.com/api/1/route?point={origen[0]}%2C{origen[1]}&point={destino[0]}%2C{destino[1]}&vehicle={vehiculo}&key={api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if 'paths' not in data or not data['paths']:
            print("No se pudo calcular la ruta.")
            return None
            
        tiempo_ms = data['paths'][0]['time']
        distancia = data['paths'][0]['distance']
        
        return {
            'tiempo_segundos': tiempo_ms // 1000,
            'distancia_metros': distancia
        }
    
    except requests.exceptions.RequestException as e:
        print(f"Error al calcular la ruta: {e}")
        return None

def formatear_tiempo(segundos):
    """Convertir segundos a horas, minutos y segundos"""
    horas = segundos // 3600
    segundos_restantes = segundos % 3600
    minutos = segundos_restantes // 60
    segundos = segundos_restantes % 60
    return horas, minutos, segundos

def convertir_distancia(metros):
    """Convertir metros a kilómetros y millas"""
    kilometros = metros / 1000
    millas = metros * 0.000621371
    return kilometros, millas

def main():
    # API Key de Graphopper
    API_KEY = "190cf078-b8d4-495f-a430-bc8d97d835a6"
    
    print("Calculadora de rutas usando Graphhopper")
    print("Presiona 's' para salir en cualquier momento\n")
    
    transportes = obtener_medios_transporte()
    
    while True:
        # Solicitar ciudad de origen
        ciudad_origen = input("Ingresa la ciudad de origen: ")
        if ciudad_origen.lower() == 's':
            break
            
        # Solicitar ciudad de destino
        ciudad_destino = input("Ingresa la ciudad de destino: ")
        if ciudad_destino.lower() == 's':
            break
            
        # Mostrar y seleccionar medio de transporte
        mostrar_medios_transporte(transportes)
        while True:
            opcion = input("\nSelecciona el medio de transporte (número): ")
            if opcion.lower() == 's':
                break
            if opcion in transportes:
                vehiculo = transportes[opcion]['codigo']
                nombre_vehiculo = transportes[opcion]['nombre']
                break
            print("Opción no válida. Intenta nuevamente.")
        
        if opcion.lower() == 's':
            break
            
        print(f"\nCalculando ruta en {nombre_vehiculo.lower()}...")
        
        # Obtener coordenadas
        coords_origen = obtener_coordenadas(ciudad_origen, API_KEY)
        if not coords_origen:
            continue
            
        coords_destino = obtener_coordenadas(ciudad_destino, API_KEY)
        if not coords_destino:
            continue
            
        # Calcular ruta
        resultado = calcular_ruta(coords_origen, coords_destino, API_KEY, vehiculo)
        if resultado is None:
            continue
            
        # Formatear y mostrar resultados
        horas, minutos, segundos = formatear_tiempo(resultado['tiempo_segundos'])
        km, millas = convertir_distancia(resultado['distancia_metros'])
        
        print("\n" + "="*50)
        print(f"RESULTADO DEL VIAJE ({nombre_vehiculo})")
        print(f"De: {ciudad_origen} a {ciudad_destino}")
        print("-"*50)
        print(f"Tiempo estimado: {horas} horas, {minutos} minutos y {segundos} segundos")
        print(f"Distancia: {km:.2f} km ({millas:.2f} millas)")
        print("="*50 + "\n")
    
    print("\nPrograma finalizado.")

if __name__ == "__main__":
    main()
