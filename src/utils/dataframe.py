from typing import Optional

import pandas
import xlrd


def load_data_frame(file_path: str, sheet_name='Exports') -> Optional[pandas.DataFrame]:
    try:
        data = pandas.read_excel(file_path, sheet_name=sheet_name)
        return data
    except (xlrd.biffh.XLRDError, FileNotFoundError) as error:
        print(error)
        return pandas.DataFrame([])
