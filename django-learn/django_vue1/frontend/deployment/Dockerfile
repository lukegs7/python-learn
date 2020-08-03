FROM nginx:latest

COPY ./dist /usr/share/nginx/dist
COPY ./default.conf /etc/nginx/conf.d/default.conf
WORKDIR /usr/share/nginx/dist

EXPOSE 80
