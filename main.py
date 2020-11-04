import sys
from pathlib import Path

from src.configuration import (args)
from src.utils import (load_data_frame, write_data)

if __name__ == '__main__':

    input_file_path = args.input_file
    output_file_path = Path(args.output_file)
    output_file_path.parent.mkdir(exist_ok=True, parents=True)

    data = load_data_frame(args.input_file)
    if not data.shape[0]:
        sys.exit('File not supported: use .xlsx file with Exports sheet in it')

    write_data(data, output_file_path, sheet_name='Formulas')
