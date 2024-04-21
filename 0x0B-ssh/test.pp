file { './test':
  ensure => present,
}

file_line { 'Enable Password Authentication':
  ensure  => present,
  path    => './test',
  line    => '#  PasswordAuthentication no',
  match   => '^#  PasswordAuthentication',
}

file_line { 'IdentityFile':
  ensure  => present,
  path    => './test',
  line    => '#  IdentityFile ~/.ssh/school',
  match   => '^#  IdentityFile ~/.ssh/school',
}    
