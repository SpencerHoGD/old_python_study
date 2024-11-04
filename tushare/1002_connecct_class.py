import psycopg2
import psycopg2.extras


class myPostgreSQL:
    def __init__(self, database='postgres', user='postgres', password='394460', host='127.0.0.1', port='5432'):
        self.database = database
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None

    def _connect(self):
        self.connection = psycopg2.connect(database=self.database, user=self.user, password=self.password,
                                            host=self.host, port=self.port)
        print(f"连接数据库 postgres://{self.host}:{self.port}/{self.database}成功,用户名:{self.user}")

    def connect(self):
        try:
            if self.connection:
                conn_info = self.connection.options
                if conn_info['database'] == self.database and conn_info['user'] == self.user and conn_info[
                    'password'] == self.password and conn_info['host'] == self.host and conn_info['port'] == self.port:
                    print(f"返回已存在的数据库连接 postgres://{self.host}:{self.port}/{self.database}成功,用户名:{self.user}")
                else:
                    self._connect()
            else:
                self._connect()
        except Exception as err:
            print(f"连接数据库 postgres://{self.host}:{self.port}/{self.database}失败,用户名:{self.user},异常信息:{err.args[0]}")
            

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None
            print(f"关闭据库成功")

    def execute_sql(self, sql):  # 数据库操作，无返回值
        """
        数据库操作，无返回值
            :param sql: 数据库插入语句
            :return:
        """
        self.connect()
        try:
            cur = self.connection.cursor()
            cur.execute(sql)
            self.connection.commit()
            print(f"执行sql语句成功:{sql}")
            cur.close()
        except Exception as e:
            print(f"执行sql语句失败:{sql},异常信息:{e.args[0]}")
        finally:
            self.close()

    def execute_sql_list(self, sql):
        """
        数据库查询，返回为列表
            :param sql: 数据库语句
            :return:
        """
        self.connect()
        row = None
        try:
            cur = self.connection.cursor()
            cur.execute(sql)
            row = cur.fetchall()  # all rows in table
            self.connection.commit()
            print(f"执行sql语句成功:{sql}")
            cur.close()
        except Exception as e:
            print(f"执行sql语句失败:{sql},异常信息:{e.args[0]}")
        finally:
            print(f"sql语句执行结果：{str(row)}")
            self.close()
            return row

    def execute_sql_dict(self, sql):
        """
        数据库查询，返回为字典
            :param sql: 数据库语句
            :return:
        """
        self.connect()
        row = None
        try:
            cur = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            cur.execute(sql)
            row = cur.fetchall()  # all rows in table
            self.connection.commit()
            print(f"执行sql语句成功:{sql}")
            cur.close()
        except Exception as e:
            print(f"执行sql语句失败:{sql},异常信息:{e.args[0]}")
        finally:
            print(f"sql语句执行结果：{str(row)}")
            self.close()
            return row



if __name__ == "__main__":
    db = myPostgreSQL()
    db.connect() 
    # db.close()

    QL1 = "select * from hs_const order by ts_code ASC"
    sql = QL1
    # db.execute_sql(sql)
    db.execute_sql_list(sql)
    # db.execute_sql_dict(sql)