# this file executes a command to install flask

exec { 'install_flask':
  command     => '/usr/bin/pip3 install flask==2.1.0',
  path        => ['/usr/bin'],
  unless      => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
}

package { 'python3-pip':
  ensure   => installed,
}
