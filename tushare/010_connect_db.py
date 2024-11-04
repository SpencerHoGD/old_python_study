import psycopg2


def connect_db():
    try:
        conn = psycopg2.connect(database='postgres', user='postgres', 
                                password='394460', host='127.0.0.1', port=5432)
    except Exception as e:
        pass
    else:
        return conn 
    return None

def close_db_connection(conn):
    conn.commit()
    conn.close()
    

if __name__ == "__main__":
    connect_db()
    print('done')