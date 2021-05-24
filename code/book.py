import sys
from pyLingo import *
def book(s1Discount1,s1Discount2,s2Discount,s3Discount,s4Discount):
    #create Lingo enviroment object
    pEnv = lingo.pyLScreateEnvLng()
    if pEnv is None:
        print("cannot create LINGO environment!")
        exit(1)
    #open LINGO's log file
    name='_'+str(s1Discount1)+'_'+str(s1Discount2)+'_'+str(s2Discount)+'_'+str(s3Discount)+'_'+str(s4Discount)
    cur_name='book'+name+'.log'
    errorcode = lingo.pyLSopenLogFileLng(pEnv,cur_name)
    if errorcode != const.LSERR_NO_ERROR_LNG:
        print("errorcode = ", errorcode)
        exit(1)
    #pass memory transfer pointers to LINGO
    #define pnPointersNow
    pnPointersNow = N.array([0],dtype=N.int32)
    #@POINTER(1)
    s1Discount1_cur = N.array([s1Discount1],dtype=N.double)
    errorcode = lingo.pyLSsetDouPointerLng(pEnv, s1Discount1_cur, pnPointersNow)
    if errorcode != const.LSERR_NO_ERROR_LNG:
        print("errorcode = ", errorcode)
        exit(1)
    #@POINTER(2)
    s1Discount2_cur = N.array([s1Discount2],dtype=N.double)
    errorcode = lingo.pyLSsetDouPointerLng(pEnv, s1Discount2_cur, pnPointersNow)
    if errorcode != const.LSERR_NO_ERROR_LNG:
        print("errorcode = ", errorcode)
        exit(1)
    #@POINTER(3)
    s2Discount_cur = N.array([s2Discount],dtype=N.double)
    errorcode = lingo.pyLSsetDouPointerLng(pEnv, s2Discount_cur, pnPointersNow)
    if errorcode != const.LSERR_NO_ERROR_LNG:
        print("errorcode = ", errorcode)
        exit(1)
    #@POINTER(4)
    s3Discount_cur = N.array([s3Discount],dtype=N.double)
    errorcode = lingo.pyLSsetDouPointerLng(pEnv, s3Discount_cur, pnPointersNow)
    if errorcode != const.LSERR_NO_ERROR_LNG:
        print("errorcode = ", errorcode)
        exit(1)    
    #@POINTER(5)
    s4Discount_cur = N.array([s4Discount],dtype=N.double)
    errorcode = lingo.pyLSsetDouPointerLng(pEnv, s4Discount_cur, pnPointersNow)
    if errorcode != const.LSERR_NO_ERROR_LNG:
        print("errorcode = ", errorcode)
        exit(1)    
    #@POINTER(6)
    Status = N.array([-1.0],dtype=N.double)
    errorcode = lingo.pyLSsetDouPointerLng(pEnv, Status, pnPointersNow)
    if errorcode != const.LSERR_NO_ERROR_LNG:
        print("errorcode = ", errorcode)
        exit(1)        
    #Run the script
    cScript = "SET ECHOIN 1 \n TAKE book.lng \n GO \n QUIT \n"
    errorcode = lingo.pyLSexecuteScriptLng(pEnv, cScript)
    if errorcode != const.LSERR_NO_ERROR_LNG:
        print("errorcode = ", errorcode)
        exit(1)
    #Close the log file
    errorcode = lingo.pyLScloseLogFileLng(pEnv)
    if errorcode != const.LSERR_NO_ERROR_LNG:
        print("errorcode = ", errorcode)
        exit(1)     
    if Status[0] == const.LS_STATUS_GLOBAL_LNG:
        print("\nGlobal optimum found!")
    elif Status[0] == const.LS_STATUS_LOCAL_LNG:
        print("\nLocal optimum found!")
    else:
        print("\nSolution is non-optimal\n")    
    #delete Lingo enviroment object
    errorcode = lingo.pyLSdeleteEnvLng(pEnv)
    if errorcode != const.LSERR_NO_ERROR_LNG:
        exit(1) 
        
if __name__ == '__main__':
    rate=[0.1,0.2,0.3,0.4,0.5]
    discount_float_2=[18,21,24] #s2店铺浮动折扣
    discount_float_3=[0.88,0.85,0.82,0.79,0.76,0.73]  #s3店铺浮动折扣
    boundary_4=[125,118,113,105] #s4边界浮动
    for i in discount_float_2:
        for j in discount_float_3:
            for k in boundary_4:
                book(16,40,i,j,k)
                sys.stdin.read(1)
      
    
    
    
    
    
    
    
    
    
    