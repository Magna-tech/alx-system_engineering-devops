# Install Nginx package
package { 'nginx':
  ensure => installed,
}
# Define the content for the default index page
file { '/var/www/html/index.html':
  ensure  => present,
  content => "Hello World!\n",
}

# Configure Nginx server
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => @("EOF"
server {
    listen 80;
    server_name _;

    location / {
        root /var/www/html;
        index index.html;
    }

    location /redirect_me {
        return 301 http://www.google.com;
    }
}
EOF
),
  notify  => Service['nginx'],
}

# Enable Nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

