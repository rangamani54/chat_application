FROM rangamani54/basic-python3:v1

ADD appserver.py

EXPOSE 1000

CMD ["python3", "appserver.py"]
