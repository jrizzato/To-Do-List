# To-Do List App

Esta es una aplicación web simple de lista de tareas pendientes construida con Flask. Permite a los usuarios agregar, editar, marcar como completadas y eliminar tareas.

## Características

- **Agregar Tareas**: Los usuarios pueden agregar nuevas tareas a la lista.
- **Marcar Tareas como Completadas**: Los usuarios pueden marcar las tareas como completadas/descompletadas.
- **Editar Tareas**: Los usuarios pueden editar el contenido de las tareas.
- **Eliminar Tareas**: Los usuarios pueden eliminar tareas de la lista.

## Requisitos

- Python 3.x
- Flask

## Instalación

1. Clona este repositorio:
   ```sh
   git clone https://github.com/tu-usuario/to-do-list-app.git
   cd to-do-list-app
   ```
2. Crea un entorno virtual e instala las dependencias:
   ```sh
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   pip install flask
   ```

## Uso
1. Ejecuta la aplicación:
   ```sh
    python app.py
    ```

2. Abre tu navegador y ve a `http://127.0.0.1:5000'

## Estructura del Proyecto

app.py: El archivo principal de la aplicación Flask.
index.html: La plantilla HTML para la página principal.
editar.html: La plantilla HTML para la página de edición de tareas.