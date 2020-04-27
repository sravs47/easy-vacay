
FROM centos/python-36-centos7

COPY . /easy_vacay/

WORKDIR /easy_vacay

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD flask run -h 0.0.0.0 -p 8080


