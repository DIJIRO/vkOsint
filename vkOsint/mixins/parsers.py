from vkOsint.exceptions import WrongAuthCredientals

class Parsers:
    def __init__(self):
        print('Parsers init')
        super().__init__()

    def authDataParser(self,authData):
        if 'error_description' in authData and authData['error_description'] == 'Неправильный логин или пароль':
            raise WrongAuthCredientals(f"Login or password is incorrect\nLogin : {self.username}\nPassword : {self.password}\n")
        if 'access_token' and 'user_id' and 'secret' in authData:
            self.accessToken = authData['access_token']
            self.secret = authData['secret']
            self.userId = authData['user_id']
            print(self.accessToken)
            print(self.secret)
            print(self.userId)
            print('Authorized successfully')
        else:
            raise SystemExit('Unknown Error')

    def updateTokensParser(self,tokensData):
        self.accessToken = tokensData['response']['token']
        self.secret = tokensData['response']['secret']

    def contactDataParser(self):
        print(self.contactData)
        contact = self.contactData['response']['found'][0]['user']
        self.trackCode = contact['track_code']
        self.accessKey = contact['access_key']

    def profileParser(self):
        self.parsedData[self.phoneNumber] = self.profileData
