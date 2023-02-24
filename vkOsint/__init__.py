from urllib.parse import urlparse


from vkOsint.mixins.api import Api
from vkOsint.mixins.utils import Utils
from vkOsint.mixins.parsers import Parsers


class vkOsint(Api,Utils,Parsers):

    def __init__(self,
                settings: dict = {},
                proxy: str = None,
                delay_range: list = None,
                **kwargs
    ):
        super().__init__()
        self.setProxy(proxy)
        
    def setProxy(self,proxy):
        if proxy:
            assert isinstance(proxy,str),f'Proxy must be string format, but now its {type(proxy)}'
            proxyHref = "{scheme}{href}".format(
                scheme="http://" if not urlparse(proxy).scheme else "",
                href=proxy,
            )
            self.session.proxies = {
                "http": proxyHref,
                "https": proxyHref,
            }