# script that ensures the web server functions properly

exec { 'Fix_wp':
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => shell,
}