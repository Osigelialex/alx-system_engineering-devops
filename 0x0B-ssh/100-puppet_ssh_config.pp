#!/usr/bin/env bash
# client configuration file with puppet

class my_ssh_config {
	ssh_config { '144983-web-01':
	ensure => 'present',
	host => '18.207.142.20',
	IdentityFile => '~/.ssh/school'
	}	
}
