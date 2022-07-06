# Auto build web-server with cgi-bin actived.
# Author: abdoul fataoh kabore

# Base Image
FROM httpd:latest

# Update repo and install python and pip
RUN apt-get update  && apt-get install python3 python3-pycurl -y && apt clean


# Import custum config file
COPY ./httpd.conf /usr/local/apache2/conf/httpd.conf

# Remove defaults apache cgi-bi folder files
RUN rm -rdf /usr/local/apache2/cgi-bin/*

# Copy souces code 
COPY ./app/  /usr/local/apache2/cgi-bin/

# Expose port
EXPOSE 80




