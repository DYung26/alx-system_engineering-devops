exec { 'install_stdlib_module':
  command     => '/opt/puppetlabs/bin/puppet module install puppetlabs-stdlib',
  path        => ['/usr/bin', '/bin', '/usr/sbin', '/sbin'],
  logoutput   => true,
  refreshonly => true,
}

include  stdlib

# ensure '/etc/ssh/ssh_config' exists
file { '/etc/ssh/ssh_config':
  ensure => present,
}

# Enable Password Authentication
file_line { 'Enable Password Authentication':
  ensure => present,
  path   => '/etc/ssh/sshd_config',
  line   => '#  PasswordAuthentication no',
  match  => '#  PasswordAuthentication',
}

# Declare identity file
file_line { 'IdentityFile':
  ensure => present,
  path   => '/etc/ssh/sshd_config',
  line   => '#  IdentityFile ~/.ssh/school',
  match  => '#  IdentityFile ~/.ssh/school',
}    
