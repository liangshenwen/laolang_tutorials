import os
import random
import datetime
import pyhdfs

def mock_pid_list(start: int, end: int) -> list:
    pid_list = []
    for i in range(start, end + 1, 1):
        pid = f'0000000000{i}'
        length = len(pid)
        pid = '0P' + pid[length - 8: length]
        pid_list.append(pid)

    return pid_list

def mock_stock_names(pid_start: int, pid_end: int, output_file: str) -> None:
    stock_dir = os.path.dirname(output_file)
    if not os.path.exists(stock_dir):
        os.makedirs(stock_dir)
    with open(output_file, mode='w', encoding='UTF-8') as f:
        for pid in mock_pid_list(pid_start, pid_end):
            f.write(pid + ',' + 'stock ' + str(int(pid[2:])) +'\n')

def mock_history_prices(pid_start: int, pid_end: int, output_file: str) -> None:
    # 价格的整数部分
    int_price_options = list(range(10, 1001, 5))
    start_date = datetime.date(1990, 1, 1)
    end_date = datetime.date.today()
    price_dir = os.path.dirname(output_file)
    if not os.path.exists(price_dir):
        os.makedirs(price_dir)
    with open(output_file, mode='w', encoding='UTF-8') as f:
        for pid in mock_pid_list(pid_start, pid_end):
            int_price = random.choice(int_price_options)
            price_date = start_date
            pid_history_prices = ''
            while price_date <= end_date:
                # 如果是周一到周五
                if price_date.weekday() not in (5, 6):
                    if random.choice([True, False]):
                        open_price = round(int_price + random.random(), 5)
                    else:
                        open_price = round(int_price - random.random(), 5)

                    if random.choice([True, False]):
                        close_price = round(int_price + random.random(), 5)
                    else:
                        close_price = round(int_price - random.random(), 5)

                    if random.choice([True, False]):
                        bid_price = round(int_price + random.random(), 5)
                    else:
                        bid_price = round(int_price - random.random(), 5)

                    if random.choice([True, False]):
                        ask_price = round(int_price + random.random(), 5)
                    else:
                        ask_price = round(int_price - random.random(), 5)

                    pid_history_prices += f'{pid},{price_date},{open_price},{close_price},{bid_price},{ask_price}\n'

                price_date = price_date + datetime.timedelta(days=1)

            f.write(pid_history_prices)
            print(pid)


if __name__ == '__main__':
    price_file_path = r'D:\laolang_dev\big-data\price_data\input\mock_stock_info.csv'
    # mock_history_prices(151, 222, price_file_path)
    mock_stock_names(1, 10000, price_file_path)
    # hdfs_client = pyhdfs.HdfsClient(hosts='192.168.10.102:9870', user_name='huixue')
    # hdfs_price_dir = '/market_price/'
    # if not hdfs_client.exists(hdfs_price_dir):
    #     hdfs_client.mkdirs('/market_price/')
    # hdfs_price_filepath = hdfs_price_dir + os.path.basename(price_file_path)
    # hdfs_client.copy_from_local(price_file_path, hdfs_price_filepath)
