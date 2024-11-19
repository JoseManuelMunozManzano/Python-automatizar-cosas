# Vemos el módulo webbrowser
# Vamos a recibir un término de búsqueda y vamos a abrir
# el navegador para buscarlo en Google.
import webbrowser

user_term = input("Enter a search term: ").replace(" ", "+")

# La función open() espera una URL como cadena
webbrowser.open(f"https://google.com/search?q={user_term}")