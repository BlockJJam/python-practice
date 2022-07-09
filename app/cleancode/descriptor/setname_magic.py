from asyncio.log import logger


class DescriptorWithName :
    def __init__(self, name = None):
        self.name = name

    def __get__(self, instance, value):
        if instance is None:
            return self
        print('%r에서 %r 속성 가져오기', instance, self.name)
        return instance.__dict__[self.name]
    
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value
    
    
class ClientClass:
    descriptor = DescriptorWithName()

client = ClientClass()
client.descriptor = 'value'
print(client.descriptor)


