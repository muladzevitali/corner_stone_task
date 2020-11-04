import pandas

from ..operations import divide


def all_type_whiff_gt(data):
    filter_base = (data['Strikes'] == 0) & (data['PitchCall'] == 'StrikeSwinging') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                      data['PlateLocSide'].between(-0.55, 0.55, inclusive=True))
    filter_base = filter_base & (data['Batter'] == 'Compton, Drew') & (data['TaggedPitchType'] == 'Fastball')

    ok_heart = data[filter_base].shape[0]

    filter_base = (data['Strikes'] == 1) & (data['PitchCall'] == 'StrikeSwinging') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                      data['PlateLocSide'].between(-0.55, 0.55, inclusive=True))
    filter_base = filter_base & (data['Batter'] == 'Compton, Drew') & (data['TaggedPitchType'] == 'Fastball')

    k1_heart = data[filter_base].shape[0]

    filter_base = (data['Strikes'] == 2) & (data['PitchCall'] == 'StrikeSwinging') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                      data['PlateLocSide'].between(-0.55, 0.55, inclusive=True))
    filter_base = filter_base & (data['Batter'] == 'Compton, Drew') & (data['TaggedPitchType'] == 'Fastball')

    k2_heart = data[filter_base].shape[0]

    filter_base = (data['Strikes'] == 0) & (data['PitchCall'] == 'StrikeSwinging')
    filter_base = filter_base & (data['Batter'] == 'Compton, Drew') & (data['TaggedPitchType'] == 'Fastball')
    filter_1 = filter_base & (data['PlateLocHeight'].between(3.17, 3.83, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_2 = filter_base & (data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
        data['PlateLocSide'].between(0.56, 1.1, inclusive=True))
    filter_3 = filter_base & (data['PlateLocHeight'].between(1.16, 1.82, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_4 = filter_base & (data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, -0.56, inclusive=True))

    ok_shadow = data[filter_1 | filter_2 | filter_3 | filter_4].shape[0]

    filter_base = (data['Strikes'] == 1) & (data['PitchCall'] == 'StrikeSwinging')
    filter_base = filter_base & (data['BatterTeam'] == 'GIT_YEL') & (data['TaggedPitchType'] == 'Fastball')
    filter_1 = filter_base & (data['PlateLocHeight'].between(3.17, 3.83, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_2 = filter_base & (data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
        data['PlateLocSide'].between(0.56, 1.1, inclusive=True))
    filter_3 = filter_base & (data['PlateLocHeight'].between(1.16, 1.82, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_4 = filter_base & (data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, -0.56, inclusive=True))

    k1_shadow = data[filter_1 | filter_2 | filter_3 | filter_4].shape[0]

    filter_base = (data['Strikes'] == 2) & (data['PitchCall'] == 'StrikeSwinging')
    filter_base = filter_base & (data['BatterTeam'] == 'GIT_YEL') & (data['TaggedPitchType'] == 'Fastball')
    filter_1 = filter_base & (data['PlateLocHeight'].between(3.17, 3.83, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_2 = filter_base & (data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
        data['PlateLocSide'].between(0.56, 1.1, inclusive=True))
    filter_3 = filter_base & (data['PlateLocHeight'].between(1.16, 1.82, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_4 = filter_base & (data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, -0.56, inclusive=True))

    k2_shadow = data[filter_1 | filter_2 | filter_3 | filter_4].shape[0]

    filter_base = (data['Strikes'] == 0) & (data['PitchCall'] == 'StrikeSwinging')
    filter_base = filter_base & (data['Batter'] == 'Compton, Drew') & (data['TaggedPitchType'] == 'Fastball')
    filter_1 = filter_base & (data['PlateLocHeight'] <= 1.15)
    filter_2 = filter_base & (data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (
            data['PlateLocSide'] <= -1.11)
    filter_3 = filter_base & (data['PlateLocHeight'] >= 3.84) & (
        data['PlateLocSide'].between(-1.1, -0.56, inclusive=True))
    filter_4 = filter_base & (data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (
            data['PlateLocSide'] >= 1.11)

    ok_chase = data[filter_1 | filter_2 | filter_3 | filter_4].shape[0]

    filter_base = (data['Strikes'] == 1) & (data['PitchCall'] == 'StrikeSwinging')
    filter_base = filter_base & (data['BatterTeam'] == 'GIT_YEL') & (data['TaggedPitchType'] == 'Fastball')
    filter_1 = filter_base & (data['PlateLocHeight'] <= 1.15)
    filter_2 = filter_base & (data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (
            data['PlateLocSide'] <= -1.11)
    filter_3 = filter_base & (data['PlateLocHeight'] >= 3.84) & (
        data['PlateLocSide'].between(-1.1, -0.56, inclusive=True))
    filter_4 = filter_base & (data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (
            data['PlateLocSide'] >= 1.11)

    k1_chase = data[filter_1 | filter_2 | filter_3 | filter_4].shape[0]

    filter_base = (data['Strikes'] == 2) & (data['PitchCall'] == 'StrikeSwinging')
    filter_base = filter_base & (data['BatterTeam'] == 'GIT_YEL') & (data['TaggedPitchType'] == 'Fastball')
    filter_1 = filter_base & (data['PlateLocHeight'] <= 1.15)
    filter_2 = filter_base & (data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (
            data['PlateLocSide'] <= -1.11)
    filter_3 = filter_base & (data['PlateLocHeight'] >= 3.84) & (
        data['PlateLocSide'].between(-1.1, -0.56, inclusive=True))
    filter_4 = filter_base & (data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (
            data['PlateLocSide'] >= 1.11)

    k2_chase = data[filter_1 | filter_2 | filter_3 | filter_4].shape[0]
    hard_first_row = [ok_heart, k1_heart, k2_heart, ok_shadow, k1_shadow, k2_shadow, ok_chase, k1_chase, k2_chase]

    filter_base = (data['Strikes'] == 0) & (data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
        data['PlateLocSide'].between(-0.55, 0.55, inclusive=True))
    filter_base = filter_base & (data['Batter'] == 'Compton, Drew') & (data['TaggedPitchType'] == 'Fastball')

    ok_heart = data[filter_base].shape[0]

    filter_base = (data['Strikes'] == 1) & (data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
        data['PlateLocSide'].between(-0.55, 0.55, inclusive=True))
    filter_base = filter_base & (data['Batter'] == 'Compton, Drew') & (data['TaggedPitchType'] == 'Fastball')

    k1_heart = data[filter_base].shape[0]

    filter_base = (data['Strikes'] == 2) & (data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
        data['PlateLocSide'].between(-0.55, 0.55, inclusive=True))
    filter_base = filter_base & (data['Batter'] == 'Compton, Drew') & (data['TaggedPitchType'] == 'Fastball')

    k2_heart = data[filter_base].shape[0]

    filter_base = (data['Strikes'] == 0)
    filter_base = filter_base & (data['Batter'] == 'Compton, Drew') & (data['TaggedPitchType'] == 'Fastball')
    filter_1 = filter_base & (data['PlateLocHeight'].between(3.17, 3.83, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_2 = filter_base & (data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
        data['PlateLocSide'].between(0.56, 1.1, inclusive=True))
    filter_3 = filter_base & (data['PlateLocHeight'].between(1.16, 1.82, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_4 = filter_base & (data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, -0.56, inclusive=True))

    ok_shadow = data[filter_1 | filter_2 | filter_3 | filter_4].shape[0]

    filter_base = (data['Strikes'] == 1)
    filter_base = filter_base & (data['Batter'] == 'Compton, Drew') & (data['TaggedPitchType'] == 'Fastball')
    filter_1 = filter_base & (data['PlateLocHeight'].between(3.17, 3.83, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_2 = filter_base & (data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
        data['PlateLocSide'].between(0.56, 1.1, inclusive=True))
    filter_3 = filter_base & (data['PlateLocHeight'].between(1.16, 1.82, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_4 = filter_base & (data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, -0.56, inclusive=True))

    k1_shadow = data[filter_1 | filter_2 | filter_3 | filter_4].shape[0]

    filter_base = (data['Strikes'] == 2)
    filter_base = filter_base & (data['Batter'] == 'Compton, Drew') & (data['TaggedPitchType'] == 'Fastball')
    filter_1 = filter_base & (data['PlateLocHeight'].between(3.17, 3.83, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_2 = filter_base & (data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
        data['PlateLocSide'].between(0.56, 1.1, inclusive=True))
    filter_3 = filter_base & (data['PlateLocHeight'].between(1.16, 1.82, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_4 = filter_base & (data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, -0.56, inclusive=True))

    k2_shadow = data[filter_1 | filter_2 | filter_3 | filter_4].shape[0]

    filter_base = (data['Strikes'] == 0)
    filter_base = filter_base & (data['Batter'] == 'Compton, Drew') & (data['TaggedPitchType'] == 'Fastball')
    filter_1 = filter_base & (data['PlateLocHeight'] <= 1.15)
    filter_2 = filter_base & (data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (
            data['PlateLocSide'] <= -1.11)
    filter_3 = filter_base & (data['PlateLocHeight'] >= 3.84)
    filter_4 = filter_base & (data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (
            data['PlateLocSide'] >= 1.11)

    ok_chase = data[filter_1 | filter_2 | filter_3 | filter_4].shape[0]

    filter_base = (data['Strikes'] == 1)
    filter_base = filter_base & (data['Batter'] == 'Compton, Drew') & (data['TaggedPitchType'] == 'Fastball')
    filter_1 = filter_base & (data['PlateLocHeight'] <= 1.15)
    filter_2 = filter_base & (data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (
            data['PlateLocSide'] <= -1.11)
    filter_3 = filter_base & (data['PlateLocHeight'] >= 3.84)
    filter_4 = filter_base & (data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (
            data['PlateLocSide'] >= 1.11)

    k1_chase = data[filter_1 | filter_2 | filter_3 | filter_4].shape[0]

    filter_base = (data['Strikes'] == 2)
    filter_base = filter_base & (data['Batter'] == 'Compton, Drew') & (data['TaggedPitchType'] == 'Fastball')
    filter_1 = filter_base & (data['PlateLocHeight'] <= 1.15)
    filter_2 = filter_base & (data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (
            data['PlateLocSide'] <= -1.11)
    filter_3 = filter_base & (data['PlateLocHeight'] >= 3.84)
    filter_4 = filter_base & (data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (
            data['PlateLocSide'] >= 1.11)

    k2_chase = data[filter_1 | filter_2 | filter_3 | filter_4].shape[0]
    hard_third_row = [ok_heart, k1_heart, k2_heart, ok_shadow, k1_shadow, k2_shadow, ok_chase, k1_chase, k2_chase]

    hard_second_row = ['Whiff %'] + [divide(a, b) for a, b in zip(hard_first_row, hard_third_row)]
    hard_first_row = ['Whiff'] + hard_first_row
    hard_third_row = ['Total'] + hard_third_row

    columns = ['Hard', '0K Heart', '1K Heart', '2K Heart', '0K Shadow', '1K Shadow', '2K Shadow', '0K Chase',
               '1K Chase', '2K Chase']

    hard_data = pandas.DataFrame([hard_first_row, hard_second_row, hard_third_row], columns=columns)

    filter_base = (data['Strikes'] == 0) & (data['PitchCall'] == 'StrikeSwinging') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                      data['PlateLocSide'].between(-0.55, 0.55, inclusive=True))
    filter_base = filter_base & (data['Batter'] == 'Compton, Drew') & (data['TaggedPitchType'] != 'Fastball')

    ok_heart = data[filter_base].shape[0]

    filter_base = (data['Strikes'] == 1) & (data['PitchCall'] == 'StrikeSwinging') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                      data['PlateLocSide'].between(-0.55, 0.55, inclusive=True))
    filter_base = filter_base & (data['Batter'] == 'Compton, Drew') & (data['TaggedPitchType'] != 'Fastball')

    k1_heart = data[filter_base].shape[0]

    filter_base = (data['Strikes'] == 2) & (data['PitchCall'] == 'StrikeSwinging') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                      data['PlateLocSide'].between(-0.55, 0.55, inclusive=True))
    filter_base = filter_base & (data['Batter'] == 'Compton, Drew') & (data['TaggedPitchType'] != 'Fastball')

    k2_heart = data[filter_base].shape[0]

    filter_base = (data['Strikes'] == 0) & (data['PitchCall'] == 'StrikeSwinging')
    filter_base = filter_base & (data['Batter'] == 'Compton, Drew') & (data['TaggedPitchType'] == 'Fastball')
    filter_1 = filter_base & (data['PlateLocHeight'].between(3.17, 3.83, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_2 = filter_base & (data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
        data['PlateLocSide'].between(0.56, 1.1, inclusive=True))
    filter_3 = filter_base & (data['PlateLocHeight'].between(1.16, 1.82, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_4 = filter_base & (data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, -0.56, inclusive=True))

    ok_shadow = data[filter_1 | filter_2 | filter_3 | filter_4].shape[0]

    filter_base = (data['Strikes'] == 1) & (data['PitchCall'] == 'StrikeSwinging')
    filter_base = filter_base & (data['BatterTeam'] == 'GIT_YEL') & (data['TaggedPitchType'] != 'Fastball')
    filter_1 = filter_base & (data['PlateLocHeight'].between(3.17, 3.83, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_2 = filter_base & (data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
        data['PlateLocSide'].between(0.56, 1.1, inclusive=True))
    filter_3 = filter_base & (data['PlateLocHeight'].between(1.16, 1.82, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_4 = filter_base & (data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, -0.56, inclusive=True))

    k1_shadow = data[filter_1 | filter_2 | filter_3 | filter_4].shape[0]

    filter_base = (data['Strikes'] == 2) & (data['PitchCall'] == 'StrikeSwinging')
    filter_base = filter_base & (data['BatterTeam'] == 'GIT_YEL') & (data['TaggedPitchType'] != 'Fastball')
    filter_1 = filter_base & (data['PlateLocHeight'].between(3.17, 3.83, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_2 = filter_base & (data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
        data['PlateLocSide'].between(0.56, 1.1, inclusive=True))
    filter_3 = filter_base & (data['PlateLocHeight'].between(1.16, 1.82, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_4 = filter_base & (data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, -0.56, inclusive=True))

    k2_shadow = data[filter_1 | filter_2 | filter_3 | filter_4].shape[0]

    filter_base = (data['Strikes'] == 0) & (data['PitchCall'] == 'StrikeSwinging')
    filter_base = filter_base & (data['Batter'] == 'Compton, Drew') & (data['TaggedPitchType'] != 'Fastball')
    filter_1 = filter_base & (data['PlateLocHeight'] <= 1.15)
    filter_2 = filter_base & (data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (
            data['PlateLocSide'] <= -1.11)
    filter_3 = filter_base & (data['PlateLocHeight'] >= 3.84) & (
        data['PlateLocSide'].between(-1.1, -0.56, inclusive=True))
    filter_4 = filter_base & (data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (
            data['PlateLocSide'] >= 1.11)

    ok_chase = data[filter_1 | filter_2 | filter_3 | filter_4].shape[0]

    filter_base = (data['Strikes'] == 1) & (data['PitchCall'] == 'StrikeSwinging')
    filter_base = filter_base & (data['BatterTeam'] == 'GIT_YEL') & (data['TaggedPitchType'] != 'Fastball')
    filter_1 = filter_base & (data['PlateLocHeight'] <= 1.15)
    filter_2 = filter_base & (data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (
            data['PlateLocSide'] <= -1.11)
    filter_3 = filter_base & (data['PlateLocHeight'] >= 3.84) & (
        data['PlateLocSide'].between(-1.1, -0.56, inclusive=True))
    filter_4 = filter_base & (data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (
            data['PlateLocSide'] >= 1.11)

    k1_chase = data[filter_1 | filter_2 | filter_3 | filter_4].shape[0]

    filter_base = (data['Strikes'] == 2) & (data['PitchCall'] == 'StrikeSwinging')
    filter_base = filter_base & (data['BatterTeam'] == 'GIT_YEL') & (data['TaggedPitchType'] != 'Fastball')
    filter_1 = filter_base & (data['PlateLocHeight'] <= 1.15)
    filter_2 = filter_base & (data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (
            data['PlateLocSide'] <= -1.11)
    filter_3 = filter_base & (data['PlateLocHeight'] >= 3.84) & (
        data['PlateLocSide'].between(-1.1, -0.56, inclusive=True))
    filter_4 = filter_base & (data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (
            data['PlateLocSide'] >= 1.11)

    k2_chase = data[filter_1 | filter_2 | filter_3 | filter_4].shape[0]
    off_first_row = [ok_heart, k1_heart, k2_heart, ok_shadow, k1_shadow, k2_shadow, ok_chase, k1_chase, k2_chase]

    filter_base = (data['Strikes'] == 0) & (data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
        data['PlateLocSide'].between(-0.55, 0.55, inclusive=True))
    filter_base = filter_base & (data['Batter'] == 'Compton, Drew') & (data['TaggedPitchType'] != 'Fastball')

    ok_heart = data[filter_base].shape[0]

    filter_base = (data['Strikes'] == 1) & (data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
        data['PlateLocSide'].between(-0.55, 0.55, inclusive=True))
    filter_base = filter_base & (data['Batter'] == 'Compton, Drew') & (data['TaggedPitchType'] != 'Fastball')

    k1_heart = data[filter_base].shape[0]

    filter_base = (data['Strikes'] == 2) & (data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
        data['PlateLocSide'].between(-0.55, 0.55, inclusive=True))
    filter_base = filter_base & (data['Batter'] == 'Compton, Drew') & (data['TaggedPitchType'] != 'Fastball')

    k2_heart = data[filter_base].shape[0]

    filter_base = (data['Strikes'] == 0)
    filter_base = filter_base & (data['Batter'] == 'Compton, Drew') & (data['TaggedPitchType'] == 'Fastball')
    filter_1 = filter_base & (data['PlateLocHeight'].between(3.17, 3.83, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_2 = filter_base & (data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
        data['PlateLocSide'].between(0.56, 1.1, inclusive=True))
    filter_3 = filter_base & (data['PlateLocHeight'].between(1.16, 1.82, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_4 = filter_base & (data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, -0.56, inclusive=True))

    ok_shadow = data[filter_1 | filter_2 | filter_3 | filter_4].shape[0]

    filter_base = (data['Strikes'] == 1)
    filter_base = filter_base & (data['Batter'] == 'Compton, Drew') & (data['TaggedPitchType'] != 'Fastball')
    filter_1 = filter_base & (data['PlateLocHeight'].between(3.17, 3.83, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_2 = filter_base & (data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
        data['PlateLocSide'].between(0.56, 1.1, inclusive=True))
    filter_3 = filter_base & (data['PlateLocHeight'].between(1.16, 1.82, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_4 = filter_base & (data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, -0.56, inclusive=True))

    k1_shadow = data[filter_1 | filter_2 | filter_3 | filter_4].shape[0]

    filter_base = (data['Strikes'] == 2)
    filter_base = filter_base & (data['Batter'] == 'Compton, Drew') & (data['TaggedPitchType'] != 'Fastball')
    filter_1 = filter_base & (data['PlateLocHeight'].between(3.17, 3.83, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_2 = filter_base & (data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
        data['PlateLocSide'].between(0.56, 1.1, inclusive=True))
    filter_3 = filter_base & (data['PlateLocHeight'].between(1.16, 1.82, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_4 = filter_base & (data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, -0.56, inclusive=True))

    k2_shadow = data[filter_1 | filter_2 | filter_3 | filter_4].shape[0]

    filter_base = (data['Strikes'] == 0)
    filter_base = filter_base & (data['Batter'] == 'Compton, Drew') & (data['TaggedPitchType'] != 'Fastball')
    filter_1 = filter_base & (data['PlateLocHeight'] <= 1.15)
    filter_2 = filter_base & (data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (
            data['PlateLocSide'] <= -1.11)
    filter_3 = filter_base & (data['PlateLocHeight'] >= 3.84)
    filter_4 = filter_base & (data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (
            data['PlateLocSide'] >= 1.11)

    ok_chase = data[filter_1 | filter_2 | filter_3 | filter_4].shape[0]

    filter_base = (data['Strikes'] == 1)
    filter_base = filter_base & (data['Batter'] == 'Compton, Drew') & (data['TaggedPitchType'] != 'Fastball')
    filter_1 = filter_base & (data['PlateLocHeight'] <= 1.15)
    filter_2 = filter_base & (data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (
            data['PlateLocSide'] <= -1.11)
    filter_3 = filter_base & (data['PlateLocHeight'] >= 3.84)
    filter_4 = filter_base & (data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (
            data['PlateLocSide'] >= 1.11)

    k1_chase = data[filter_1 | filter_2 | filter_3 | filter_4].shape[0]

    filter_base = (data['Strikes'] == 2)
    filter_base = filter_base & (data['Batter'] == 'Compton, Drew') & (data['TaggedPitchType'] != 'Fastball')
    filter_1 = filter_base & (data['PlateLocHeight'] <= 1.15)
    filter_2 = filter_base & (data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (
            data['PlateLocSide'] <= -1.11)
    filter_3 = filter_base & (data['PlateLocHeight'] >= 3.84)
    filter_4 = filter_base & (data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (
            data['PlateLocSide'] >= 1.11)

    k2_chase = data[filter_1 | filter_2 | filter_3 | filter_4].shape[0]
    off_third_row = [ok_heart, k1_heart, k2_heart, ok_shadow, k1_shadow, k2_shadow, ok_chase, k1_chase, k2_chase]

    off_second_row = ['Whiff %'] + [divide(a, b) for a, b in zip(off_first_row, off_third_row)]
    off_first_row = ['Whiff'] + off_first_row
    off_third_row = ['Total'] + off_third_row

    columns = ['Offspeed', '0K Heart', '1K Heart', '2K Heart', '0K Shadow', '1K Shadow', '2K Shadow', '0K Chase',
               '1K Chase', '2K Chase']

    off_data = pandas.DataFrame([off_first_row, off_second_row, off_third_row], columns=columns)

    swings = [a + b for a, b in zip(hard_first_row, off_first_row) if isinstance(a, int)]
    totals = [a + b for a, b in zip(hard_third_row, off_third_row) if isinstance(a, int)]
    percent_total = [divide(a, b) for a, b in zip(swings, totals) if isinstance(a, int)]

    swings = ['Whiff'] + swings
    totals = ['Total'] + totals
    percents = ['Whiff %'] + percent_total

    column_names = ['All P Types', '0K Heart', '1K Heart', '2K Heart', '0K Shadow', '1K Shadow', '2K Shadow',
                    '0K Chase', '1K Chase', '2K Chase']
    all_type = pandas.DataFrame([swings, percents, totals], columns=column_names)

    return all_type, hard_data, off_data
