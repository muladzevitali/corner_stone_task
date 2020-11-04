import pandas

from ..operations import divide


def form_second_table(data):
    second_table = list()
    heart_filter = (data['PlateLocHeight'] > 1.83) & (data['PlateLocHeight'] <= 3.16) & (
            data['PlateLocSide'] >= -0.55) & (data['PlateLocSide'] <= 0.55)
    gt_heart_filter = (data['Batter'] != 'Compton, Drew') & heart_filter
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
    wRC_D1_Avg = divide(wRC, bip_only)

    row = [bip_only, b1, b2, b3, hr, wOBAcon, wRC, Hard_Hit, HH, Line_drive, LD, wRC_D1_Avg]
    second_table.append(row)

    shadow_s_filter = (data['PlateLocHeight'] <= 1.82) & (data['PlateLocHeight'] >= 1.16) & (
            data['PlateLocSide'] >= -1.1) & (data['PlateLocSide'] <= 1.1)
    gt_shadow_s_filter = (data['Batter'] != 'Compton, Drew') & shadow_s_filter

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

    wRC_D1_Avg = divide(wRC, bip_only)
    row = [bip_only, b1, b2, b3, hr, wOBAcon, wRC, Hard_Hit, HH, Line_drive, LD, wRC_D1_Avg]
    second_table.append(row)

    shadow_w_filter = (data['PlateLocHeight'] <= 3.16) & (data['PlateLocHeight'] >= 1.83) & (
            data['PlateLocSide'] >= -1.1) & (data['PlateLocSide'] <= -0.56)
    gt_heart_filter = (data['Batter'] != 'Compton, Drew') & shadow_w_filter

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
    wRC_D1_Avg = divide(wRC, bip_only)
    row = [bip_only, b1, b2, b3, hr, wOBAcon, wRC, Hard_Hit, HH, Line_drive, LD, wRC_D1_Avg]
    second_table.append(row)

    shadow_n_filter = (data['PlateLocHeight'] <= 3.83) & (data['PlateLocHeight'] >= 3.17) & (
            data['PlateLocSide'] >= -1.1) & (data['PlateLocSide'] <= 1.1)
    gt_heart_filter = (data['Batter'] != 'Compton, Drew') & shadow_n_filter

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
    wRC_D1_Avg = divide(wRC, bip_only)
    row = [bip_only, b1, b2, b3, hr, wOBAcon, wRC, Hard_Hit, HH, Line_drive, LD, wRC_D1_Avg]
    second_table.append(row)

    shadow_e_filter = (data['PlateLocHeight'] <= 3.83) & (data['PlateLocHeight'] >= 1.83) & (
            data['PlateLocSide'] >= 0.56) & (data['PlateLocSide'] <= 1.1)
    gt_heart_filter = (data['Batter'] != 'Compton, Drew') & shadow_e_filter

    bip_only = data[gt_heart_filter & (data['PitchCall'] == 'InPlay')].shape[0]
    b1 = data[gt_heart_filter & (data['PlayResult'] == 'Single')].shape[0]
    b2 = data[gt_heart_filter & (data['PlayResult'] == 'Double')].shape[0]
    b3 = data[gt_heart_filter & (data['PlayResult'] == 'Triple')].shape[0]
    hr = data[gt_heart_filter & (data['PlayResult'] == 'HomeRun')].shape[0]

    wOBAcon = divide(b1 * 0.94 + b2 * 1.34 + b3 * 1.67 + hr * 2.08, bip_only)
    wRC = (((wOBAcon - 0.363) / 1.194) + (0.146)) * bip_only
    Hard_Hit = data[gt_heart_filter & (data['ExitSpeed'] >= 85)].shape[0]
    HH = divide(Hard_Hit, bip_only)
    Line_drive = data[gt_heart_filter & (data['Angle'] >= 10) & (data['Angle'] <= 25)].shape[0]
    LD = divide(Line_drive, bip_only)
    wRC_D1_Avg = divide(wRC, bip_only)
    row = [bip_only, b1, b2, b3, hr, wOBAcon, wRC, Hard_Hit, HH, Line_drive, LD, wRC_D1_Avg]
    second_table.append(row)

    chase_s_filter = (data['PlateLocHeight'] <= 1.15)
    gt_chase_s_filter = (data['Batter'] != 'Compton, Drew') & chase_s_filter

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
    wRC_D1_Avg = divide(wRC, bip_only)
    row = [bip_only, b1, b2, b3, hr, wOBAcon, wRC, Hard_Hit, HH, Line_drive, LD, wRC_D1_Avg]
    second_table.append(row)

    chase_w_filter = (data['PlateLocHeight'] <= 3.83) & (data['PlateLocHeight'] >= 1.16) & (
            data['PlateLocSide'] <= -1.11)
    gt_chase_w_filter = (data['Batter'] != 'Compton, Drew') & chase_w_filter

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
    wRC_D1_Avg = divide(wRC, bip_only)
    row = [bip_only, b1, b2, b3, hr, wOBAcon, wRC, Hard_Hit, HH, Line_drive, LD, wRC_D1_Avg]
    second_table.append(row)

    chase_n_filter = (data['PlateLocHeight'] >= 3.84)
    gt_chase_n_filter = (data['Batter'] != 'Compton, Drew') & chase_n_filter

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
    wRC_D1_Avg = divide(wRC, bip_only)
    row = [bip_only, b1, b2, b3, hr, wOBAcon, wRC, Hard_Hit, HH, Line_drive, LD, wRC_D1_Avg]
    second_table.append(row)

    chase_e_filter = (data['PlateLocHeight'] <= 3.83) & (data['PlateLocHeight'] >= 1.16) & (
            data['PlateLocSide'] >= 1.11)
    gt_chase_e_filter = (data['Batter'] != 'Compton, Drew') & chase_e_filter

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
    wRC_D1_Avg = divide(wRC, bip_only)
    row = [bip_only, b1, b2, b3, hr, wOBAcon, wRC, Hard_Hit, HH, Line_drive, LD, wRC_D1_Avg]
    second_table.append(row)

    second_table_columns = ['AB (BIP)', '1B', '2B', '3B', 'HR', 'wOBAcon', 'wRC', 'Hard Hit', 'HH%', 'Linedrive',
                            'LD %', 'wRC D1 Avg']
    second_table_index = ['Heart', 'Shadow S', 'Shadow W', 'Shadow N', 'Shadow E', 'Chase S', 'Chase W', 'Chase N',
                          'Chase E']
    second_data_frame = pandas.DataFrame(second_table, columns=second_table_columns, index=second_table_index)
    second_data_frame = second_data_frame.reset_index()

    tmp = second_data_frame.sum(axis=0)
    tmp['wOBAcon'] = (tmp['1B'] * 0.94 + tmp['2B'] * 1.34 + tmp['3B'] * 1.67 + tmp['HR'] * 2.08) / tmp['AB (BIP)']
    tmp['wRC'] = (((tmp['wOBAcon'] - 0.363) / 1.194) + (0.146)) * tmp['AB (BIP)']
    tmp['HH%'] = tmp['Hard Hit'] / tmp['AB (BIP)']
    tmp['LD %'] = tmp['Linedrive'] / tmp['AB (BIP)']
    tmp['index'] = 'Total'
    second_data_frame = second_data_frame.append(tmp.T, ignore_index=True)
    second_data_frame = second_data_frame.rename({'index': ''}, axis=1)

    return second_data_frame
