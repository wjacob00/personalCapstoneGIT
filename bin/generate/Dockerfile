FROM opensuse/tumbleweed
RUN apt update
RUN apt install -y apache2
RUN apt install -y apache2-utils
RUN clean

FROM php:8-apache
COPY ../../ /app/static
RUN docker-php-ext-install pdo_mysql
