# Puppet manifest to set up nginx web servers for the deployment of web_static

# Update package repositories
exec { 'apt_update':
  command => '/usr/bin/apt-get update',
  refreshonly => true,
}

# Install nginx package
package { 'nginx':
  ensure => installed,
  require => Exec['apt_update'],
}

# Allow Nginx HTTP through UFW
exec { 'allow_nginx_http':
  command => '/usr/sbin/ufw allow "Nginx HTTP"',
  path => '/usr/sbin',
}

# Create necessary directories
file { ['/data/web_static/shared/', '/data/web_static/releases/test/']:
  ensure => directory,
}

# Create index.html file with content
file { '/data/web_static/releases/test/index.html':
  ensure => file,
  content => "<html>\n  <head>\n  </head>\n  <body>\n    Holberton Schools\n  </body>\n</html>\n",
}

# Create symbolic link
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test/',
}

# Set ownership recursively
exec { 'set_ownership':
  command => '/bin/chown -hR ubuntu:ubuntu /data/',
}

# Update Nginx configuration
file_line { 'add_hbnb_static_location':
  path => '/etc/nginx/sites-enabled/default',
  line => '        location /hbnb_static { alias /data/web_static/current/; }',
  match => 'listen 80 default_server',
  ensure => present,
  require => Package['nginx'],
  notify => Service['nginx'],
}

# Restart Nginx service
service { 'nginx':
  ensure => running,
  enable => true,
  require => [Package['nginx'], File_line['add_hbnb_static_location']],
}
