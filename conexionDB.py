from logging import raiseExceptions
import cx_Oracle
import sys
import ClassCommon.DBConectionsClass


try: 
  
    conn = ClassCommon.DBConectionsClass.DBConectionsClass.NewConnection()
    select = conn.cursor()
    registros =  select.execute('select * from lbj.cam_client_type')

    print("CLITP_OID - CLITP_DESCRIPTION")
    print("-----------------------------")
    for row in registros:
        print(row[0] ," - ", row[1])
        
except Exception as e:
    print ("error => ", type(e))
    
    


