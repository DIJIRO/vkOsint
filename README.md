###
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/vkosint)
[![Downloads](https://pepy.tech/badge/vkosint)](https://pepy.tech/project/vkosint)
[![Downloads](https://pepy.tech/badge/vkosint/month)](https://pepy.tech/project/vkosint)
[![Downloads](https://pepy.tech/badge/vkosint/week)](https://pepy.tech/project/vkosint)

## vkOsint - Python package for searching vk accounts by phone number

Features:
* Authorization by login and password
* Tokens parsing
* Accounts searching by phone number
* Source code contains all the api's hash functionality

Package uses Private api without selenium.
Developed by reverse engineering & api sniffing

Support **Python >= 3.10**

## ToDo
- [ ] 2fa authorization
- [ ] Osint function return value filters
## Installation
```console
$ pip install vkOsint
```
### Basic Usage

``` python
import json

from vkOsint import vkOsint

vkInstance = vkOsint(proxy='[proxy]')
vkInstance.login(username='[login]',password='[password]')
parsedData = vkInstance.osint(phoneNumbers=['+7..........','+7..........'])
with open('results.json','w') as file:
    json.dump(parsedData,file,indent=4,ensure_ascii=True)
```
## Documentation

### vkOsint

#### Main class
Input
* proxy (default = None)
* verbose (default = True)
* sessionVerify (default = True)
``` python
from vkOsint import vkOsint

vkInstance = vkOsint(proxy='[proxy]',sessionVerify=True,verbose=False)
```
### login function

#### Basic authorization
Input
* username (phone number of parser account)
* password (Password of parser account)
``` python
vkInstance.login(username='[login]',password='[password]')
```
### tokenAuth function 

#### Skip the auth by providing parser account's tokens
Input
* username
* accessToken
* secret
* userId
``` python
vkInstance.tokenAuth(username='[login]',accessToken='[accessToken]',secret='[secret]',userId='[userId]')
```
### getTokens

#### Get auth tokens of authorized account in vkOsint instance
Input
* None

Output
```json
{
    "accessToken": "[self.accessToken]",
    "secret": "[self.secret]",
    "userId": "[self.userId]",
    "webviewRefreshToken": "[self.webviewRefreshToken]",
    "webviewAccessToken": "[self.webviewAccessToken]"
}
```
### changeProxy function 

#### Change the proxy of current vkOsint instance
Input
* proxy
``` python
vkInstance.changeProxy(proxy='[proxy]')
```


