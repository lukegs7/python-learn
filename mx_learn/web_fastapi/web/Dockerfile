FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host=tuna.tsinghua.edu.cn
ADD app /app/app
EXPOSE 80
