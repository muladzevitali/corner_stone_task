# Cornerstone 
> Test task from cornerstone

# Installation
* Install python >= 3.8
* Install dependencies
```bash
pip install -r requirements.txt
```

# Usage
* To get statistics on your file you should run
```bash
python main.py --input_file <file_path>
```
Output will be saved in media/output.xlsx file
* To get statistics on your file and save in custom output file you should run 
```bash
python main.py --input_file <input_file_path> --ouput_file <out_file_path>
```

## Issues
* The table starting from A32 has problems with column indexing, i.e B33 and C33 has different columns. This is the common problem in the tables below this one
* H26 column is missing  <>"Fastball". There is written ="Fastball". That is also common problem
