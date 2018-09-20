# Increases file descriptor limit of nginx
$settings = '/etc/default/nginx'
file { $settings:
  ensure => present,
}
exec { 'edit file':
  command => "sed -i 's/15/800000/g' ${settings}",
  path    => [ '/bin/' ]
}

exec { 'restart nginx':
  command => 'service nginx restart',
  path    => [ '/usr/bin/' ]
}
