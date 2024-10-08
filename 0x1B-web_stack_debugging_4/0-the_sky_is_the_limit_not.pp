# Automates setting up an Nginx server to handle 2000 requests with every 100 made concurrently
exec { 'Limit':
  command => '/usr/bin/env sed -i s/15/2000/ /etc/default/nginx',
  unless  => '/usr/bin/grep -q "2000" /etc/default/nginx',
}

exec { 'Restart Nginx':
  command => '/usr/bin/env service nginx restart',
  require => Exec['Limit'],
}

