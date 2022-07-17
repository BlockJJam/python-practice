import json

def open_client_json_file() -> None:
    json_info = {}
    try:
        with open('json_parsing/client_input.json') as json_file:
            json_info = json.load(json_file)
    except json.JSONDecodeError:
        raise ValueError('Strategy > config 파일을 정확히 입력해주세요. ')

    return json_info



    

    

           

    







        


    


    

    