class Connector:
    def __init__(self, source):
        self.source = source
        self.__timeout = 60



conn = Connector('postgresql://localhost')
# {'source': 'postgresql://localhost', '_Connector__timeout': 60} <- _Connector__timeout = 맹글링
print(conn.__dict__)
        

