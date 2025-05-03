from clickhouse_driver import Client
import logging
logging.basicConfig(level=logging.DEBUG)
client = Client(
    host='192.168.2.42',
    port='8123',
    user='root',
    password='123456',
    database='mt_sms_sit',
    settings={'send_receive_timeout': 300},
    connect_timeout=15
)

client.execute("select * from mt_msg_result where account='M5865357' and ptt_day = '2025-04-15'")

# def test():
#     global client
#     sql = 'show tables'  # show databases;
#     res = client.execute(sql)
#     print(res)
#
#
# if __name__ == '__main__':
#     test()
