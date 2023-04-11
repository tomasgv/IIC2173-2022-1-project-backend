#!/bin/bash
# Absolute path to this script, e.g. /home/user/bin/foo.sh
SCRIPT=$(readlink -f "$0")
# Absolute path this script is in, thus /home/user/bin
SCRIPTPATH=$(dirname "$SCRIPT")
echo $SCRIPTPATH

cd $SCRIPTPATH
cd ..
sudo cp -a appspec.yml ~/appspec.yml
sudo bash init-letsencrypt.sh
sudo docker-compose -f docker-compose.prod.yml build
sudo docker-compose -f docker-compose.prod.yml run app rails db:migrate
sudo docker-compose -f docker-compose.prod.yml run app rails db:seed
sudo docker-compose -f docker-compose.prod.yml run web python celery/manage.py migrate
sudo docker-compose -f docker-compose.prod.yml run chat npx sequelize db:migrate
sudo docker-compose -f docker-compose.prod.yml run chat npx sequelize db:seed:all
sudo docker-compose -f docker-compose.prod.yml up -d