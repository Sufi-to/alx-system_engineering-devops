# Script that fixes nginx webserver

exec {'nginx_fix':
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  before   => Exec['nginx_restart'],
  provider => shell,
}

exec {'nginx_restart':
  command  => 'sudo service nginx restart',
  provider => shell,
}