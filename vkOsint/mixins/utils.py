import random
import uuid
import hashlib

class Utils:
    def __init__(self):
        print('Utils init')
        self.genUa()
        self.genAuthHeaders()
        self.genBaseHeaders()
        self.genDeviceUuid()
        super().__init__()

    def genUa(self):
        androidResolutions = ['1024x600', '1280x800', '480x854', '720x1280', '1200x1290', '2560x1600', '768x1280', '1080x1920','800x1280']
        androidVersions = [{'sdkVersion':'28','androidVersion':'9'},{'sdkVersion':'29','androidVersion':'10'},{'sdkVersion':'30','androidVersion':'11'},{'sdkVersion':'31','androidVersion':'12'},{'sdkVersion':'33','androidVersion':'13'}]
        androidModels = ['SM-A505F','SM-A515','SM-A516F','SM-A526B','SM-A710F','SM-A530F']
        sdkV,androidV = random.choice(androidVersions).values()
        self.useragent = f'VKAndroidApp/7.24-3439 (Android {androidV}; SDK {sdkV}; armeabi-v7a; samsung {random.choice(androidModels)}; ru; {random.choice(androidResolutions)})'

    def genDeviceUuid(self):
        self.deviceUuid = str(uuid.uuid4())
        
    def genDeviceHash(self):
        seed = hashlib.md5(self.username.encode('utf-8') + self.password.encode('utf-8')).hexdigest()
        m = hashlib.md5()
        m.update(seed.encode('utf-8'))
        self.deviceHash = m.hexdigest()[:16]

    def genAuthHeaders(self):
        self.authHeaders = {
            'Host': 'oauth.vk.com',
            'User-Agent': self.useragent
        }

    def genBaseHeaders(self):
        self.baseHeaders = {
            'Host': 'api.vk.com',
            'Cache-Control': 'no-cache',
            'User-Agent': self.useragent,
            'X-Vk-Android-Client': 'new',
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'
        }



