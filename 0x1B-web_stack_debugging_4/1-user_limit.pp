# Script that changes the OS configuration so that it is possible 
# to login with the holberton user and open a file without any error message.

exec {'hard_nofile':
  command  => 'sudo sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',
  provider => shell,
  before   => Exec['soft_nofile'],
}

exec {'soft_nofile':
  command  => 'sudo sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf',
  provider => shell,
}