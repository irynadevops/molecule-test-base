# molecule_test_base
### Description: 
*Testing ansible base role by molecule and tesinfra tests.*


### Requirements:
*Please install docker and molecule/ Also you need use python 3.7 version for testinfra.*
- pip install docker molecule

Of course, you can install its by yum,apt or pacman but better is using of pip.

### How to use:
*Don't forget start docker service.*
- systemctl start docker

### How to start:
- molecule init role <name_of_role>

[документация molecule](https://molecule.readthedocs.io/en/latest/getting-started.html) 

[github molecule](https://github.com/ansible-community/molecule)
