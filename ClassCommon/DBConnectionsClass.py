from logging import raiseExceptions
import cx_Oracle
import sys
import pandas as pd

cx_Oracle.init_oracle_client(lib_dir=r"C:\Oracle\instantclient_19_14")


class DBConnectionsClass:

    # creamos un nuevo objeto de tipo conexión.
    def NewConnection():

        #archivo_excel = pd.read_excel('C:\Temp\python_oracle\ActiveDataCommon\COMMON\BBDD.xlsx')
        #print(archivo_excel.columns)
        
        host = '10.121.110.50'
        port = '1521'
        SID = 'CRMLBJTX'

        try:
            dns_tns = cx_Oracle.makedsn(
                host,
                port,
                SID,
            )

            conn = cx_Oracle.connect(
                user='LBJ',
                password='PRELBJ',
                dsn=dns_tns
            )
            return conn

        except Exception as e:
            print ("error => ", type(e))
