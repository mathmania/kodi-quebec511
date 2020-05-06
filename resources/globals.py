import sys

try:  # Python 3
    from urllib.parse import urlparse
except ImportError:  # Python 2
    from urlparse import urlparse

class GlobalVariables(object):
    def initGlobals(self, argv):
        self.URL = urlparse(argv[0])
        try:
            self.PLUGIN_HANDLE = int(argv[1])
            self.IS_SERVICE = False
            self.BASE_URL = '{scheme}://{netloc}'.format(scheme=self.URL[0],
                                                            netloc=self.URL[1])
        except IndexError:
            self.PLUGIN_HANDLE = 0
            self.IS_SERVICE = True
            self.BASE_URL = '{scheme}://{netloc}'.format(scheme='plugin',
                                                            netloc=self.ADDON_ID)


g = GlobalVariables()