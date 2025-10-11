import  openpyxl
import  pytest

workbook = None

def setup_function():
    global  workbook
    workbook = openpyxl.load_workbook("practicefile_2.xlsx")

def teardown_function():
    global workbook
    workbook.close()
    workbook = None

@pytest.fixture
def sheet_data():
    my_sheet = workbook.active
    data_sheet = []
    for row in my_sheet.iter_rows(values_only=True):
        data_sheet.append(row)
    return data_sheet

def test_multiply(sheet_data):

    for row in sheet_data:
        var1 = row[0]
        var2 = row[1]
        print(f"mult result {var1} * {var2} = {var1 * var2}")


def test_add(sheet_data):
    for row in sheet_data:
        var1 = row[0]
        var2 = row[1]
        print(f"add result {var1} + {var2} = {var1 + var2}")




