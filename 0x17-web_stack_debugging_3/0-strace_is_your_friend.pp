# Script that ensures the web server functions properly

exec { 'Fix file name':
  command  => 'sudo sed -i "s/.php/.phpp/" /var/www/html/class-wp-locale.php',
  provider => shell,
}