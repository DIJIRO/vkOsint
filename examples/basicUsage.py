import json

from vkOsint import vkOsint

vkInstance = vkOsint(proxy='[proxy]')
vkInstance.login(username='[login]',password='[password]')
parsedData = vkInstance.osint(phoneNumbers=['+7..........','+7..........'])
with open('results.json','w') as file:
    json.dump(parsedData,file,indent=4,ensure_ascii=True)