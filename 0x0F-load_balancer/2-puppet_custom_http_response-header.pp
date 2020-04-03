# Configures a server with nginx adding a custom header
exec { 'apt-get -y update':
  provider  => 'shell',
}
-> exec { 'apt-get -y install nginx':
  provider  => 'shell',
}
-> exec { 'service nginx start':
  provider  => 'shell',
}
-> exec { 'sed -i "/sendfile on;/a \\tadd_header X-Served-By "$HOSTNAME";" /etc/nginx/nginx.conf':
  provider  => 'shell',
}
-> exec { 'service nginx restart':
  provider  => 'shell',
}