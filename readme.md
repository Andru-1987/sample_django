django primeros pasos
----
django-admin startproject <nombre_del_proyecto>
cd <nombre_del_proyecto>
django-admin startapp <nombre_de_la_app>
- Creacion de la primera app
- Creacion de la primera vista

    
---
para conectar la base de postgress con django tenemos que usar lo siguiente:
si estas en mac o linux por desgracia hay que instalar localmente

pip install psycopg2

para el manejo de los .env es necesario
pip install python-dotenv

configurar en la parte de settins.py los engines por default
y cambiar el que viene que es sqlite3 por postgresql
```
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': ‘<database_name>’,
       'USER': '<database_username>',
       'PASSWORD': '<password>',
       'HOST': '<database_hostname_or_ip>',
       'PORT': '<database_port>',
   }
}
```

instalar la app que creamos en la parte de installed app
```
INSTALLED_APPS=[ 'app_blog',...INSTALLED_APP]
```
---
Creando una tabla con un model.
Registrar en el sector de admin

---
Crear un super usuario admin 
```
python manage.py createsuperuser
anderson
123
```

