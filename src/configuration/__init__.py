import argparse

space = 3

parser = argparse.ArgumentParser()
parser.add_argument("--input_file", help="input file path", required=True)
parser.add_argument("--output_file", help="output file path", default='media/output.xlsx')
args = parser.parse_args()

merge_format_ = {'align': 'center', 'valign': 'vcenter', 'border': 2}
