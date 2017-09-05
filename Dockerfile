FROM python:3.6

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN echo "#!/bin/sh\n\
export DJANGO_SETTINGS_MODULE=prod_settings\n\
python manage.py migrate \n\
exec python manage.py runserver 0.0.0.0:8000" > run.sh && \
chmod +x run.sh
    
EXPOSE 8000

CMD [ "./run.sh" ]
