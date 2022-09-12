import sys

import cymysql


class mysqlDB:

    def __init__(self, host, user, password, db, port, charset='utf8'):
        self.host = host
        self.user = user

        self.password = password
        self.db = db
        self.port = port
        self.chartset = charset

    def _getConnect(self):
        try:
            self.conn = cymysql.connect(host=self.host,
                                        user=self.user,
                                        passwd=self.password,
                                        db=self.db,
                                        port=self.port,
                                        charset=self.chartset)
            cur = self.conn.cursor()
        except Exception, ex:
            print 'MySQL connecting error,reason is:' + str(ex[1])
            sys.exit()
        return cur

    def ExecQuery(self, sql):
        cur = self._getConnect()
        try:
            cur.execute(sql)
            rows = cur.fetchall()
        except pyodbc.Error, ex:
            print 'MySQL.Error :%s \ns' % (str(ex[0]), str(ex[1]))
            sys.exit()
            cur.close()
            self.conn.close()
        return rows

    def ExecNoQuery(self, sql):
        cur = self._getConnect()
        try:
            cur.execute(sql)
            self.conn.commit()
        except pyodbc.Error, ex:
            print 'MySQL.Error :%s %s' % (str(ex[0]), str(ex[1]))
            sys.exit()
            cur.close()
            self.conn.close()

    def testMysql():
        mysql = mysqlDB('127.0.0.1', 'root', 'xxx722123', 'test', 3306)
        sql = 'select * from newcq limit 0,10;'
        rows = mysql.ExecQuery(sql)
        for row in rows:
            print row[0], row[1], row[2], row[3]
