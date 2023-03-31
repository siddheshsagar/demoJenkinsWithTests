FROM python:3.10.4
ADD . /jenkins-demo
WORKDIR /jenkins-demo
RUN pip install -r requirements.txt
CMD ["python"]
