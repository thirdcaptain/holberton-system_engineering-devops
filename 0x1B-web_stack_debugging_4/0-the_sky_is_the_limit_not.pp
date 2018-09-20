# Increases file descriptor limit of nginx
$settings = '/etc/default/nginx'
file { $settings:
  ensure => present,
}
exec { 'edit file':
  command => "sed -i 's/15/4000/g' /etc/default/nginx",
  path    => [ '/bin/' ]
}

exec { 'restart nginx':
  command => 'service nginx restart',
  path    => [ '/usr/bin/' ]
}
