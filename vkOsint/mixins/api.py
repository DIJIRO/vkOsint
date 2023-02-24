import requests
from urllib3.exceptions import MaxRetryError,NewConnectionError
from socket import gaierror
import json
import urllib
import hashlib
from vkOsint.exceptions import *
class Api:
    def __init__(self):
        print('API init')
        self.session = requests.session()
        super().__init__()
    
    def login(self,username: str,password: str):
        self.username = username
        self.password = password
        self.genDeviceHash()
        print(username)
        print(password)
        authParams = {
            'scope': 'nohttps,all',
            'client_id': '2274003',
            'client_secret': 'hHbZxrka2uZ6jB1inYsH',  # apps secret token - static
            'v': '5.96',
            'lang': 'ru',
            '2fa_supported': '1',
            'lang': 'ru',
            'device_id': self.deviceHash,
            'grant_type': 'password',
            'username': self.username,
            'password': self.password,
            'libverify_support': '0'
        }
        try:
            authData = self.session.get('https://oauth.vk.com/token', params=authParams, headers=self.authHeaders).json()
            self.authDataParser(authData)
        except json.decoder.JSONDecodeError:
            raise JsonDecodeError("Error in decoding response json")
        except (requests.exceptions.ProxyError,MaxRetryError,NewConnectionError,gaierror):
            raise ProxyError("Lost connection to server, Inavild proxy")

    def updateTokens(self):
        data = {'v': '5.96',
                'https': '1',
                'timestamp': '0',
                'receipt2': 'eyJhbGciOiAibm9uZSJ9.eyJub25jZSI6ICJ0ZXN0PT0ifQ.',
                'device_id': self.deviceUuid,
                'receipt': 'yssp9o9p9pamz5t-nvmq8spgwtin3e0==',  # статические параметры ( можно не обращать внимание )
                'lang': 'ru',
                'access_token': self.accessToken
                }
        tokensData = self.makeRequest('auth.refreshToken',data)
        self.updateTokensParser(tokensData)

    def osint(self,phoneNumbers: list):
        assert isinstance(phoneNumbers, list), f'Phone numbers must be list format, but now its {type(phoneNumbers)}, you can also provide 1 number in the list'
        self.phoneNumbers = phoneNumbers
        self.parsedData = {}
        for self.phoneNumber in phoneNumbers:
            self.searchContact()
            self.contactDataParser()
            self.getProfile()
            self.profileParser()
        return self.parsedData






    def searchContact(self):
        contacts = {
            "phone":
                {
                    "user_contact": self.username,
                    "contacts": self.phoneNumber
                }
        }
        data = {'v': '5.96',
                'https': '1',
                'device_id': self.deviceUuid,
                'fields': 'online,photo_50,photo_100,photo_200,career,city,country,education,verified,trending',
                'lang': 'ru',
                'search_only': '0',
                'count': '5000',
                'contacts': json.dumps(contacts, separators=(',', ':')),
                'need_mutual': '1',
                'access_token': self.accessToken,
                }
        contactData = self.makeRequest('account.searchContacts', data)
        self.contactData = contactData

    def getProfile(self):
        data = {
            'v': '5.96',
            'https': '1',
            'track_code': self.trackCode,
            'source': 'friends_import_address_book',
            'gift_count': '25',
            'track_events': '1',
            'skip_hidden': '1',
            'photo_sizes': '1',
            'func_v': '8',
            'access_keys':  self.accessKey,  # ВАЖНО!!!
            'device_id': self.deviceUuid,
            'photo_count': '25',
            'lang': 'ru',
            'ref': 'profile',
            'user_id': self.userId,  # id профиля бота
            'access_token': self.accessToken

        }
        self.profileData = self.makeRequest('execute.getFullProfileNewNew', data)


    def makeRequest(self,method,data):
        baseUrl = 'https://api.vk.com/method/'
        sigStr = f'/method/{method}?' + urllib.parse.unquote(urllib.parse.urlencode(data)) + self.secret
        print(sigStr)
        sig = hashlib.md5(sigStr.encode()).hexdigest()
        print(sig)
        data['sig'] = sig
        try:
            response = self.session.post(f'https://api.vk.com/method/{method}', headers=self.baseHeaders, data=data)
            jsonResp = response.json()
            if 'error' in jsonResp:
                if jsonResp['error']['error_code'] == 13:
                    raise LimitError("Requests limist reached")
                elif jsonResp['error']['error_msg'] == 'Flood control':
                    raise FloodError("Flood control triggerred, change bot account")
                elif jsonResp['error']['error_msg'] == 'Token confirmation required':
                    raise TokenError("Access & Secret tokens expired")
            return jsonResp
        except json.decoder.JSONDecodeError:
            raise JsonDecodeError("Error in decoding response json")
        except (requests.exceptions.ProxyError,MaxRetryError,NewConnectionError,gaierror):
            raise ProxyError("Lost connection to server, Inavild proxy")

