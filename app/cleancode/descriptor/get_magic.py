class DescriptorClass:
    def __get__(self, instance, owner):
        if instance is None:
            return f'{self.__class__.__name__}.{owner.__name__}'
        return f'value for {instance}'
    
class ClientClass:
    descriptor = DescriptorClass()

print(ClientClass.descriptor) # 직접 호출
print(ClientClass().descriptor) # 객체 호출

