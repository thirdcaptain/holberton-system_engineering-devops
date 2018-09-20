# Increases file descriptor limit of nginx
$settings = '/etc/default/nginx'
file { $settings:
  ensure => present,
}
exec { 'edit file':
  command => "sed -i 's/15/4000/g' /etc/default/nginx && sudo service nginx restart",
  path    => [ '/bin/' ]
}

