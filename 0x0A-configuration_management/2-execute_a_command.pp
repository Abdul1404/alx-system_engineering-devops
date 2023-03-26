# kills a program called killmenow
exec{ 'killmenow':
  command   => 'pkill killmenow',
  path      => '/usr/bin',
  logoutput => true
  }
