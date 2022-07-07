# Crackpot CLI

Crackpot CLI will take an LDAP Dump <domain_users.grep>, an Active Directory Dump <activeDirectoryDump.txt> and a (optional) HashCat output to combine them into a clean CSV file for reading.

Written by [Oliver Scotten](https://www.github.com/oliv10).

### Requirements
- Python 3.10.4 or greater

### Usage
- Install requirements
```
pip3 install -r requirements.txt
```

```
usage: crackpot.py [-h] [-cH] [-w] [-v] [-s] domainUsers activeDirectoryDump

Crackpot CLI Version 1.1.2

positional arguments:
  domainUsers
  activeDirectoryDump

options:
  -h, --help            show this help message and exit
  -cH , --crackedHash   path to file
  -w , --writeFile      path to file
  -v, --verbose
  -s, --slow-mode
```

```
./crackpot.py <domainUsers.grep> <activeDirectoryDump.txt> <crackedHash.txt>
```
