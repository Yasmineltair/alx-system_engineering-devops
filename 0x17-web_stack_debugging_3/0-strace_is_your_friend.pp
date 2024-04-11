# why Apache is returning a 500 error.
exec { 'fix wordpress':
  command       => "/bin/sed -i 's/phpp/php/g' /var/www/html/wp-setting.php",
}
