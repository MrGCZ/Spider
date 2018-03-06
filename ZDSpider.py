import ZDCatch,interpreter,DataStore

data=ZDCatch.zd_catch()
xieyihuoqi=interpreter.catch_xyhuoqi(data)
DataStore.store_xyhq(xieyihuoqi)

