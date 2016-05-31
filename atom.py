'''import numpy as np
a = np.array([1,2,3,4,5])
print(a)'''
import pymysql
def access_mysql():

    conn = pymysql.connect(host='localhost', port=3306,user='root',passwd='NmGJWRb9W5J9AFzH',db='client')
    cur = conn.cursor()
    cur.execute("SELECT * FROM dictionarylimit 10")
    for r in cur:
        print("row_number:"+str(cur.rownumber))
        print("id:"+str(r[0])+"key:"+str(r[1])+" mean:"+str(r[2]))
        cur.close()
        conn.close()
if __name__ == '__main__':
    access_mysql()
