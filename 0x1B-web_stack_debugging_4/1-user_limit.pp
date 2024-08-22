# Permanently increases the maximum number of open file descriptors to 20000 by editing `/etc/security/limits.conf`
exec { 'Fix hard limit':
  command => '/usr/bin/env sed -i "s/4/20000/; s/5/20000/" /etc/security/limits.conf'
}

