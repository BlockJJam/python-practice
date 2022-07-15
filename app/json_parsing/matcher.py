from abc import ABCMeta
from json_parsing.parsed_data import DB, Key
from numpy import size

class Matcher(metaclass = ABCMeta):
    @staticmethod
    def validate_key(json_info: dict) -> bool:
        pass
    
    @staticmethod
    def take_out_value(json_info: dict) -> object:
        pass


class DbMatcher(Matcher):
    
    @staticmethod
    def validate_key(json_info: dict) -> bool:
        result = { key:value  for k, v in json_info.items() if k == 'db' for key, value in v.items() if (key == 'url') or (key == 'db_name')}
        if len(result) is 0:
            return False
        return True

    @staticmethod
    def take_out_value(json_info: dict) -> object: 
        db_info = {key: value for k, v in json_info.items() if k == 'db' for key, value in v.items()}
        return DB(url = db_info['url'], db_name= db_info['db_name'])


class KeyMatcher(Matcher):
    
    @staticmethod
    def validate_key( json_info: dict) -> bool:
        result = { key:value for k,v in json_info.items() if k == 'key' for key,value in v.items() if (key == 'appkey') or (key == 'seckey')}
        if len(result) is 0:
            return False
        return True

    @staticmethod
    def take_out_value( json_info: dict) -> object: 
        key_info = { key:value for k,v in json_info.items() if k == 'key' for key,value in v.items()}
        return Key(appkey= key_info['appkey'], seckey= key_info['seckey'])
