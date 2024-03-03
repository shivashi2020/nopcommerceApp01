import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")


class Readconfig():
    @staticmethod
    def getApplicationURL():
        url = config.get('LoginDetails', 'baseurl')
        return url


    @staticmethod
    def getUserEmail():
        username = config.get('LoginDetails', 'emailid')
        return username


    @staticmethod
    def getUserPassword():
        password = config.get('LoginDetails', 'password')
        return password
