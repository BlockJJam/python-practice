fd =open(filename)
try:
    process_file(fd)
finally: 
    fd.close()


with open(filename) as fd: # with: context manager로 진입
    process_file(fd)

def stop_database():
    run('systemctl stop postgresql.service')

def start_database():
    run('systemcl start postgresql.service')

class DBHandler:
    def __enter__(self):
        stop_datebase()
        return self
    
    def __exit__(self, exc_type, ex_value, ex_traceback):
        start_database()
    
def db_backup():
    run('pg_dump database')

def main():
    with DBHandler():
        db_backup()


