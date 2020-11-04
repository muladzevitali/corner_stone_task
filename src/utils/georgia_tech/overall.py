__author__ = 'Vitali Muladze'

import pandas

from src.utils.operations import divide


def form_first_table(data):
    first_table = []
    heart_filter = (data['PlateLocHeight'] > 1.83) & (data['PlateLocHeight'] <= 3.16) & (
            data['PlateLocSide'] >= -0.55) & (data['PlateLocSide'] <= 0.55)
    gt_heart_filter = (data['Batter'] == 'Compton, Drew') & heart_filter
    bip_only = data[gt_heart_filter & (data['PitchCall'] == 'InPlay')].shape[0]
    b1 = data[gt_heart_filter & (data['PlayResult'] == 'Single')].shape[0]
    b2 = data[gt_heart_filter & (data['PlayResult'] == 'Double')].shape[0]
    b3 = data[gt_heart_filter & (data['PlayResult'] == 'Triple')].shape[0]
    hr = data[gt_heart_filter & (data['PlayResult'] == 'HomeRun')].shape[0]

    wOBAcon = divide(b1 * 0.94 + b2 * 1.34 + b3 * 1.67 + hr * 2.08, bip_only)
    wRC = ((((wOBAcon - 0.363) / 1.194) + (0.146)) * bip_only)
    Hard_Hit = data[gt_heart_filter & (data['ExitSpeed'] >= 85)].shape[0]
    HH = divide(Hard_Hit, bip_only)
    Line_drive = data[gt_heart_filter & (data['Angle'] >= 10) & (data['Angle'] <= 25)].shape[0]
    LD = divide(Line_drive, bip_only)
    row = [bip_only, b1, b2, b3, hr, wOBAcon, wRC, Hard_Hit, HH, Line_drive, LD]
    first_table.append(row)

    shadow_s_filter = (data['PlateLocHeight'] <= 1.82) & (data['PlateLocHeight'] >= 1.16) & (
            data['PlateLocSide'] >= -1.1) & (data['PlateLocSide'] <= 1.1)
    gt_shadow_s_filter = (data['Batter'] == 'Compton, Drew') & shadow_s_filter

    bip_only = data[gt_shadow_s_filter & (data['PitchCall'] == 'InPlay')].shape[0]
    b1 = data[gt_shadow_s_filter & (data['PlayResult'] == 'Single')].shape[0]
    b2 = data[gt_shadow_s_filter & (data['PlayResult'] == 'Double')].shape[0]
    b3 = data[gt_shadow_s_filter & (data['PlayResult'] == 'Triple')].shape[0]
    hr = data[gt_shadow_s_filter & (data['PlayResult'] == 'HomeRun')].shape[0]

    wOBAcon = divide(b1 * 0.94 + b2 * 1.34 + b3 * 1.67 + hr * 2.08, bip_only)
    wRC = ((((wOBAcon - 0.363) / 1.194) + (0.146)) * bip_only)
    Hard_Hit = data[gt_shadow_s_filter & (data['ExitSpeed'] >= 85)].shape[0]
    HH = divide(Hard_Hit, bip_only)
    Line_drive = data[gt_shadow_s_filter & (data['Angle'] >= 10) & (data['Angle'] <= 25)].shape[0]
    LD = divide(Line_drive, bip_only)
    row = [bip_only, b1, b2, b3, hr, wOBAcon, wRC, Hard_Hit, HH, Line_drive, LD]
    first_table.append(row)

    shadow_w_filter = (data['PlateLocHeight'] <= 3.16) & (data['PlateLocHeight'] >= 1.83) & (
            data['PlateLocSide'] >= -1.1) & (data['PlateLocSide'] <= -0.56)
    gt_heart_filter = (data['Batter'] == 'Compton, Drew') & shadow_w_filter

    bip_only = data[gt_heart_filter & (data['PitchCall'] == 'InPlay')].shape[0]
    b1 = data[gt_heart_filter & (data['PlayResult'] == 'Single')].shape[0]
    b2 = data[gt_heart_filter & (data['PlayResult'] == 'Double')].shape[0]
    b3 = data[gt_heart_filter & (data['PlayResult'] == 'Triple')].shape[0]
    hr = data[gt_heart_filter & (data['PlayResult'] == 'HomeRun')].shape[0]

    wOBAcon = divide(b1 * 0.94 + b2 * 1.34 + b3 * 1.67 + hr * 2.08, bip_only)
    wRC = ((((wOBAcon - 0.363) / 1.194) + (0.146)) * bip_only)
    Hard_Hit = data[gt_heart_filter & (data['ExitSpeed'] >= 85)].shape[0]
    HH = divide(Hard_Hit, bip_only)
    Line_drive = data[gt_heart_filter & (data['Angle'] >= 10) & (data['Angle'] <= 25)].shape[0]
    LD = divide(Line_drive, bip_only)
    row = [bip_only, b1, b2, b3, hr, wOBAcon, wRC, Hard_Hit, HH, Line_drive, LD]
    first_table.append(row)

    shadow_n_filter = (data['PlateLocHeight'] <= 3.83) & (data['PlateLocHeight'] >= 3.17) & (
            data['PlateLocSide'] >= -1.1) & (data['PlateLocSide'] <= 1.1)
    gt_heart_filter = (data['Batter'] == 'Compton, Drew') & shadow_n_filter

    bip_only = data[gt_heart_filter & (data['PitchCall'] == 'InPlay')].shape[0]
    b1 = data[gt_heart_filter & (data['PlayResult'] == 'Single')].shape[0]
    b2 = data[gt_heart_filter & (data['PlayResult'] == 'Double')].shape[0]
    b3 = data[gt_heart_filter & (data['PlayResult'] == 'Triple')].shape[0]
    hr = data[gt_heart_filter & (data['PlayResult'] == 'HomeRun')].shape[0]

    wOBAcon = divide(b1 * 0.94 + b2 * 1.34 + b3 * 1.67 + hr * 2.08, bip_only)
    wRC = ((((wOBAcon - 0.363) / 1.194) + (0.146)) * bip_only)
    Hard_Hit = data[gt_heart_filter & (data['ExitSpeed'] >= 85)].shape[0]
    HH = divide(Hard_Hit, bip_only)
    Line_drive = data[gt_heart_filter & (data['Angle'] >= 10) & (data['Angle'] <= 25)].shape[0]
    LD = divide(Line_drive, bip_only)
    row = [bip_only, b1, b2, b3, hr, wOBAcon, wRC, Hard_Hit, HH, Line_drive, LD]
    first_table.append(row)

    shadow_e_filter = (data['PlateLocHeight'] <= 3.83) & (data['PlateLocHeight'] >= 1.83) & (
            data['PlateLocSide'] >= 0.56) & (data['PlateLocSide'] <= 1.1)
    gt_heart_filter = (data['Batter'] == 'Compton, Drew') & shadow_e_filter

    bip_only = data[gt_heart_filter & (data['PitchCall'] == 'InPlay')].shape[0]
    b1 = data[gt_heart_filter & (data['PlayResult'] == 'Single')].shape[0]
    b2 = data[gt_heart_filter & (data['PlayResult'] == 'Double')].shape[0]
    b3 = data[gt_heart_filter & (data['PlayResult'] == 'Triple')].shape[0]
    hr = data[gt_heart_filter & (data['PlayResult'] == 'HomeRun')].shape[0]

    wOBAcon = divide(b1 * 0.94 + b2 * 1.34 + b3 * 1.67 + hr * 2.08, bip_only)
    wRC = ((((wOBAcon - 0.363) / 1.194) + (0.146)) * bip_only)
    Hard_Hit = data[gt_heart_filter & (data['ExitSpeed'] >= 85)].shape[0]
    HH = divide(Hard_Hit, bip_only)
    Line_drive = data[gt_heart_filter & (data['Angle'] >= 10) & (data['Angle'] <= 25)].shape[0]
    LD = divide(Line_drive, bip_only)
    row = [bip_only, b1, b2, b3, hr, wOBAcon, wRC, Hard_Hit, HH, Line_drive, LD]
    first_table.append(row)

    chase_s_filter = (data['PlateLocHeight'] <= 1.15)
    gt_chase_s_filter = (data['Batter'] == 'Compton, Drew') & chase_s_filter

    bip_only = data[gt_chase_s_filter & (data['PitchCall'] == 'InPlay')].shape[0]
    b1 = data[gt_chase_s_filter & (data['PlayResult'] == 'Single')].shape[0]
    b2 = data[gt_chase_s_filter & (data['PlayResult'] == 'Double')].shape[0]
    b3 = data[gt_chase_s_filter & (data['PlayResult'] == 'Triple')].shape[0]
    hr = data[gt_chase_s_filter & (data['PlayResult'] == 'HomeRun')].shape[0]

    wOBAcon = divide(b1 * 0.94 + b2 * 1.34 + b3 * 1.67 + hr * 2.08, bip_only)
    wRC = ((((wOBAcon - 0.363) / 1.194) + (0.146)) * bip_only) if bip_only else None
    Hard_Hit = data[gt_chase_s_filter & (data['ExitSpeed'] >= 85)].shape[0]
    HH = divide(Hard_Hit, bip_only)
    Line_drive = data[gt_chase_s_filter & (data['Angle'] >= 10) & (data['Angle'] <= 25)].shape[0]
    LD = divide(Line_drive, bip_only)
    row = [bip_only, b1, b2, b3, hr, wOBAcon, wRC, Hard_Hit, HH, Line_drive, LD]
    first_table.append(row)

    chase_w_filter = (data['PlateLocHeight'] <= 3.83) & (data['PlateLocHeight'] >= 1.16) & (
            data['PlateLocSide'] <= -1.11)
    gt_chase_w_filter = (data['Batter'] == 'Compton, Drew') & chase_w_filter

    bip_only = data[gt_chase_w_filter & (data['PitchCall'] == 'InPlay')].shape[0]
    b1 = data[gt_chase_w_filter & (data['PlayResult'] == 'Single')].shape[0]
    b2 = data[gt_chase_w_filter & (data['PlayResult'] == 'Double')].shape[0]
    b3 = data[gt_chase_w_filter & (data['PlayResult'] == 'Triple')].shape[0]
    hr = data[gt_chase_w_filter & (data['PlayResult'] == 'HomeRun')].shape[0]

    wOBAcon = divide(b1 * 0.94 + b2 * 1.34 + b3 * 1.67 + hr * 2.08, bip_only)
    wRC = ((((wOBAcon - 0.363) / 1.194) + (0.146)) * bip_only) if bip_only else None
    Hard_Hit = data[gt_chase_w_filter & (data['ExitSpeed'] >= 85)].shape[0]
    HH = divide(Hard_Hit, bip_only)
    Line_drive = data[gt_chase_w_filter & (data['Angle'] >= 10) & (data['Angle'] <= 25)].shape[0]
    LD = divide(Line_drive, bip_only)
    row = [bip_only, b1, b2, b3, hr, wOBAcon, wRC, Hard_Hit, HH, Line_drive, LD]
    first_table.append(row)

    chase_n_filter = (data['PlateLocHeight'] >= 3.84)
    gt_chase_n_filter = (data['Batter'] == 'Compton, Drew') & chase_n_filter

    bip_only = data[gt_chase_n_filter & (data['PitchCall'] == 'InPlay')].shape[0]
    b1 = data[gt_chase_n_filter & (data['PlayResult'] == 'Single')].shape[0]
    b2 = data[gt_chase_n_filter & (data['PlayResult'] == 'Double')].shape[0]
    b3 = data[gt_chase_n_filter & (data['PlayResult'] == 'Triple')].shape[0]
    hr = data[gt_chase_n_filter & (data['PlayResult'] == 'HomeRun')].shape[0]

    wOBAcon = divide(b1 * 0.94 + b2 * 1.34 + b3 * 1.67 + hr * 2.08, bip_only)
    wRC = ((((wOBAcon - 0.363) / 1.194) + (0.146)) * bip_only) if bip_only else None
    Hard_Hit = data[gt_chase_n_filter & (data['ExitSpeed'] >= 85)].shape[0]
    HH = divide(Hard_Hit, bip_only)
    Line_drive = data[gt_chase_n_filter & (data['Angle'] >= 10) & (data['Angle'] <= 25)].shape[0]
    LD = divide(Line_drive, bip_only)
    row = [bip_only, b1, b2, b3, hr, wOBAcon, wRC, Hard_Hit, HH, Line_drive, LD]
    first_table.append(row)

    chase_e_filter = (data['PlateLocHeight'] <= 3.83) & (data['PlateLocHeight'] >= 1.16) & (
            data['PlateLocSide'] >= 1.11)
    gt_chase_e_filter = (data['Batter'] == 'Compton, Drew') & chase_e_filter

    bip_only = data[gt_chase_e_filter & (data['PitchCall'] == 'InPlay')].shape[0]
    b1 = data[gt_chase_e_filter & (data['PlayResult'] == 'Single')].shape[0]
    b2 = data[gt_chase_e_filter & (data['PlayResult'] == 'Double')].shape[0]
    b3 = data[gt_chase_e_filter & (data['PlayResult'] == 'Triple')].shape[0]
    hr = data[gt_chase_e_filter & (data['PlayResult'] == 'HomeRun')].shape[0]

    wOBAcon = divide(b1 * 0.94 + b2 * 1.34 + b3 * 1.67 + hr * 2.08, bip_only)
    wRC = ((((wOBAcon - 0.363) / 1.194) + (0.146)) * bip_only) if bip_only else None
    Hard_Hit = data[gt_chase_e_filter & (data['ExitSpeed'] >= 85)].shape[0]
    HH = divide(Hard_Hit, bip_only)
    Line_drive = data[gt_chase_e_filter & (data['Angle'] >= 10) & (data['Angle'] <= 25)].shape[0]
    LD = divide(Line_drive, bip_only)
    row = [bip_only, b1, b2, b3, hr, wOBAcon, wRC, Hard_Hit, HH, Line_drive, LD]
    first_table.append(row)

    first_table_columns = ['BIP Only', '1B', '2B', '3B', 'HR', 'wOBAcon', 'wRC', 'Hard Hit', 'HH%', 'Linedrive', 'LD %']
    first_table_index = ['Heart', 'Shadow S', 'Shadow W', 'Shadow N', 'Shadow E', 'Chase S', 'Chase W', 'Chase N',
                         'Chase E']
    first_data_frame = pandas.DataFrame(first_table, columns=first_table_columns, index=first_table_index)
    first_data_frame = first_data_frame.reset_index()

    tmp = first_data_frame.sum(axis=0)
    tmp['wOBAcon'] = (tmp['1B'] * 0.94 + tmp['2B'] * 1.34 + tmp['3B'] * 1.67 + tmp['HR'] * 2.08) / tmp['BIP Only']
    tmp['wRC'] = (((tmp['wOBAcon'] - 0.363) / 1.194) + (0.146)) * tmp['BIP Only']
    tmp['HH%'] = tmp['Hard Hit'] / tmp['BIP Only']
    tmp['LD %'] = tmp['Linedrive'] / tmp['BIP Only']
    tmp['index'] = 'Total'

    first_data_frame = first_data_frame.append(tmp.T, ignore_index=True)
    first_data_frame = first_data_frame.rename({'index': ''}, axis=1)

    return first_data_frame

