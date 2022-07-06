# Crackpot CLI

Crackpot CLI will take an LDAP Dump domain_users.grep, Active Directory Dump activeDirectoryDump.txt and a Hashcat cracked.txt and combine them into a clean CSV file for reading.

Written by [Oliver Scotten](https://www.github.com/oliv10).

### Requirements
- Python 3.10.4 or greater

### Usage
- Install requirements
```
pip3 install -r requirements.txt
```

```
usage: crackpot.py [-h] [-w] [-v] [-s] domainUsers activeDirectoryDump crackedHash

./crackpot.py <domainUsers.grep> <activeDirectoryDump.txt> <crackedHash.txt>

positional arguments:
  domainUsers
  activeDirectoryDump
  crackedHash

options:
  -h, --help           show this help message and exit
  -w , --writeFile     path to file
  -v, --verbose
  -s, --slow-mode
```

```
./crackpot.py <domainUsers.grep> <activeDirectoryDump.txt> <crackedHash.txt>
```
