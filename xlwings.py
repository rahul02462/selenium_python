import xlwings as xw

def read_excel_data():
    try:
        wb = xw.Book('F:/Python-Learning/example.xlsx')
        sheet = wb.sheets['Sheet1']
        data = sheet.range("A1:C5").value
        wb.close()
        return data
    except Exception as e:
        print("Error occured")
        return None

if __name__ == "__main__":
    excel_data = read_excel_data()
    if excel_data:
        print(excel_data)
    else:
        print("no data")



