#Esto es un comentario

#Indicamos que se necesita una version de Python especifica
#Para mas informacion: https://hub.docker.com/_/python
FROM python:3.11-bullseye

#Actualizamos pip
RUN pip install --upgrade pip

#Indicamos la ubicacion del proyesto DENTRO del contenedor (no dentro de la maquina)
WORKDIR /code

#Copiamos el archivo 'requirements.txt' DENTRO DEL CONTENEDOR
COPY requirements.txt requirements.txt

#Instalamos via 'pip' los requerimientos dentro de 'requirements.txt'
RUN pip install -r requirements.txt

#Copiamos TODOS los archivos del directorio actual al directorio de trabajo del CONTENEDOR
COPY . .

#Realizamos las migraciones
RUN python manage.py makemigrations
RUN python manage.py migrate

#Ejecutamos la aplicacion
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]