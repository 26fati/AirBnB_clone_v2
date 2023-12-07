# Use Puppet to automate the task of creating a custom HTTP header response

content="
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

exec {'update':
  command => '/usr/bin/apt-get update',
}
-> package {'nginx':
  ensure => 'present',
}
-> file { '/data':
  ensure => directory,
}

-> file { '/data/web_static':
  ensure => directory,
}

-> file { '/data/web_static/releases':
  ensure => directory,
}

-> file { '/data/web_static/shared':
  ensure => directory,
}

-> file { '/data/web_static/releases/test':
  ensure => directory,
}

-> file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  content => $content,
}

-> file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
}

-> exec { 'change_ownership':
  command => 'chown -R ubuntu:ubuntu /data/',
  path    => '/bin',
}

-> exec { 'insert_header_line':
  command => "sed -i '57i\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-enabled/default",
  path    => ['/bin', '/usr/bin'],
}
-> exec {'run':
  command => '/usr/sbin/service nginx restart',
}
