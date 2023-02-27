from vkOsint import vkOsint
from vkOsint.exceptions import (ProxyError,
                                WrongAuthCredientals,
                                JsonDecodeError,
                                LimitError,
                                FloodError,
                                TokenError
                                )
def getOsintData():
    try:
        vkInstance = vkOsint(proxy='[proxy]')
        vkInstance.login(username='[login]',password='[password]')
        parsedData = vkInstance.osint(phoneNumbers=['+7......','+7......','+7.......'])
        return parsedData
    except ProxyError as ex:
        vkInstance.changeProxy('[newProxy]')
