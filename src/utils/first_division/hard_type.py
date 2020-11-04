import pandas

from ..operations import divide


def all_type_div_1(data):
    filter_base = (data['Strikes'] == 0) & (data['TaggedPitchType'] == 'Fastball') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                      data['PlateLocSide'].between(-0.55, 0.55, inclusive=True))
    filter_base = filter_base & (data['Batter'] != 'Compton, Drew')

    filter_1 = filter_base & (data['PitchCall'] == 'FoulBall')
    filter_2 = filter_base & (data['PitchCall'] == 'InPlay')
    filter_3 = filter_base & (data['PitchCall'] == 'StrikeSwinging')
    ok_heart = data[filter_1 | filter_2 | filter_3].shape[0]

    filter_base = (data['Strikes'] == 1) & (data['TaggedPitchType'] == 'Fastball') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                      data['PlateLocSide'].between(-0.55, 0.55, inclusive=True))
    filter_base = filter_base & (data['Batter'] != 'Compton, Drew')

    filter_1 = filter_base & (data['PitchCall'] == 'FoulBall')
    filter_2 = filter_base & (data['PitchCall'] == 'InPlay')
    filter_3 = filter_base & (data['PitchCall'] == 'StrikeSwinging')
    k1_heart = data[filter_1 | filter_2 | filter_3].shape[0]

    filter_base = (data['Strikes'] == 2) & (data['TaggedPitchType'] == 'Fastball') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                      data['PlateLocSide'].between(-0.55, 0.55, inclusive=True))
    filter_base = filter_base & (data['Batter'] != 'Compton, Drew')

    filter_1 = filter_base & (data['PitchCall'] == 'FoulBall')
    filter_2 = filter_base & (data['PitchCall'] == 'InPlay')
    filter_3 = filter_base & (data['PitchCall'] == 'StrikeSwinging')
    k2_heart = data[filter_1 | filter_2 | filter_3].shape[0]

    filter_base = (data['Strikes'] == 0) & (data['TaggedPitchType'] == 'Fastball')
    filter_base = filter_base & (data['Batter'] != 'Compton, Drew')

    filter_1 = filter_base & (data['PitchCall'] == 'FoulBall') & (
        data['PlateLocHeight'].between(3.17, 3.83, inclusive=True)) & (
                   data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_2 = filter_base & (data['PitchCall'] == 'FoulBall') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                   data['PlateLocSide'].between(0.56, 1.1, inclusive=True))
    filter_3 = filter_base & (data['PitchCall'] == 'FoulBall') & (
        data['PlateLocHeight'].between(1.16, 1.82, inclusive=True)) & (
                   data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_4 = filter_base & (data['PitchCall'] == 'FoulBall') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                   data['PlateLocSide'].between(-1.1, -0.56, inclusive=True))

    filter_5 = filter_base & (data['PitchCall'] == 'InPlay') & (
        data['PlateLocHeight'].between(3.17, 3.83, inclusive=True)) & (
                   data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_6 = filter_base & (data['PitchCall'] == 'InPlay') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                   data['PlateLocSide'].between(0.56, 1.1, inclusive=True))
    filter_7 = filter_base & (data['PitchCall'] == 'InPlay') & (
        data['PlateLocHeight'].between(1.16, 1.82, inclusive=True)) & (
                   data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_8 = filter_base & (data['PitchCall'] == 'InPlay') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                   data['PlateLocSide'].between(-1.1, -0.56, inclusive=True))

    filter_9 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (
        data['PlateLocHeight'].between(3.17, 3.83, inclusive=True)) & (
                   data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_10 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                    data['PlateLocSide'].between(0.56, 1.1, inclusive=True))
    filter_11 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (
        data['PlateLocHeight'].between(1.16, 1.82, inclusive=True)) & (
                    data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_12 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                    data['PlateLocSide'].between(-1.1, -0.56, inclusive=True))

    ok_shadow = data[
        filter_1 | filter_2 | filter_3 | filter_4 | filter_5 | filter_6 | filter_7 | filter_8 | filter_9 | filter_10 | filter_11 | filter_12].shape[
        0]

    filter_base = (data['Strikes'] == 1) & (data['TaggedPitchType'] == 'Fastball')
    filter_base = filter_base & (data['Batter'] != 'Compton, Drew')

    filter_1 = filter_base & (data['PitchCall'] == 'FoulBall') & (
        data['PlateLocHeight'].between(3.17, 3.83, inclusive=True)) & (
                   data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_2 = filter_base & (data['PitchCall'] == 'FoulBall') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                   data['PlateLocSide'].between(0.56, 1.1, inclusive=True))
    filter_3 = filter_base & (data['PitchCall'] == 'FoulBall') & (
        data['PlateLocHeight'].between(1.16, 1.82, inclusive=True)) & (
                   data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_4 = filter_base & (data['PitchCall'] == 'FoulBall') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                   data['PlateLocSide'].between(-1.1, -0.56, inclusive=True))

    filter_5 = filter_base & (data['PitchCall'] == 'InPlay') & (
        data['PlateLocHeight'].between(3.17, 3.83, inclusive=True)) & (
                   data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_6 = filter_base & (data['PitchCall'] == 'InPlay') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                   data['PlateLocSide'].between(0.56, 1.1, inclusive=True))
    filter_7 = filter_base & (data['PitchCall'] == 'InPlay') & (
        data['PlateLocHeight'].between(1.16, 1.82, inclusive=True)) & (
                   data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_8 = filter_base & (data['PitchCall'] == 'InPlay') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                   data['PlateLocSide'].between(-1.1, -0.56, inclusive=True))

    filter_9 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (
        data['PlateLocHeight'].between(3.17, 3.83, inclusive=True)) & (
                   data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_10 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                    data['PlateLocSide'].between(0.56, 1.1, inclusive=True))
    filter_11 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (
        data['PlateLocHeight'].between(1.16, 1.82, inclusive=True)) & (
                    data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_12 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                    data['PlateLocSide'].between(-1.1, -0.56, inclusive=True))

    k1_shadow = data[
        filter_1 | filter_2 | filter_3 | filter_4 | filter_5 | filter_6 | filter_7 | filter_8 | filter_9 | filter_10 | filter_11 | filter_12].shape[
        0]

    filter_base = (data['Strikes'] == 2) & (data['TaggedPitchType'] == 'Fastball')
    filter_base = filter_base & (data['Batter'] != 'Compton, Drew')

    filter_1 = filter_base & (data['PitchCall'] == 'FoulBall') & (
        data['PlateLocHeight'].between(3.17, 3.83, inclusive=True)) & (
                   data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_2 = filter_base & (data['PitchCall'] == 'FoulBall') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                   data['PlateLocSide'].between(0.56, 1.1, inclusive=True))
    filter_3 = filter_base & (data['PitchCall'] == 'FoulBall') & (
        data['PlateLocHeight'].between(1.16, 1.82, inclusive=True)) & (
                   data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_4 = filter_base & (data['PitchCall'] == 'FoulBall') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                   data['PlateLocSide'].between(-1.1, -0.56, inclusive=True))

    filter_5 = filter_base & (data['PitchCall'] == 'InPlay') & (
        data['PlateLocHeight'].between(3.17, 3.83, inclusive=True)) & (
                   data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_6 = filter_base & (data['PitchCall'] == 'InPlay') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                   data['PlateLocSide'].between(0.56, 1.1, inclusive=True))
    filter_7 = filter_base & (data['PitchCall'] == 'InPlay') & (
        data['PlateLocHeight'].between(1.16, 1.82, inclusive=True)) & (
                   data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_8 = filter_base & (data['PitchCall'] == 'InPlay') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                   data['PlateLocSide'].between(-1.1, -0.56, inclusive=True))

    filter_9 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (
        data['PlateLocHeight'].between(3.17, 3.83, inclusive=True)) & (
                   data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_10 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                    data['PlateLocSide'].between(0.56, 1.1, inclusive=True))
    filter_11 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (
        data['PlateLocHeight'].between(1.16, 1.82, inclusive=True)) & (
                    data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_12 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                    data['PlateLocSide'].between(-1.1, -0.56, inclusive=True))

    k2_shadow = data[
        filter_1 | filter_2 | filter_3 | filter_4 | filter_5 | filter_6 | filter_7 | filter_8 | filter_9 | filter_10 | filter_11 | filter_12].shape[
        0]

    filter_base = (data['Strikes'] == 0) & (data['TaggedPitchType'] == 'Fastball')
    filter_base = filter_base & (data['Batter'] != 'Compton, Drew')

    filter_1 = filter_base & (data['PitchCall'] == 'FoulBall') & (data['PlateLocHeight'] <= 1.15)
    filter_2 = filter_base & (data['PitchCall'] == 'FoulBall') & (
        data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (data['PlateLocSide'] <= -1.11)
    filter_3 = filter_base & (data['PitchCall'] == 'FoulBall') & (data['PlateLocHeight'] >= 3.84)
    filter_4 = filter_base & (data['PitchCall'] == 'FoulBall') & (
        data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (data['PlateLocSide'] >= 1.11)

    filter_5 = filter_base & (data['PitchCall'] == 'InPlay') & (data['PlateLocHeight'] <= 1.15)
    filter_6 = filter_base & (data['PitchCall'] == 'InPlay') & (
        data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (data['PlateLocSide'] <= -1.11)
    filter_7 = filter_base & (data['PitchCall'] == 'InPlay') & (data['PlateLocHeight'] >= 3.84)
    filter_8 = filter_base & (data['PitchCall'] == 'InPlay') & (
        data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (data['PlateLocSide'] >= 1.11)

    filter_9 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (data['PlateLocHeight'] <= 1.15)
    filter_10 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (
        data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (data['PlateLocSide'] <= -1.11)
    filter_11 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (data['PlateLocHeight'] >= 3.84)
    filter_12 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (
        data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (data['PlateLocSide'] >= 1.11)

    ok_chase = data[
        filter_1 | filter_2 | filter_3 | filter_4 | filter_5 | filter_6 | filter_7 | filter_8 | filter_9 | filter_10 | filter_11 | filter_12].shape[
        0]

    filter_base = (data['Strikes'] == 1) & (data['TaggedPitchType'] == 'Fastball')
    filter_base = filter_base & (data['Batter'] != 'Compton, Drew')

    filter_1 = filter_base & (data['PitchCall'] == 'FoulBall') & (data['PlateLocHeight'] <= 1.15)
    filter_2 = filter_base & (data['PitchCall'] == 'FoulBall') & (
        data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (data['PlateLocSide'] <= -1.11)
    filter_3 = filter_base & (data['PitchCall'] == 'FoulBall') & (data['PlateLocHeight'] >= 3.84)
    filter_4 = filter_base & (data['PitchCall'] == 'FoulBall') & (
        data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (data['PlateLocSide'] >= 1.11)

    filter_5 = filter_base & (data['PitchCall'] == 'InPlay') & (data['PlateLocHeight'] <= 1.15)
    filter_6 = filter_base & (data['PitchCall'] == 'InPlay') & (
        data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (data['PlateLocSide'] <= -1.11)
    filter_7 = filter_base & (data['PitchCall'] == 'InPlay') & (data['PlateLocHeight'] >= 3.84)
    filter_8 = filter_base & (data['PitchCall'] == 'InPlay') & (
        data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (data['PlateLocSide'] >= 1.11)

    filter_9 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (data['PlateLocHeight'] <= 1.15)
    filter_10 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (
        data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (data['PlateLocSide'] <= -1.11)
    filter_11 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (data['PlateLocHeight'] >= 3.84)
    filter_12 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (
        data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (data['PlateLocSide'] >= 1.11)

    k1_chase = data[
        filter_1 | filter_2 | filter_3 | filter_4 | filter_5 | filter_6 | filter_7 | filter_8 | filter_9 | filter_10 | filter_11 | filter_12].shape[
        0]

    filter_base = (data['Strikes'] == 2) & (data['TaggedPitchType'] == 'Fastball')
    filter_base = filter_base & (data['Batter'] == 'Compton, Drew')

    filter_1 = filter_base & (data['PitchCall'] == 'FoulBall') & (data['PlateLocHeight'] <= 1.15)
    filter_2 = filter_base & (data['PitchCall'] == 'FoulBall') & (
        data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (data['PlateLocSide'] <= -1.11)
    filter_3 = filter_base & (data['PitchCall'] == 'FoulBall') & (data['PlateLocHeight'] >= 3.84)
    filter_4 = filter_base & (data['PitchCall'] == 'FoulBall') & (
        data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (data['PlateLocSide'] >= 1.11)

    filter_5 = filter_base & (data['PitchCall'] == 'InPlay') & (data['PlateLocHeight'] <= 1.15)
    filter_6 = filter_base & (data['PitchCall'] == 'InPlay') & (
        data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (data['PlateLocSide'] <= -1.11)
    filter_7 = filter_base & (data['PitchCall'] == 'InPlay') & (data['PlateLocHeight'] >= 3.84)
    filter_8 = filter_base & (data['PitchCall'] == 'InPlay') & (
        data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (data['PlateLocSide'] >= 1.11)

    filter_9 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (data['PlateLocHeight'] <= 1.15)
    filter_10 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (
        data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (data['PlateLocSide'] <= -1.11)
    filter_11 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (data['PlateLocHeight'] >= 3.84)
    filter_12 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (
        data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (data['PlateLocSide'] >= 1.11)

    k2_chase = data[
        filter_1 | filter_2 | filter_3 | filter_4 | filter_5 | filter_6 | filter_7 | filter_8 | filter_9 | filter_10 | filter_11 | filter_12].shape[
        0]

    hard_swing = ['Swing', ok_heart, k1_heart, k2_heart, ok_shadow, k1_shadow, k2_shadow, ok_chase, k1_chase, k2_chase]

    filter_base = (data['Strikes'] == 0) & (data['TaggedPitchType'] == 'Fastball') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                      data['PlateLocSide'].between(-0.55, 0.55, inclusive=True))
    filter_base = filter_base & (data['Batter'] != 'Compton, Drew')

    ok_heart = data[filter_base].shape[0]

    filter_base = (data['Strikes'] == 1) & (data['TaggedPitchType'] == 'Fastball') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                      data['PlateLocSide'].between(-0.55, 0.55, inclusive=True))
    filter_base = filter_base & (data['Batter'] != 'Compton, Drew')
    k1_heart = data[filter_base].shape[0]

    filter_base = (data['Strikes'] == 2) & (data['TaggedPitchType'] == 'Fastball') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                      data['PlateLocSide'].between(-0.55, 0.55, inclusive=True))
    filter_base = filter_base & (data['Batter'] != 'Compton, Drew')
    k2_heart = data[filter_base].shape[0]

    filter_base = (data['Strikes'] == 0) & (data['TaggedPitchType'] == 'Fastball')
    filter_base = filter_base & (data['Batter'] != 'Compton, Drew')

    filter_1 = filter_base & (data['PlateLocHeight'].between(3.17, 3.83, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_2 = filter_base & (data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
        data['PlateLocSide'].between(0.56, 1.1, inclusive=True))
    filter_3 = filter_base & (data['PlateLocHeight'].between(1.16, 1.82, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_4 = filter_base & (data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, -0.56, inclusive=True))

    ok_shadow = data[filter_1 | filter_2 | filter_3 | filter_4].shape[0]

    filter_base = (data['Strikes'] == 1) & (data['TaggedPitchType'] == 'Fastball')
    filter_base = filter_base & (data['Batter'] != 'Compton, Drew')

    filter_1 = filter_base & (data['PlateLocHeight'].between(3.17, 3.83, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_2 = filter_base & (data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
        data['PlateLocSide'].between(0.56, 1.1, inclusive=True))
    filter_3 = filter_base & (data['PlateLocHeight'].between(1.16, 1.82, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_4 = filter_base & (data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, -0.56, inclusive=True))

    k1_shadow = data[filter_1 | filter_2 | filter_3 | filter_4].shape[0]

    filter_base = (data['Strikes'] == 2) & (data['TaggedPitchType'] == 'Fastball')
    filter_base = filter_base & (data['Batter'] != 'Compton, Drew')

    filter_1 = filter_base & (data['PlateLocHeight'].between(3.17, 3.83, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_2 = filter_base & (data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
        data['PlateLocSide'].between(0.56, 1.1, inclusive=True))
    filter_3 = filter_base & (data['PlateLocHeight'].between(1.16, 1.82, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_4 = filter_base & (data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, -0.56, inclusive=True))

    k2_shadow = data[filter_1 | filter_2 | filter_3 | filter_4].shape[0]

    filter_base = (data['Strikes'] == 0) & (data['TaggedPitchType'] == 'Fastball')
    filter_base = filter_base & (data['Batter'] != 'Compton, Drew')

    filter_1 = filter_base & (data['PlateLocHeight'] <= 1.15)
    filter_2 = filter_base & (data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (
            data['PlateLocSide'] <= -1.11)
    filter_3 = filter_base & (data['PlateLocHeight'] >= 3.84)
    filter_4 = filter_base & (data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (
            data['PlateLocSide'] >= 1.11)

    ok_chase = data[filter_1 | filter_2 | filter_3 | filter_4].shape[0]

    filter_base = (data['Strikes'] == 1) & (data['TaggedPitchType'] == 'Fastball')
    filter_base = filter_base & (data['Batter'] != 'Compton, Drew')

    filter_1 = filter_base & (data['PlateLocHeight'] <= 1.15)
    filter_2 = filter_base & (data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (
            data['PlateLocSide'] <= -1.11)
    filter_3 = filter_base & (data['PlateLocHeight'] >= 3.84)
    filter_4 = filter_base & (data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (
            data['PlateLocSide'] >= 1.11)

    k1_chase = data[filter_1 | filter_2 | filter_3 | filter_4].shape[0]

    filter_base = (data['Strikes'] == 2) & (data['TaggedPitchType'] == 'Fastball')
    filter_base = filter_base & (data['Batter'] != 'Compton, Drew')

    filter_1 = filter_base & (data['PlateLocHeight'] <= 1.15)
    filter_2 = filter_base & (data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (
            data['PlateLocSide'] <= -1.11)
    filter_3 = filter_base & (data['PlateLocHeight'] >= 3.84)
    filter_4 = filter_base & (data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (
            data['PlateLocSide'] >= 1.11)

    k2_chase = data[filter_1 | filter_2 | filter_3 | filter_4].shape[0]

    total_hard = ['Total', ok_heart, k1_heart, k2_heart, ok_shadow, k1_shadow, k2_shadow, ok_chase, k1_chase, k2_chase]

    percent_hard = [divide(a, b) for a, b in zip(hard_swing, total_hard) if isinstance(a, int)]
    percent_hard = ['Swing %'] + percent_hard

    column_names = ['Hard', '0K Heart', '1K Heart', '2K Heart', '0K Shadow', '1K Shadow', '2K Shadow', '0K Chase',
                    '1K Chase', '2K Chase']
    hard_gt_data = pandas.DataFrame([hard_swing, percent_hard, total_hard], columns=column_names)

    filter_base = (data['Strikes'] == 0) & (data['TaggedPitchType'] != 'Fastball') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                      data['PlateLocSide'].between(-0.55, 0.55, inclusive=True))
    filter_base = filter_base & (data['Batter'] != 'Compton, Drew')

    filter_1 = filter_base & (data['PitchCall'] == 'FoulBall')
    filter_2 = filter_base & (data['PitchCall'] == 'InPlay')
    filter_3 = filter_base & (data['PitchCall'] == 'StrikeSwinging')
    ok_heart = data[filter_1 | filter_2 | filter_3].shape[0]

    filter_base = (data['Strikes'] == 1) & (data['TaggedPitchType'] != 'Fastball') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                      data['PlateLocSide'].between(-0.55, 0.55, inclusive=True))
    filter_base = filter_base & (data['Batter'] != 'Compton, Drew')

    filter_1 = filter_base & (data['PitchCall'] == 'FoulBall')
    filter_2 = filter_base & (data['PitchCall'] == 'InPlay')
    filter_3 = filter_base & (data['PitchCall'] == 'StrikeSwinging')
    k1_heart = data[filter_1 | filter_2 | filter_3].shape[0]

    filter_base = (data['Strikes'] == 2) & (data['TaggedPitchType'] != 'Fastball') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                      data['PlateLocSide'].between(-0.55, 0.55, inclusive=True))
    filter_base = filter_base & (data['Batter'] != 'Compton, Drew')

    filter_1 = filter_base & (data['PitchCall'] == 'FoulBall')
    filter_2 = filter_base & (data['PitchCall'] == 'InPlay')
    filter_3 = filter_base & (data['PitchCall'] == 'StrikeSwinging')
    k2_heart = data[filter_1 | filter_2 | filter_3].shape[0]

    filter_base = (data['Strikes'] == 0) & (data['TaggedPitchType'] != 'Fastball')
    filter_base = filter_base & (data['Batter'] != 'Compton, Drew')

    filter_1 = filter_base & (data['PitchCall'] == 'FoulBall') & (
        data['PlateLocHeight'].between(3.17, 3.83, inclusive=True)) & (
                   data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_2 = filter_base & (data['PitchCall'] == 'FoulBall') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                   data['PlateLocSide'].between(0.56, 1.1, inclusive=True))
    filter_3 = filter_base & (data['PitchCall'] == 'FoulBall') & (
        data['PlateLocHeight'].between(1.16, 1.82, inclusive=True)) & (
                   data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_4 = filter_base & (data['PitchCall'] == 'FoulBall') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                   data['PlateLocSide'].between(-1.1, -0.56, inclusive=True))

    filter_5 = filter_base & (data['PitchCall'] == 'InPlay') & (
        data['PlateLocHeight'].between(3.17, 3.83, inclusive=True)) & (
                   data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_6 = filter_base & (data['PitchCall'] == 'InPlay') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                   data['PlateLocSide'].between(0.56, 1.1, inclusive=True))
    filter_7 = filter_base & (data['PitchCall'] == 'InPlay') & (
        data['PlateLocHeight'].between(1.16, 1.82, inclusive=True)) & (
                   data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_8 = filter_base & (data['PitchCall'] == 'InPlay') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                   data['PlateLocSide'].between(-1.1, -0.56, inclusive=True))

    filter_9 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (
        data['PlateLocHeight'].between(3.17, 3.83, inclusive=True)) & (
                   data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_10 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                    data['PlateLocSide'].between(0.56, 1.1, inclusive=True))
    filter_11 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (
        data['PlateLocHeight'].between(1.16, 1.82, inclusive=True)) & (
                    data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_12 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                    data['PlateLocSide'].between(-1.1, -0.56, inclusive=True))

    ok_shadow = data[
        filter_1 | filter_2 | filter_3 | filter_4 | filter_5 | filter_6 | filter_7 | filter_8 | filter_9 | filter_10 | filter_11 | filter_12].shape[
        0]

    filter_base = (data['Strikes'] == 1) & (data['TaggedPitchType'] != 'Fastball')
    filter_base = filter_base & (data['Batter'] != 'Compton, Drew')

    filter_1 = filter_base & (data['PitchCall'] == 'FoulBall') & (
        data['PlateLocHeight'].between(3.17, 3.83, inclusive=True)) & (
                   data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_2 = filter_base & (data['PitchCall'] == 'FoulBall') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                   data['PlateLocSide'].between(0.56, 1.1, inclusive=True))
    filter_3 = filter_base & (data['PitchCall'] == 'FoulBall') & (
        data['PlateLocHeight'].between(1.16, 1.82, inclusive=True)) & (
                   data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_4 = filter_base & (data['PitchCall'] == 'FoulBall') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                   data['PlateLocSide'].between(-1.1, -0.56, inclusive=True))

    filter_5 = filter_base & (data['PitchCall'] == 'InPlay') & (
        data['PlateLocHeight'].between(3.17, 3.83, inclusive=True)) & (
                   data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_6 = filter_base & (data['PitchCall'] == 'InPlay') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                   data['PlateLocSide'].between(0.56, 1.1, inclusive=True))
    filter_7 = filter_base & (data['PitchCall'] == 'InPlay') & (
        data['PlateLocHeight'].between(1.16, 1.82, inclusive=True)) & (
                   data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_8 = filter_base & (data['PitchCall'] == 'InPlay') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                   data['PlateLocSide'].between(-1.1, -0.56, inclusive=True))

    filter_9 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (
        data['PlateLocHeight'].between(3.17, 3.83, inclusive=True)) & (
                   data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_10 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                    data['PlateLocSide'].between(0.56, 1.1, inclusive=True))
    filter_11 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (
        data['PlateLocHeight'].between(1.16, 1.82, inclusive=True)) & (
                    data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_12 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                    data['PlateLocSide'].between(-1.1, -0.56, inclusive=True))

    k1_shadow = data[
        filter_1 | filter_2 | filter_3 | filter_4 | filter_5 | filter_6 | filter_7 | filter_8 | filter_9 | filter_10 | filter_11 | filter_12].shape[
        0]

    filter_base = (data['Strikes'] == 2) & (data['TaggedPitchType'] != 'Fastball')
    filter_base = filter_base & (data['Batter'] != 'Compton, Drew')

    filter_1 = filter_base & (data['PitchCall'] == 'FoulBall') & (
        data['PlateLocHeight'].between(3.17, 3.83, inclusive=True)) & (
                   data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_2 = filter_base & (data['PitchCall'] == 'FoulBall') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                   data['PlateLocSide'].between(0.56, 1.1, inclusive=True))
    filter_3 = filter_base & (data['PitchCall'] == 'FoulBall') & (
        data['PlateLocHeight'].between(1.16, 1.82, inclusive=True)) & (
                   data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_4 = filter_base & (data['PitchCall'] == 'FoulBall') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                   data['PlateLocSide'].between(-1.1, -0.56, inclusive=True))

    filter_5 = filter_base & (data['PitchCall'] == 'InPlay') & (
        data['PlateLocHeight'].between(3.17, 3.83, inclusive=True)) & (
                   data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_6 = filter_base & (data['PitchCall'] == 'InPlay') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                   data['PlateLocSide'].between(0.56, 1.1, inclusive=True))
    filter_7 = filter_base & (data['PitchCall'] == 'InPlay') & (
        data['PlateLocHeight'].between(1.16, 1.82, inclusive=True)) & (
                   data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_8 = filter_base & (data['PitchCall'] == 'InPlay') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                   data['PlateLocSide'].between(-1.1, -0.56, inclusive=True))

    filter_9 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (
        data['PlateLocHeight'].between(3.17, 3.83, inclusive=True)) & (
                   data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_10 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                    data['PlateLocSide'].between(0.56, 1.1, inclusive=True))
    filter_11 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (
        data['PlateLocHeight'].between(1.16, 1.82, inclusive=True)) & (
                    data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_12 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                    data['PlateLocSide'].between(-1.1, -0.56, inclusive=True))

    k2_shadow = data[
        filter_1 | filter_2 | filter_3 | filter_4 | filter_5 | filter_6 | filter_7 | filter_8 | filter_9 | filter_10 | filter_11 | filter_12].shape[
        0]

    filter_base = (data['Strikes'] == 0) & (data['TaggedPitchType'] != 'Fastball')
    filter_base = filter_base & (data['Batter'] != 'Compton, Drew')

    filter_1 = filter_base & (data['PitchCall'] == 'FoulBall') & (data['PlateLocHeight'] <= 1.15)
    filter_2 = filter_base & (data['PitchCall'] == 'FoulBall') & (
        data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (data['PlateLocSide'] <= -1.11)
    filter_3 = filter_base & (data['PitchCall'] == 'FoulBall') & (data['PlateLocHeight'] >= 3.84)
    filter_4 = filter_base & (data['PitchCall'] == 'FoulBall') & (
        data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (data['PlateLocSide'] >= 1.11)

    filter_5 = filter_base & (data['PitchCall'] == 'InPlay') & (data['PlateLocHeight'] <= 1.15)
    filter_6 = filter_base & (data['PitchCall'] == 'InPlay') & (
        data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (data['PlateLocSide'] <= -1.11)
    filter_7 = filter_base & (data['PitchCall'] == 'InPlay') & (data['PlateLocHeight'] >= 3.84)
    filter_8 = filter_base & (data['PitchCall'] == 'InPlay') & (
        data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (data['PlateLocSide'] >= 1.11)

    filter_9 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (data['PlateLocHeight'] <= 1.15)
    filter_10 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (
        data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (data['PlateLocSide'] <= -1.11)
    filter_11 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (data['PlateLocHeight'] >= 3.84)
    filter_12 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (
        data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (data['PlateLocSide'] >= 1.11)

    ok_chase = data[
        filter_1 | filter_2 | filter_3 | filter_4 | filter_5 | filter_6 | filter_7 | filter_8 | filter_9 | filter_10 | filter_11 | filter_12].shape[
        0]

    filter_base = (data['Strikes'] == 1) & (data['TaggedPitchType'] != 'Fastball')
    filter_base = filter_base & (data['Batter'] != 'Compton, Drew')

    filter_1 = filter_base & (data['PitchCall'] == 'FoulBall') & (data['PlateLocHeight'] <= 1.15)
    filter_2 = filter_base & (data['PitchCall'] == 'FoulBall') & (
        data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (data['PlateLocSide'] <= -1.11)
    filter_3 = filter_base & (data['PitchCall'] == 'FoulBall') & (data['PlateLocHeight'] >= 3.84)
    filter_4 = filter_base & (data['PitchCall'] == 'FoulBall') & (
        data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (data['PlateLocSide'] >= 1.11)

    filter_5 = filter_base & (data['PitchCall'] == 'InPlay') & (data['PlateLocHeight'] <= 1.15)
    filter_6 = filter_base & (data['PitchCall'] == 'InPlay') & (
        data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (data['PlateLocSide'] <= -1.11)
    filter_7 = filter_base & (data['PitchCall'] == 'InPlay') & (data['PlateLocHeight'] >= 3.84)
    filter_8 = filter_base & (data['PitchCall'] == 'InPlay') & (
        data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (data['PlateLocSide'] >= 1.11)

    filter_9 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (data['PlateLocHeight'] <= 1.15)
    filter_10 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (
        data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (data['PlateLocSide'] <= -1.11)
    filter_11 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (data['PlateLocHeight'] >= 3.84)
    filter_12 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (
        data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (data['PlateLocSide'] >= 1.11)

    k1_chase = data[
        filter_1 | filter_2 | filter_3 | filter_4 | filter_5 | filter_6 | filter_7 | filter_8 | filter_9 | filter_10 | filter_11 | filter_12].shape[
        0]

    filter_base = (data['Strikes'] == 2) & (data['TaggedPitchType'] != 'Fastball')
    filter_base = filter_base & (data['Batter'] != 'Compton, Drew')

    filter_1 = filter_base & (data['PitchCall'] == 'FoulBall') & (data['PlateLocHeight'] <= 1.15)
    filter_2 = filter_base & (data['PitchCall'] == 'FoulBall') & (
        data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (data['PlateLocSide'] <= -1.11)
    filter_3 = filter_base & (data['PitchCall'] == 'FoulBall') & (data['PlateLocHeight'] >= 3.84)
    filter_4 = filter_base & (data['PitchCall'] == 'FoulBall') & (
        data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (data['PlateLocSide'] >= 1.11)

    filter_5 = filter_base & (data['PitchCall'] == 'InPlay') & (data['PlateLocHeight'] <= 1.15)
    filter_6 = filter_base & (data['PitchCall'] == 'InPlay') & (
        data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (data['PlateLocSide'] <= -1.11)
    filter_7 = filter_base & (data['PitchCall'] == 'InPlay') & (data['PlateLocHeight'] >= 3.84)
    filter_8 = filter_base & (data['PitchCall'] == 'InPlay') & (
        data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (data['PlateLocSide'] >= 1.11)

    filter_9 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (data['PlateLocHeight'] <= 1.15)
    filter_10 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (
        data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (data['PlateLocSide'] <= -1.11)
    filter_11 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (data['PlateLocHeight'] >= 3.84)
    filter_12 = filter_base & (data['PitchCall'] == 'StrikeSwinging') & (
        data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (data['PlateLocSide'] >= 1.11)

    k2_chase = data[
        filter_1 | filter_2 | filter_3 | filter_4 | filter_5 | filter_6 | filter_7 | filter_8 | filter_9 | filter_10 | filter_11 | filter_12].shape[
        0]

    off_speed_swing = ['Swing', ok_heart, k1_heart, k2_heart, ok_shadow, k1_shadow, k2_shadow, ok_chase, k1_chase,
                       k2_chase]

    filter_base = (data['Strikes'] == 0) & (data['TaggedPitchType'] != 'Fastball') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                      data['PlateLocSide'].between(-0.55, 0.55, inclusive=True))
    filter_base = filter_base & (data['Batter'] != 'Compton, Drew')

    ok_heart = data[filter_base].shape[0]

    filter_base = (data['Strikes'] == 1) & (data['TaggedPitchType'] != 'Fastball') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                      data['PlateLocSide'].between(-0.55, 0.55, inclusive=True))
    filter_base = filter_base & (data['Batter'] != 'Compton, Drew')
    k1_heart = data[filter_base].shape[0]

    filter_base = (data['Strikes'] == 2) & (data['TaggedPitchType'] != 'Fastball') & (
        data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
                      data['PlateLocSide'].between(-0.55, 0.55, inclusive=True))
    filter_base = filter_base & (data['Batter'] != 'Compton, Drew')
    k2_heart = data[filter_base].shape[0]

    filter_base = (data['Strikes'] == 0) & (data['TaggedPitchType'] != 'Fastball')
    filter_base = filter_base & (data['Batter'] != 'Compton, Drew')

    filter_1 = filter_base & (data['PlateLocHeight'].between(3.17, 3.83, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_2 = filter_base & (data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
        data['PlateLocSide'].between(0.56, 1.1, inclusive=True))
    filter_3 = filter_base & (data['PlateLocHeight'].between(1.16, 1.82, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_4 = filter_base & (data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, -0.56, inclusive=True))

    ok_shadow = data[filter_1 | filter_2 | filter_3 | filter_4].shape[0]

    filter_base = (data['Strikes'] == 1) & (data['TaggedPitchType'] != 'Fastball')
    filter_base = filter_base & (data['Batter'] != 'Compton, Drew')

    filter_1 = filter_base & (data['PlateLocHeight'].between(3.17, 3.83, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_2 = filter_base & (data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
        data['PlateLocSide'].between(0.56, 1.1, inclusive=True))
    filter_3 = filter_base & (data['PlateLocHeight'].between(1.16, 1.82, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_4 = filter_base & (data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, -0.56, inclusive=True))

    k1_shadow = data[filter_1 | filter_2 | filter_3 | filter_4].shape[0]

    filter_base = (data['Strikes'] == 2) & (data['TaggedPitchType'] != 'Fastball')
    filter_base = filter_base & (data['Batter'] != 'Compton, Drew')

    filter_1 = filter_base & (data['PlateLocHeight'].between(3.17, 3.83, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_2 = filter_base & (data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
        data['PlateLocSide'].between(0.56, 1.1, inclusive=True))
    filter_3 = filter_base & (data['PlateLocHeight'].between(1.16, 1.82, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, 1.1, inclusive=True))
    filter_4 = filter_base & (data['PlateLocHeight'].between(1.83, 3.16, inclusive=True)) & (
        data['PlateLocSide'].between(-1.1, -0.56, inclusive=True))

    k2_shadow = data[filter_1 | filter_2 | filter_3 | filter_4].shape[0]

    filter_base = (data['Strikes'] == 0) & (data['TaggedPitchType'] != 'Fastball')
    filter_base = filter_base & (data['Batter'] != 'Compton, Drew')

    filter_1 = filter_base & (data['PlateLocHeight'] <= 1.15)
    filter_2 = filter_base & (data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (
            data['PlateLocSide'] <= -1.11)
    filter_3 = filter_base & (data['PlateLocHeight'] >= 3.84)
    filter_4 = filter_base & (data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (
            data['PlateLocSide'] >= 1.11)

    ok_chase = data[filter_1 | filter_2 | filter_3 | filter_4].shape[0]

    filter_base = (data['Strikes'] == 1) & (data['TaggedPitchType'] != 'Fastball')
    filter_base = filter_base & (data['Batter'] != 'Compton, Drew')

    filter_1 = filter_base & (data['PlateLocHeight'] <= 1.15)
    filter_2 = filter_base & (data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (
            data['PlateLocSide'] <= -1.11)
    filter_3 = filter_base & (data['PlateLocHeight'] >= 3.84)
    filter_4 = filter_base & (data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (
            data['PlateLocSide'] >= 1.11)

    k1_chase = data[filter_1 | filter_2 | filter_3 | filter_4].shape[0]

    filter_base = (data['Strikes'] == 2) & (data['TaggedPitchType'] != 'Fastball')
    filter_base = filter_base & (data['Batter'] != 'Compton, Drew')

    filter_1 = filter_base & (data['PlateLocHeight'] <= 1.15)
    filter_2 = filter_base & (data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (
            data['PlateLocSide'] <= -1.11)
    filter_3 = filter_base & (data['PlateLocHeight'] >= 3.84)
    filter_4 = filter_base & (data['PlateLocHeight'].between(1.16, 3.83, inclusive=True)) & (
            data['PlateLocSide'] >= 1.11)

    k2_chase = data[filter_1 | filter_2 | filter_3 | filter_4].shape[0]

    off_speed_total = ['Total', ok_heart, k1_heart, k2_heart, ok_shadow, k1_shadow, k2_shadow, ok_chase, k1_chase,
                       k2_chase]

    percent_hard = [divide(a, b) for a, b in zip(hard_swing, total_hard) if isinstance(a, int)]
    percent_hard = ['Swing %'] + percent_hard

    column_names = ['Offspeed', '0K Heart', '1K Heart', '2K Heart', '0K Shadow', '1K Shadow', '2K Shadow', '0K Chase',
                    '1K Chase', '2K Chase']
    off_speed_gt_data = pandas.DataFrame([off_speed_swing, percent_hard, off_speed_total], columns=column_names)

    swings = [a + b for a, b in zip(hard_swing, off_speed_swing) if isinstance(a, int)]
    totals = [a + b for a, b in zip(total_hard, off_speed_total) if isinstance(a, int)]
    percent_total = [divide(a, b) for a, b in zip(swings, totals) if isinstance(a, int)]

    swings = ['Swing'] + swings
    totals = ['Total'] + totals
    percents = ['Swing %'] + percent_total

    column_names = ['All P Types', '0K Heart', '1K Heart', '2K Heart', '0K Shadow', '1K Shadow', '2K Shadow', '0K Chase',
                    '1K Chase', '2K Chase']
    all_type = pandas.DataFrame([swings, percents, totals], columns=column_names)

    return all_type, hard_gt_data, off_speed_gt_data
