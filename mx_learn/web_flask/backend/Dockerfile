FROM python:3.7-alpine
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host=tuna.tsinghua.edu.cn
COPY . /code/
ENV FLASK_APP hello.py
CMD flask run --host=0.0.0.0
 