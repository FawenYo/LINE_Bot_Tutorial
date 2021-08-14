# Use the Nginx image
FROM nginx

# Remove the default nginx.conf
RUN rm /etc/nginx/conf.d/default.conf

# Replace with our own nginx.conf
COPY nginx.conf /etc/nginx/conf.d/
COPY certificate.pem /etc/nginx/certificate.pem
COPY private.key /etc/nginx/private.key