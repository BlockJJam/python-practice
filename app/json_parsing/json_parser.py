from dataclasses import dataclass
from functools import partial
from json_parsing.parsed_data import DB, Key
from typing import Iterable
import json

# from json_parsing.parsed_data import DB, Key
from json_parsing.matcher import Matcher, DbMatcher, KeyMatcher

class ClientAttribute:
    def __init__(self, matcher: Matcher):
        self._name = None
        self._matcher = matcher
    
    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        
        return instance.__dict__[self._name]
    
    def __set__(self, instance, value: dict):
        if self._matcher.validate_key(value) is True:
            instance.__dict__[self._name] = self._matcher.take_out_value(value)



def open_client_json_file() -> None:
    json_info = {}
    with open('json_parsing/client_input.json') as json_file:
        json_info = json.load(json_file)
    return json_info

FieldDbInfo = partial(
    ClientAttribute,
    DbMatcher
)

FieldKeyInfo = partial(
    ClientAttribute,
    KeyMatcher
)

class ClientInfo:
    db:DB = ClientAttribute(DbMatcher)
    key:Key = ClientAttribute(KeyMatcher)

    def __init__(self):
        self.json_info = open_client_json_file()
        self.db = self.json_info
        self.key = self.json_info
        

    def look_up_config_keys(self):
        print('현재 Strategy > client_input.json 파일에 있는 key정보입니다:', end= ' ')
        for key in vars(self).keys():
            print(key, end=', ')
        print()

    def print_jsonfile(self):
        print(json.dumps(self.json_info, indent=2))
    

    
    

           

    







        


    


    

    