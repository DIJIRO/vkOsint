from setuptools import find_packages, setup

longDescription = """
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
"""

requirements = [
    "PySocks==1.7.1",
    "requests==2.28.2",
    "urllib3==1.26.14",
]

setup(
    name="vkOsint",
    version="1.0",
    author="DIJIRO",
    author_email="de.sm1rnov@yandex.ru",
    license="MIT",
    url="https://github.com/DIJIRO/vkOsint",
    install_requires=requirements,
    keywords=[
        "vk private api",
        "vk osint",
        "vkOsint",
        "vk-api"
    ],
    description="Python package for searching vk accounts by phone number",
    long_description=longDescription,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.10",
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
