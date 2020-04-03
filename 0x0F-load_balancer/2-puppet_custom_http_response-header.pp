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
-> exec { 'Adding header':                                                                                                                                          
  provider  => 'shell',                                                                                                                                          
  command   => "sed -i -e '/sendfile on;/a \\\tadd_header X-Served-By '$HOSTNAM\                                                                                 
E';' /etc/nginx/nginx.conf",                                                                                                                                     
}                                                                                                                                                                
-> exec { 'service nginx restart':                                                                                                                               
  provider  => 'shell',                                                                                                                                          
}      