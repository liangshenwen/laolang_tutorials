from sqlalchemy import create_engine

from china_stats_data.config import get_db_path


def get_db_engine():
    # echo=Ture----echo默认为False，表示不打印执行的SQL语句等较详细的执行信息，改为Ture表示让其打印。
    # check_same_thread=False----sqlite默认建立的对象只能让建立该对象的线程使用，
    # 而sqlalchemy是多线程的所以我们需要指定check_same_thread=False来让建立的对象任意线程都可使用。
    db_path = get_db_path()
    return create_engine('sqlite:///' + db_path + '?check_same_thread=False&encoding=UTF-8',
                         echo=True)
