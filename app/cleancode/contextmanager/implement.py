# with를 활용한 객체의 로직 전후 프로세스를 핸들링 가능하도록
# setting 1처럼, 제네레이터 + @contextlib.contextmanager활용
# setting 2처럼, contextlib.ContextDecorator를 상속받는 클래스로, 메서드 호출만으로 만족하도록 구현하는 방식
@contextlib

import contextlib

def stop_database():
    print('systemctl stop postgresql.service')

def start_database():
    print('systemcl start postgresql.service')

def db_backup():
    print('pg_dump database')


# setting 1
@contextlib.contextmanager
def db_handler():
    stop_database()
    yield
    start_database()

# setting 2
class dbhandler_decorator(contextlib.ContextDecorator):
    def __enter__(self):
        stop_database()

    def __exit__(self, ext_type, ex_value, eex_traceback):
        start_database()

@dbhandler_decorator()
def offline_backup():
    print('pg_dump database')

if __name__ == '__main__':
    with db_handler():
        db_backup()
    
    offline_backup()
    print('----------------------------')

    with contextlib.suppress(DataConversionException):
        parse_data(input_json_or_dict)
    
    
        