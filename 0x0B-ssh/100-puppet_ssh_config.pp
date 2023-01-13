# Puppet manifest to set up ssh configuration file
class ssh_config {
  file_line { 'use school':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'IdentityFile ~/.ssh/school',
  }

  file_line { 'no_password_authentication':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'PasswordAuthentication no',
  }
}

