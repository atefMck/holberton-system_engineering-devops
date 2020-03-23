# Installs puppet-lint
exec { 'gem install puppet-lint -v 2.1.1':
  provider  => 'shell',
}
