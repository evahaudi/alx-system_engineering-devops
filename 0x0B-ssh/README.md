# SSH
Project done during **Software Engineering studies** at **ALX School**. It aims to learn about what is a SSH, how to create a SSH RSA key pair and how to connect to a remote host using SSH.

## Technologies
* Scripts written in Bash 5.0
* Tested on Ubuntu 20.04 LTS
* Puppet 7.10

## Files

| Filename | Description |
| -------- | ----------- |
| `0-use_a_private_key` | Uses `ssh` to connect to a server using a private key previously generated |
| `1-create_ssh_key_pair` | Creates an RSA key pair |
| `2-ssh_config` | SSH client configuration using a private key and refusing to authenticate using a password |
| `100-puppet_ssh_config.pp` | Sets up the client SSH configuration file to connect to a server without typing a password |