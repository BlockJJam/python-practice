from datetime import datetime

import requests
STATUS_ENDPOINT = 'https://reqres.in/api/users'

class BuildStatus:
    @staticmethod
    def build_date() -> str:
        return datetime.utcnow().isoformat()

    @classmethod
    def notify(cls, name: str, job: str):
        build_status = {
            'name' : name,
            'job' : job,
        }
        print(cls.build_date())
        response = requests.post(STATUS_ENDPOINT, json=build_status)
        response.raise_for_status()
        return response
    

