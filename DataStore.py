#coding:utf-8
import xlwt
import datetime

def store_xyhq(dict):
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)
    sheet1.write(0, 0, u'账套编号')
    sheet1.write(0, 1, u'调拨日期')
    sheet1.write(0, 2, u'资金流出科目')
    sheet1.write(0, 3, u'资金流入科目')
    sheet1.write(0, 4, u'调拨金额')
    sheet1.write(0, 5, u'结算费用')
    sheet1.write(0, 6, u'摘要')
    for i in range(0, len(dict['ztbh'])):
        sheet1.write(i + 1, 0, dict['ztbh'][i])
        sheet1.write(i + 1, 1, dict['time'][i])
        sheet1.write(i + 1, 2, dict['liuchu'][i])
        sheet1.write(i + 1, 3, dict['liuru'][i])
        sheet1.write(i + 1, 4, dict['jine'][i])
    f.save('data/Output_File_xyhq' + datetime.datetime.now().strftime('%Y%m%d') + '.xls')
