import configparser

class PropertyUtil:

    @staticmethod
    def getPropertyString():
        config = configparser.ConfigParser()
        config.read('database.properties')

        host = config.get('Database', 'host')
        dbname = config.get('Database', 'dbname')
        user = config.get('Database', 'user')
        password = config.get('Database', 'password')
        port = config.get('Database', 'port')

        connection_string = f"host={localhost} dbname={appointment} user={root} password={root} port={'3305'}"
        return connection_string