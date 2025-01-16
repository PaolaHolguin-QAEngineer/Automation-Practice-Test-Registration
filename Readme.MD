# Automation Practice Registration Test

Este proyecto tiene como objetivo automatizar el proceso de registro en la página **Automation Practice** usando **Selenium** y **PyTest**.

## Descripción

El proyecto utiliza Selenium para interactuar con el navegador web, específicamente con el sitio de **Automation Practice**. Utiliza locaciones específicas para identificar los elementos de la página y métodos personalizados para realizar interacciones como llenar campos de formulario, hacer clic en botones y seleccionar opciones en menús desplegables.

El flujo de pruebas automatiza el proceso de registro completando campos como el correo electrónico, nombre, apellido, fecha de nacimiento y selecciona las opciones correctas en los menús desplegables.

## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener los siguientes requisitos instalados:

- Python (se recomienda versión 3.x)
- Selenium
- PyTest

Instala las dependencias necesarias con el siguiente comando:

 ```bash  
 pip install -r requirements.txt 
 ```
## Estructura del proyecto

 ```bash 
.
├── Data.py                # Datos para pruebas, como URLs, credenciales, etc.
├── Locators.py            # Locación de elementos en la página web
├── methods.py             # Métodos genéricos de interacción con la página
├── Test.py                # Caso de prueba para automatización del registro
├── README.md              # Este archivo
└── venv/                  # Entorno virtual
```
## Configuración

1. Instalación de dependencias: Asegúrate de tener Python 3.x y Selenium instalados. Puedes crear un entorno virtual para las dependencias:

 ```bash 
python -m venv venv
source venv/bin/activate  # En sistemas Unix/Linux
venv\Scripts\activate      # En sistemas Windows
pip install -r requirements.txt
```
2. Configuración de WebDriver: Configura WebDriver (por ejemplo, ChromeDriver) en tu sistema para que Selenium pueda interactuar con tu navegador.

## Uso

1. Ejecutar las pruebas automatizadas:
```bash 
pytest Test.py
```
2. El proceso ejecutará el caso de prueba definido para el registro en la página Automation Practice y validará cada paso del flujo.

## Contribuciones
Cualquier contribución al proyecto es bienvenida. Si encuentras errores o tienes mejoras, por favor abre un pull request o un issue.

¡Gracias por revisar este proyecto!