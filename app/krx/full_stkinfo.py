import requests
import pandas as pd
from io import BytesIO
def get_krx_code():
    gen_url = 'http://data.krx.co.kr/comm/fileDn/GenerateOTP/generate.cmd'
    gen_parms = {
        'mktId': 'ALL',
        'share': '1',
        'csvxls_isNo': 'false',
        'name': 'fileDown',
        'url': 'dbms/MDC/STAT/standard/MDCSTAT02001' # 전종목 지정내역 generate url
        }
    headers = {
    'Referer': 'http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201020201',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36' #generate.cmd에서 찾아서 입력하세요
    }
    r = requests.get(url=gen_url, params=gen_parms, headers=headers)
    
    down_url = 'http://data.krx.co.kr/comm/fileDn/download_csv/download.cmd'
    data = {
        'code': r.content
    }
    r = requests.post(url=down_url, data=data, headers=headers)
    
    stock_code = pd.read_csv(BytesIO(r.content), encoding='cp949')
    print(stock_code.columns)
    # stock_code = stock_code[['한글 종목약명', '단축코드', '시장구분', '액면가', '상장주식수']]
    # stock_code = stock_code.rename(columns = {'시장구분': 'market', '한글 종목약명': 'name', '단축코드': 'code', 
    #                                           '액면가': 'par_value', '상장주식수': 'total_shrs'})
    
    return stock_code

stkcode = get_krx_code()
# print(stkcode)