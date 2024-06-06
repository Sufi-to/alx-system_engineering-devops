# script that ensures the web server functions properly

exec { 'fix-wp':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-includes/class-wp-locale.php',
  path    => '/usr/local/bin/:/bin/'
}