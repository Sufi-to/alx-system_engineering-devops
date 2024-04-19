# kills a process using puppet
exec {'killmenow':
  command => 'pkill'
}
