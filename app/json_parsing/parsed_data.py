from dataclasses import dataclass

@dataclass
class DB:
    url: str
    db_name: str

@dataclass
class Key:
    appkey: str
    seckey: str