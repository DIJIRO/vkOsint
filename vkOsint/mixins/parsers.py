from vkOsint.exceptions import WrongAuthCredientals,UnknownError

class Parsers:

    def __init__(self):
        super().__init__()

    def authDataParser(self,authData):
        if 'error_description' in authData and authData['error_description'] == 'Неправильный логин или пароль':
            raise WrongAuthCredientals(f"Login or password is incorrect\nLogin : {self.username}\nPassword : {self.password}\n")
        if 'access_token' and 'user_id' and 'secret' in authData:
            self.setTokens(authData)
            self.writeOutput('Authorized successfully')
        else:
            print(authData)
            raise UnknownError('Unknown Error')

    def updateTokensParser(self,tokensData):
        self.accessToken = tokensData['response']['token']
        self.secret = tokensData['response']['secret']

    def contactDataParser(self):
        if len(self.contactData['response']['found']):
            contact = self.contactData['response']['found'][0]['user']
            self.trackCode = contact['track_code']
            self.accessKey = contact['access_key']
            self.found = True
        else:
            self.found = False

    def profileParser(self):
        self.parsedData[self.phoneNumber] = self.profileData
        self.parsedData[self.phoneNumber]['found'] = self.found

