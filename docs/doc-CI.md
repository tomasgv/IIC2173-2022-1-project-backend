# Documentación pipe CI:

1. Se crea la imagen de Ruby para la versión 3.0.2.
2. Se crea la imagen de la base de datos PostgreSQL / PostGIS y luego se configura el entorno.
3. Se obtiene el código del repositorio de GitHub con el comando “checkout”.
4. Se instalan las dependencias con el comando “bundle install”.
5. Se espera a que el puerto apropiado esté disponible, ya que la base de datos puede tardar un poco en estar disponible.
6. Se hace el setup de la base de datos con el comando “bundle exec rake db:setup”.


# Documentación CD:

1. Replicar archivo `config.yml`, en específico lo relativo al job `aws-code-deploy/deploy` 
2. Replicar archivo `appspec.yml`
3. Considerando las especificaciones el archivo anterior, crear archivos `before-install.sh` y `after-install.sh` en la carpeta `scripts`.
4. Agregar variables de entorno a configuración de proyecto en CircleCI (las variables referenciadas están en `config.yml`)