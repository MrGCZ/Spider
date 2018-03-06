#coding:utf-8
import re
import datetime

def del_zuofei(list):
    a=list[:]
    pattern = re.compile(u'作废')
    for i in range(len(a) - 1, -1, -1):
        if re.search(pattern, a[i][0]):
            del a[i]
    return a

def catch_xyhuoqi(list):
    excel={'ztbh':[],'time':[],'liuchu':[],'liuru':[],'jine':[],'jiesuanfei':[],'zhaiyao':[]}
    a=del_zuofei(list)
    print u'今日有' + str(len(a))+ u'笔电子指令'
    pattern_zq = re.compile(u'协议活期支取')
    pattern_cf=re.compile(u'协议活期存放')

    for i in range(len(a)-1,-1,-1):
        if re.search(pattern_zq,a[i][1]):
            excel['ztbh'].append('1156')
            excel['time'].append(datetime.datetime.now().strftime('%Y%m%d'))
            excel['liuru'].append('10020101')
            excel['liuchu'].append(xyhq_trans(a[i][3]))
            excel['jine'].append(a[i][4]+u'.00')

    for i in range(len(a)-1,-1,-1):
        if re.search(pattern_cf,a[i][1]):
            excel['ztbh'].append('1156')
            excel['time'].append(datetime.datetime.now().strftime('%Y%m%d'))
            excel['liuru'].append(xyhq_trans(a[i][3]))
            excel['liuchu'].append('10020101')
            excel['jine'].append(a[i][4]+u'.00')
    return excel

def xyhq_trans(xyhq):
    xyhq_dict={
        u'中国建设银行股份有限公司深圳南山支行':'10020509000001',
        u'北京银行深圳分行营业部':'10020507000001',
        u'中国民生银行股份有限公司盐城分行':'10020503000002',
        u'兴业银行股份有限公司常州支行':'10020501000001'
    }
    return xyhq_dict[xyhq]