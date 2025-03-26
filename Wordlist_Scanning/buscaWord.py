import requests

def scan_url(target_url, word):    
    #URL de prueba
    full_url = f"{target_url.rstrip('/')}/{word}"
    
    try:
        response = requests.get(full_url, timeout=5)
        
        #Si la respuesta es 200, el recurso existe
        if response.status_code == 200:
            print(f"Encontrado: {full_url} (Código {response.status_code})")
        elif response.status_code == 403:
            print(f"Acceso denegado: {full_url} (Código {response.status_code})")
        elif response.status_code == 404:
            print(f"No encontrado: {full_url} (Código {response.status_code})")
        else:
            print(f"Estado desconocido: {full_url} (Código {response.status_code})")
    
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con {full_url}: {e}")

def read_wordlist(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return words


TARGET_URL = "http://localhost:8000/Ejercicio_Wordlist_Scanning/victima.html"
WORDLIST_FILE = "c:/Users/esper/OneDrive/Documentos/CODE/Python/Ejercicio_Wordlist_Scanning/wordlist.txt" 

#Leer la lista
words_to_search = read_wordlist(WORDLIST_FILE)

#Escaneo
print(f"Escaneando {TARGET_URL} con la lista de palabras de {WORDLIST_FILE}...\n")
for word in words_to_search:
    if word.strip():  
        scan_url(TARGET_URL, word)
    else:
        print("Hay un espacio, omitiendo...")


'''El Wordlist Scanning es una técnica de fuerza bruta dirigida, donde se
utiliza un archivo de texto (wordlist) con una lista de palabras clave para 
probar combinaciones en un sistema, servicio o aplicación. 
Se emplea para descubrir rutas, subdominios, credenciales, archivos ocultos y más.
El siguiente programa busca una palabra en un servidor web.'''

'''Modifica el programa para poder leer una lista de palabras desde un archivo y probar si 
se encuentran en un servidor web.'''