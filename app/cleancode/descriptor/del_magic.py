class ProtectedAttribue:
    def __init__(self, requires_role = None)-> None:
        self.permission_required = requires_role
        self._name = None

    def __set_name__(self, owner, name):
        self._name = name
    
    def __set__(self, user, value):
        if value is None:
            raise ValueError(f'{self._name}를 None으로 설정불가')
        user.__dict__[self._name] = value

    def __delete__(self, user):
        if self.permission_required in user.permission_list:
            user.__dict__[self._name] = None
        else:
            raise ValueError(
                f'{user!s} 사용자는 {self.permission_required} 권한이 없음'
            )


class User:

    email = ProtectedAttribue(requires_role= "admin")

    def __init__(self, username: str, email: str, permission_list: list = None):
        self.username = username
        self.email = email
        self.permission_list = permission_list or []
    
    def __str__(self):
        return self.username


admin = User('root', 'root@em.com', ['admin'])
user = User('user1', 'user1@em.com', ['email','help'])

print(admin.email)
del admin.email
print(admin.email)
print(admin.username)
