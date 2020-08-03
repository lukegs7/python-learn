FROM python:3.7
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple  --trusted-host pypi.tuna.tsinghua.edu.cn
COPY ./EnvManager/ .

EXPOSE 8000
CMD ["gunicorn","EnvManager.wsgi","-b","0.0.0.0:8000"]
