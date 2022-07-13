# Crackpot CLI

Crackpot CLI will take an LDAP Dump <domain_users.grep>, an Active Directory Dump <activeDirectoryDump.txt> and a (optional) HashCat output to combine them into a clean CSV file for reading. This will also calculate the score of any cracked passwords using [zxcvbn](https://github.com/dwolfhub/zxcvbn-python).

Written by [Oliver Scotten](https://www.github.com/oliv10).

### Requirements
- Python 3.10.4 or greater

### Usage
- Install requirements
```
pip3 install -r requirements.txt
```

```
	   ______                  _                      
	  / _____)                | |                _    
	 | /       ____ ____  ____| |  _ ____   ___ | |_  
	 | |      / ___) _  |/ ___) | / )  _ \ / _ \|  _) 
	 | \_____| |  ( ( | ( (___| |< (| | | | |_| | |__ 
	  \______)_|   \_||_|\____)_| \_) ||_/ \___/ \___)
	                                |_|               
usage: crackpot.py [-h] [-cH] [-w] [-v] [-vv] [-s]
                   domainUsers activeDirectoryDump

Crackpot CLI Version 1.4.1

positional arguments:
  domainUsers
  activeDirectoryDump

options:
  -h, --help            show this help message and exit
  -cH , --crackedHash   path to file
  -w , --writeFile      path to file
  -v, --verbose
  -vv, --veryverbose
  -s, --slow-mode
```

```
./crackpot.py <domainUsers.grep> <activeDirectoryDump.txt> <crackedHash.txt>
```
