'''
@Serialization(
    username = show_original,
    password = hide_field,
    ip = show_original,
    timestamp = format_time
)
@dataclass
class LoginEvent:
    username: str
    password: str
    ip: str
    ti

와 같은 동작의 코드를 Descriptor로 작성
'''

from datetime import datetime
from functools import partial
from typing import Callable

class BaseFieldTransformation:
    def __init__(self, transformation: Callable[[],str]) -> None:
        self._name = None
        self.transformation = transformation

    def __get__(self, instance, owner):
        if instance is None:
            return self
        raw_value = instance.__dict__[self._name]
        return self.transformation(raw_value)

    def __set_name__(self, owner, name):
        self._name = name

    def __set__(self, instance, value):
        instance.__dict__[self._name] = value

ShowOriginal = partial(
    BaseFieldTransformation,
    transformation = lambda x: x
)

HideField = partial(
    BaseFieldTransformation,
    transformation = lambda x: '**민감정보 공개불가**'
)

FormatTime = partial(
    BaseFieldTransformation,
    transformation = lambda ft: ft.strftime('%Y-%m-%d %H:%M')
)

class LoginEvent:
    username = ShowOriginal()
    ip = ShowOriginal()
    password = HideField()
    timestamp = FormatTime()

    def __init__(self, username, ip, password, timestamp):
        self.username = username
        self.ip = ip
        self.password = password
        self.timestamp = timestamp

    def serialize(self):
        return {
            'username': self.username,
            'password': self.password,
            'ip' : self.ip,
            'timestamp' : self.timestamp
        }

user1 = LoginEvent('jjm','10.10.10.10','hellopwd',datetime.now())
print(user1.serialize())
print(user1.password, user1.timestamp)
print(vars(user1))
import pandas