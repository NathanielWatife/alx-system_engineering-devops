# This Puppet manifest ensures the necessary PHP modules are installed to avoid a 500 error in Apache

package { 'php5-mysql':
  ensure => installed,
}

# Ensure Apache is restarted after installing the package
service { 'apache2':
  ensure     => running,
  enable     => true,
  subscribe  => Package['php5-mysql'],
}

exec { 'fix-wordpress-permissions':
  command => 'chown -R www-data:www-data /var/www/html/wordpress',
  onlyif  => 'test "$(stat -c %U /var/www/html/wordpress/wp-config.php)" != "www-data"',
  notify  => Service['apache2'],
}
