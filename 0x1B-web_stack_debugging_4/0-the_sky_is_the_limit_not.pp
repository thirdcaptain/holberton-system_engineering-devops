# Increases file descriptor limit of nginx
exec { 'edit file':
  command => "/bin/sed -i 's/15/4000/g' /etc/default/nginx && sudo service nginx restart"
}

