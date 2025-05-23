# Utiliser une image Nginx de base
FROM nginx:alpine

# Supprimer les fichiers par défaut de Nginx
RUN rm -rf /usr/share/nginx/html/*

# Copier les fichiers Flutter Web dans Nginx
COPY . /usr/share/nginx/html

# Exposer le port 80
EXPOSE 80

# Lancer Nginx
CMD ["nginx", "-g", "daemon off;"]
