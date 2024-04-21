file { '/etc/ssh/ssh_config':
  ensure => present,
}

file_line { 'Enable Password Authentication':
  ensure  => present,
  path    => '/etc/ssh/sshd_config',
  line    => '#  PasswordAuthentication no',
  match   => '^#  PasswordAuthentication',
}

file_line { 'IdentityFile':
  ensure  => present,
  path    => '/etc/ssh/sshd_config',
  line    => '#  IdentityFile ~/.ssh/school',
  match   => '^#  IdentityFile ~/.ssh/school',
}    
