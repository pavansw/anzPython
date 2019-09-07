import xlwt
wb = xlwt.Workbook()
ws = wb.add_sheet("managerData")
ws.write(1,1,"pavan")
wb.save("/root/myworkbook.xls")

