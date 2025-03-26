import requests, re
from bs4 import BeautifulSoup, Comment

url = "http://localhost:8000/Ejercicio%20Web%20Scrapping/victima.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

#links = [a["href"] for a in soup.find_all("a", href=True)]
hyperMails = [a["href"][7:] for a in soup.find_all("a", href=True) if a["href"].startswith("mailto:")]
textMails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", soup.get_text())
todos = list(set(hyperMails + textMails))
comments = [comentario for comentario in soup.find_all(string=lambda text: isinstance(text, Comment))]

print("Correos:",hyperMails,textMails,"\nComentarios:",comments)


'''El programa realiza una conexión a un servidor en 127.0.0.1 en el puerto 8000 
y solicita una página llamada víctima.html y extrae los enlaces de dicha página:'''

'''Modifica el programa para que pueda extraer los comentarios que puede haber en una 
página HTML y que extraiga direcciones de correo electrónico. 
Se anexan tres archivos: el archivo victima.html y dos versiones de programas que 
extraen ligas. Puedes poner un servidor web, utilizando python así: python3 -m http.server'''