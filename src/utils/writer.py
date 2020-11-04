import pandas
from path import Path

from src.configuration import (merge_format_, space)
from src.utils import (form_first_table, form_second_table, all_type_div_1, all_type_gt,
                       all_type_whiff_gt)


def write_data(data: pandas.DataFrame, output_file_path: Path, sheet_name="Formulas"):
    gt_overall = form_first_table(data)
    div_1_overall = form_second_table(data)
    gt_all_type, gt_hard, gt_off_speed = all_type_gt(data)
    div_1_all_type, div_1_hard, div_1_off_speed = all_type_div_1(data)
    all_type_whiff, hard_whiff, off_speed_whiff = all_type_whiff_gt(data)

    writer = pandas.ExcelWriter(output_file_path, engine='xlsxwriter')
    workbook = writer.book
    gt_overall.to_excel(writer, sheet_name=sheet_name,  startrow=1, startcol=0, index=False)
    div_1_overall.to_excel(writer, sheet_name=sheet_name,  startrow=1, startcol=gt_overall.shape[1] + space,
                           index=False)

    worksheet = writer.sheets['Formulas']

    merge_format = workbook.add_format(merge_format_)
    worksheet.merge_range(0, 0, 0, gt_overall.shape[1] - 1, 'Georgia Tech', merge_format)
    worksheet.merge_range(0, gt_overall.shape[1] + space, 0,
                          div_1_overall.shape[1] + gt_overall.shape[1] + space - 1, 'Division 1', merge_format)

    start_row = gt_overall.shape[0] + 2 * space
    gt_all_type.to_excel(writer, sheet_name=sheet_name,  startrow=start_row, startcol=0, index=False)
    start_row += gt_all_type.shape[0] + space
    gt_hard.to_excel(writer, sheet_name=sheet_name,  startrow=start_row, startcol=0, index=False)
    start_row += gt_hard.shape[0] + space
    gt_off_speed.to_excel(writer, sheet_name=sheet_name,  startrow=start_row, startcol=0, index=False)

    start_row = gt_overall.shape[0] + 2 * space
    start_col = gt_overall.shape[1] + space
    div_1_all_type.to_excel(writer, sheet_name=sheet_name,  startrow=start_row, startcol=start_col, index=False)
    start_row += gt_all_type.shape[0] + space
    div_1_hard.to_excel(writer, sheet_name=sheet_name,  startrow=start_row, startcol=start_col, index=False)
    start_row += gt_hard.shape[0] + space
    div_1_off_speed.to_excel(writer, sheet_name=sheet_name,  startrow=start_row, startcol=start_col, index=False)

    start_row += div_1_off_speed.shape[0] + space
    all_type_whiff.to_excel(writer, sheet_name=sheet_name,  startrow=start_row, startcol=0, index=False)
    start_row += all_type_whiff.shape[0] + space
    hard_whiff.to_excel(writer, sheet_name=sheet_name,  startrow=start_row, startcol=0, index=False)
    start_row += hard_whiff.shape[0] + space
    off_speed_whiff.to_excel(writer, sheet_name=sheet_name,  startrow=start_row, startcol=0, index=False)

    writer.save()
