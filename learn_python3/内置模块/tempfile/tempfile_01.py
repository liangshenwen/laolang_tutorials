"""
https://docs.python.org/zh-cn/3/library/tempfile.html
"""

import tempfile


fp = tempfile.TemporaryFile()
fp.write(b'Hello world!')

fp.seek(0)
print(fp.read())
print(fp.name)


fp.close()


with tempfile.TemporaryFile() as fp:
    fp.write(b'Hello world!')
    fp.seek(0)
    print(fp.read())
    print(fp.name)




with tempfile.TemporaryDirectory() as tmpdirname:
    print('created temporary directory', tmpdirname)