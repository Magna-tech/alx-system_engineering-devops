# this file executes a command to install flask

package { 'python3-flask':
  ensure   => '2.1.0',
  provider => 'pip',
}

package { 'python3-pip':
  ensure => installed,
}
