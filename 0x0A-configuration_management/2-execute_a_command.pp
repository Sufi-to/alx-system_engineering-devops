# kills a process using puppet
exec {'pkill':
  command  => 'pkill killmenow',
  provider => 'shell'
}
