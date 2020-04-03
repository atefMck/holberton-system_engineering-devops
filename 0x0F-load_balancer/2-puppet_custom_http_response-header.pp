# Configures a server with nginx adding a custom header
exec { 'apt-get -y update':
  provider  => 'shell',
}
-> package {'check':
  name => "nginx",
  ensure => present,
}
-> service { 'starting':
  name => "nginx",
  ensure => running,
}
-> file { 'Adding header':
  path => '/etc/nginx/nginx.conf',
  line   => "	sendfile on;
  add_header X-Served-By ${hostname};",
  match  => '^\tsendfile on;',
}
-> exec { 'service nginx restart':
  provider  => 'shell',
}