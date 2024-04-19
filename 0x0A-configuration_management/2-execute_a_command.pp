# kills a process using puppet
exec {'kill':
  command  => 'pkill killmenow',
  provider => 'shell'
}
