To run the application:

    docker-compose up -d

It will then be available on `localhost:8000`.

To access the command line tool you can use:

    docker exec -ti helloapp_web_1 sh

Inside the docker-container use `./manage.sh` as if it was `./manage.py`. Examples:

    ./manage.sh createsuperuser
    ./manage.sh hello 1
