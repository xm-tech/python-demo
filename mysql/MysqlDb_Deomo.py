#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

with open('db.json', 'r') as cnf:
    dbconf = json.load(cnf)
    print("host=%s,user=%s,port=%s,pwd=%s,db=%s" %
          (dbconf['host'], dbconf['user'], dbconf['port'], dbconf['password'],
           dbconf['database']))

    # 打开数据库连接
    db = MySQLdb.connect(dbconf['host'],
                         dbconf['user'],
                         dbconf['port'],
                         dbconf['password'],
                         charset='utf8')

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    try:
        # SQL 查询语句
        sql = "select `FId`,`FName`,`FType` from t_skin_config where fid=10000"
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            fid = row[0]
            fname = row[1]
            ftype = row[2]
            # 打印结果
            print("fid=%s,fname=%s,ftype=%s" % (fname, fname, ftype))
    except:
        print("Error: unable to fecth data")

        # 关闭数据库连接
        db.close()
