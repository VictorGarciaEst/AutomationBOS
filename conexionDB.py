from logging import raiseExceptions
import cx_Oracle
import sys
import ClassCommon.DBConnectionsClass


#try: 
  
conn = ClassCommon.DBConnectionsClass.DBConnectionsClass.NewConnection()
select = conn.cursor()
registros =  select.execute('select * from lbj.cam_client_type')

    
print("CLITP_OID - CLITP_DESCRIPTIONs")
print("-----------------------------")
for row in registros:
    print(row[0] ," - ", row[1])
        
#except Exception as e:
#    print ("errors => ", type(e))
    
    


