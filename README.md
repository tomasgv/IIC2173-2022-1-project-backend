# Pasos para ejecutar aplicación en entorno local

## Backend

1. Rellenar variables de entorno:

    `celery/.env`
    `celery/main/local_settings.py`

    Estos archivos tienen una versión `.default` para completar.

2. Hacer build de los contenedores de Docker:
   
   `docker-compose build`

3. Correr migraciones:

    `docker-compose run app rails db:migrate`
    `docker-compose run web python celery/manage.py migrate`
    `docker-compose run chat npx sequelize db:migrate`

4. Ejecutar seeds:

    `docker-compose run app rails db:seed`
    `docker-compose run chat npx sequelize db:seed:all`


5. Levantar contenedores:

    `docker-compose up -d`

Cabe destacar que para el entorno de producción se usa el archivo `docker-compose.prod.yml`, el cual incluye los servicios de nginx y certbot.

## Frontend

1. Rellenar variables de entorno (vienen completas)

1. Instalar librerías mediante yarn:

    `yarn install`

1. Levantar aplicación:

    `yarn start`