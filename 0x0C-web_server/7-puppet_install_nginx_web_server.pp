# install inginx with puppet
package { 'nginx':
  ensure  => 'installed',
}

file { '/var/www/html/index/html':
  ensure  => 'file',
  content => 'Hello World!',
  mode    => '0644',
  require => package['nginx'],
}

exec { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => package['nginx'],
}
