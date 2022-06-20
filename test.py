# import os
# import pymysql
# import pandas as pd
import pymysql
db = pymysql.connect(host='localhost', user='root',password='root', database='gobang',   charset = 'gbk')

try:

    cursor = db.cursor()
    date=cursor.execute('SELECT * FROM `users` ')
    print(cursor.fetchall())
    # print(date)
    cursor.close()
except pymysql.Error as e:
    print(e)
finally:
    if db:
        db.close()
# # 读取数据1
# os.getcwd()
# os.chdir('E:/')
# db = pymysql.connect('localhost', 'root', '123456', 'tipdm', charset='gbk')
# # host: 这个是ip地址，因为我这里是本地的，所以填127.0.0.1，也可以填localhost。
# # user：用户名，如果你也是本地的，就填root好了
# # passwd：这个是密码
# # db：这个是数据库名
# # port：这个是端口，本地的一般都是3306
# # charset：这个是编码方式，要和你数据库的编码方式一致，要不会连接失败
# data = pd.read_sql('select * from all_gzdata', con=db)
# db.close()  # 关闭连接
# # 读取数据2
# try:
#     db = pymysql.connect('localhost', 'root', '123456', 'tipdm', charset='gbk')
#     cursor = db.cursor()  # 光标
#     # 这个是执行sql语句，返回的是影响的条数
#     data = cursor.execute('SELECT * FROM `all_gzdata`')
#     print(cursor.fetchone())
#     print(data)
#     cursor.close()  # 关闭光标
# except pymysql.Error as e:
#     print(e)
#     print('操作数据库失败')
# finally:  # 如果连接成功就要关闭数据库
#     if db:
#         db.close()
#
# print(cursor.description)
# new = dict(zip([x[0] for x in cursor.description], [x for x in cursor.fetchone()]))
# print(new)
# print(new['title'])
#
#
# # 上面的只是一条数据的，如果是多条，就需要用到map函数
# def new2dict(new):
#     return dict(zip([x[0] for x in cursor.description], [x for x in new]))
#
#
# news_list = list(map(new2dict, cursor.fetchall()))
# print(news_list)