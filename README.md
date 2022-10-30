# Guia de instalacion

1. Primero debemos clonar este repositorio o descargar el archivo zip.
2. Luego crea un entorno virtual para utilizar los paquetes a usar en el server (puedes usar venv o virtualenv con Python).
3. Luego de ello enciende el entorno virtual y en el directorio raiz del proyecto ejecutamos el comando pip install -r requirements.txt
4. Luego dentro de la carpeta core, en el settings.py en la sección de databases dentro de el sustituiremos todo de la siguiente forma: 
 
```python
'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'NOMBRE_DE_LA_BD',
        'USER':'root',
        'PASSWORD':'CONTRASEÑA_DEL_USUARIO',
        'HOST':'localhost',
        'PORT':'3306'
    }
```
5. Como siguiente paso debemos agregar un archivo dentro de la carpeta core, con el nombre de **.env** y dentro de el escribiremos los siguientes datos:
```.env
SECRET_KEY=cualquierllavesecretadeejemplo
DEBUG=True
```

6. En SECRET_KEY ingresamos la llave secreta que deseemos.
7. Por ultimo ejecutamos los siguientes comandos para realizar las migraciones:
```bash
python .\manage.py makemigrations
python .\manage.py migrate
```

Y asi habremos migrado y configurado la base de datos a usar por django.

8. Por ultimo corremos el servidor: 
```bash
python .\manage.py runserver
```