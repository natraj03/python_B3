import openpyxl
import pytest
from string_practice import reverse_str, check_palendrome

file_obj = openpyxl.load_workbook("strings_inputs.xlsx")

@pytest.fixture
def read_fileinput_data():
    active_sheet = file_obj.active
    all_rows = []
    for row in active_sheet.iter_rows(values_only=True):
        if row[2] == True:
            all_rows.append(row)
    return all_rows

def test_validate_xcel(read_fileinput_data):
    for row in read_fileinput_data:
        if row[1] == "REVERSE":
            assert reverse_str(row[0]) == row[3]
        elif row[1] == "PALENDROME":
            print("row[1]",row[1])
            assert check_palendrome(row[0]) == row[3]

        elif row[1] == "Length":
            assert len(str(row[0])) == int(row[3])

        else:
            print(f"{row[1]} dont know what to do")













