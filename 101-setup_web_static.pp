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

# Create necessary directories with correct permissions
file { '/data':
  ensure => directory,
  owner => 'ubuntu',
  group => 'ubuntu',
}

file { '/data/web_static':
  ensure => directory,
  owner => 'ubuntu',
  group => 'ubuntu',
}

file { '/data/web_static/shared/':
  ensure => directory,
  owner => 'ubuntu',
  group => 'ubuntu',
}

file { '/data/web_static/releases/test/':
  ensure => directory,
  owner => 'ubuntu',
  group => 'ubuntu',
}

# Create index.html file with content and correct permissions
file { '/data/web_static/releases/test/index.html':
  ensure => file,
  content => "<html>\n  <head>\n  </head>\n  <body>\n    Holberton Schools\n  </body>\n</html>\n",
  owner => 'ubuntu',
  group => 'ubuntu',
}

# Create symbolic link with correct ownership
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test/',
  owner => 'ubuntu',
  group => 'ubuntu',
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
