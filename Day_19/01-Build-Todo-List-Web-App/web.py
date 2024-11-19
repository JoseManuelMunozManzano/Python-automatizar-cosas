import streamlit as st
import functions

todos = functions.get_todos()

# Configuración de la página
# st.set_page_config(layout="wide")

# Si necesitamos más de una página, se crea la carpeta pages y ahí se crean los
# distintos fuentes Python que constituyen cada una de las páginas de la webapp.
# En el navegador se genera, a la izquierda, una barra de navegación para moverse
# por las distintas páginas

# Los handlers de los listeners se crean arriba del todo (debajo de variables globales)
# session_state es como un diccionario. En concreto es un tipo Estado de Sesión.
# Contiene pares de valores que el usuario introduce en la app, formada por la key indicada
# en el programa, y su value, informada en la app.
def add_todo():
    todo = st.session_state["new_todo"].title() + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


def complete_todo(todo, index):
    todos.pop(index)
    functions.write_todos(todos)
    del st.session_state[todo]
    # Queremos volver a ejecutar desde el principio para que vuelva a cargar los todos
    st.rerun()
    

# El orden en que se indican los elementos es el mismo que el que luego
# se ve en el navegador.
# Cada vez que se ejecuta el código (o al refrescar la página, o al pulsar Intro)
# se ejecutan todas las líneas del script, de arriba a abajo.
st.title("My Todo App")
st.subheader("This is my todo app.")
# Se puede indicar código HTML de la siguiente forma:
st.write("This app is going to increase your <b>productivity</b>.",
         unsafe_allow_html=True)

for index, todo in enumerate(todos):
    # checkbox vale True (esta seleccionado) o False (no está seleccionado)
    checkbox = st.checkbox(todo, key=todo)
    # No hay listener como tal. Solo se pregunta si está seleccionado y vamos al handler.
    if checkbox:
        complete_todo(todo, index)
        

# Conectamos un input con su acción añadiendo listeners como on_change, etc.
# donde indicamos un funcion callback.
# También se indica una key para, haciendo referencia a ella, poder
# identificar este widget y poder recuperar el texto informado.
st.text_input(label="Enter a todo", placeholder="Add new todo and press Intro...",
              on_change=add_todo, key="new_todo")


# Para ver el valor de session_state.
# Suele dejarse mientras se programa, porque sirve para ver el state.
# Luego, cuando se termina la app, esta sentencia se elimina (yo la voy a comentar)

# st.session_state