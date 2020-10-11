# molecule_test_base
### Description: 
*Testing the role of ansible playbook with molecule tests and testinfra.*

### Requirements:
*You can of course install it using yum, apt or pacman, but pip is better.*
- pip install docker molecule flake8 ansible-lint

### How to use:
*Don't forget to start the docker service.*
- sudo systemctl start docker

### Recommendation:
You need to use python version <= 3.7 for testinfra
If you are using Python version other than 3.7.1, remove the ".python-version" file or install it.

- pyenv install 3.7.1 (or any version of 3.7)
- pyenv local 3.7.1 (or global)

### How to start:
- molecule test

[документация molecule](https://molecule.readthedocs.io/en/latest/getting-started.html) 

[github molecule](https://github.com/ansible-community/molecule)
