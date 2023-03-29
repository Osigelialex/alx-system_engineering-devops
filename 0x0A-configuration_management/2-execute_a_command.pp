# kills a process named killmenow

exec {'killmenow':
  command => '/usr/bin/pkill -SIGTERM killmenow',
  onlyif  => '/usr/bin/pgrep killmenow'
}
