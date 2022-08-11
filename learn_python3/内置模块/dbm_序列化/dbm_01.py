"""
https://docs.python.org/zh-cn/3/library/dbm.html

dbm 是一种泛用接口，针对各种 DBM 数据库 --- 包括 dbm.gnu 或 dbm.ndbm。 如果未安装这些模块中的任何一种，则将使用 dbm.dumb 模块中慢速但简单的实现。

key和value都必须是字符串类型
"""
import dbm

# Open database, creating it if necessary.
with dbm.open('cache', 'c') as db:
    # Record some values
    db[b'hello'] = b'there'
    db['www.python.org'] = 'Python Website'
    db['www.cnn.com'] = 'Cable News Network'

    # Note that the keys are considered bytes now.
    assert db[b'www.python.org'] == b'Python Website'
    # Notice how the value is now in bytes.
    assert db['www.cnn.com'] == b'Cable News Network'

    # Often-used methods of the dict interface work too.
    print(db.get('python.org', b'not present'))

    # Storing a non-string key or value will raise an exception (most
    # likely a TypeError).
    db['www.yahoo.com'] = 4

# db is automatically closed when leaving the with statement.