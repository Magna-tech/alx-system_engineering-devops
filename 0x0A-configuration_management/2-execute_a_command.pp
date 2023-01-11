# This manifest will execute commands

exec {'kill':
  command => 'pkill killmenow',
  path    => '/usr/bin/',
}
