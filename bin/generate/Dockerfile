
# Stage 1: Build React app
FROM node:18 AS build
WORKDIR /app
COPY ./SADReact/ ./
RUN npm install --legacy-peer-deps

RUN npm run build

# Stage 2: PHP + Apache
FROM php:8.0-apache AS phpbase
RUN docker-php-ext-install pdo_mysql

# Stage 3: Final Apache server with React build
FROM httpd:2.4

# Copy React build to Apache web root
COPY --from=build /app/build/ /usr/local/apache2/htdocs/

# Enable mod_rewrite for React routing
RUN sed -i '/<Directory "\/usr\/local\/apache2\/htdocs">/,/<\/Directory>/ s/AllowOverride None/AllowOverride All/' /usr/local/apache2/conf/httpd.conf && \
    echo '<IfModule mod_rewrite.c>\n\
    RewriteEngine On\n\
    RewriteCond %{REQUEST_FILENAME} !-f\n\
    RewriteCond %{REQUEST_FILENAME} !-d\n\
    RewriteRule ^ /index.html [L]\n\
</IfModule>' >> /usr/local/apache2/conf/httpd.conf

EXPOSE 80
