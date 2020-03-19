"""Defining all horizontal, sagittal, and coronal contours and 10XX systems."""
# Copyright (c) 2018, Stefan Appelhoff
# BSD-3-Clause

# For horizontal and sagittal contours note the variable name to know
# from where the contour starts, over which electrode is crosses half-way
# and at which electrode position it ends. We also need the "mid" coronal
# contour to draw the horizontal contours.
horizontal_Fpz_T8_Oz = ['Fpz', 'Fp2h', 'Fp2', 'AFp8', 'AF8', 'AFF8', 'F8',
                        'FFT8', 'FT8', 'FTT8', 'T8', 'TTP8', 'TP8', 'TPP8',
                        'P8', 'PPO8', 'PO8', 'POO8', 'O2', 'O2h', 'Oz']

horizontal_Fpz_T7_Oz = ['Fpz', 'Fp1h', 'Fp1', 'AFp7', 'AF7', 'AFF7', 'F7',
                        'FFT7', 'FT7', 'FTT7', 'T7', 'TTP7', 'TP7', 'TPP7',
                        'P7', 'PPO7', 'PO7', 'POO7', 'O1', 'O1h', 'Oz']

sagittal_Nz_Cz_Iz = ['Nz', 'NFpz', 'Fpz', 'AFpz', 'AFz', 'AFFz',
                     'Fz', 'FFCz', 'FCz', 'FCCz', 'Cz', 'CCPz',
                     'CPz', 'CPPz', 'Pz', 'PPOz', 'POz', 'POOz',
                     'Oz', 'OIz', 'Iz']

coronal_T9_Cz_T10 = ['T9', 'T9h', 'T7', 'T7h', 'C5', 'C5h', 'C3', 'C3h',
                     'C1', 'C1h', 'Cz', 'C2h', 'C2', 'C4h', 'C4', 'C6h',
                     'C6', 'T8h', 'T8', 'T10h', 'T10']

horizontal_Nz_T10_Iz = ['Nz', 'N2h', 'N2', 'AFp10', 'AF10', 'AFF10',
                        'F10', 'FFT10', 'FT10', 'FTT10', 'T10',
                        'TTP10', 'TP10', 'TPP10', 'P10', 'PPO10',
                        'PO10', 'POO10', 'I2', 'I2h', 'Iz']

horizontal_Nz_T9_Iz = ['Nz', 'N1h', 'N1', 'AFp9', 'AF9', 'AFF9',
                       'F9', 'FFT9', 'FT9', 'FTT9', 'T9',
                       'TTP9', 'TP9', 'TPP9', 'P9', 'PPO9',
                       'PO9', 'POO9', 'I1', 'I1h', 'Iz']

horizontal_NFpz_T10h_OIz = ['NFpz', 'NFp2h', 'NFp2', 'AFp10h', 'AF10h',
                            'AFF10h', 'F10h', 'FFT10h', 'FT10h', 'FTT10h',
                            'T10h', 'TTP10h', 'TP10h', 'TPP10h', 'P10h',
                            'PPO10h', 'PO10h', 'POO10h', 'OI2', 'OI2h',
                            'OIz']

horizontal_NFpz_T9h_OIz = ['NFpz', 'NFp1h', 'NFp1', 'AFp9h', 'AF9h',
                           'AFF9h', 'F9h', 'FFT9h', 'FT9h', 'FTT9h',
                           'T9h', 'TTP9h', 'TP9h', 'TPP9h', 'P9h',
                           'PPO9h', 'PO9h', 'POO9h', 'OI1', 'OI1h',
                           'OIz']

# For coronal contours, always going from left to right
# when looking down at the head and nose is pointing forwards
contour_AFp = ['AFp7', 'AFp7h', 'AFp5', 'AFp5h',
               'AFp3', 'AFp3h', 'AFp1', 'AFp1h', 'AFpz', 'AFp2h',
               'AFp2', 'AFp4h', 'AFp4', 'AFp6h', 'AFp6', 'AFp8h',
               'AFp8']

contour_AF = ['AF7', 'AF7h', 'AF5', 'AF5h', 'AF3',
              'AF3h', 'AF1', 'AF1h', 'AFz', 'AF2h', 'AF2', 'AF4h',
              'AF4', 'AF6h', 'AF6', 'AF8h', 'AF8']

contour_AFF = ['AFF7', 'AFF7h', 'AFF5', 'AFF5h',
               'AFF3', 'AFF3h', 'AFF1', 'AFF1h', 'AFFz', 'AFF2h',
               'AFF2', 'AFF4h', 'AFF4', 'AFF6h', 'AFF6', 'AFF8h',
               'AFF8']

contour_F = ['F7', 'F7h', 'F5', 'F5h', 'F3', 'F3h',
             'F1', 'F1h', 'Fz', 'F2h', 'F2', 'F4h', 'F4', 'F6h',
             'F6', 'F8h', 'F8']

contour_FFC = ['FFT7', 'FFT7h', 'FFC5', 'FFC5h',
               'FFC3', 'FFC3h', 'FFC1', 'FFC1h', 'FFCz', 'FFC2h',
               'FFC2', 'FFC4h', 'FFC4', 'FFC6h', 'FFC6', 'FFT8h',
               'FFT8']

contour_FC = ['FT7', 'FT7h', 'FC5', 'FC5h', 'FC3',
              'FC3h', 'FC1', 'FC1h', 'FCz', 'FC2h', 'FC2', 'FC4h',
              'FC4', 'FC6h', 'FC6', 'FT8h', 'FT8']

contour_FCC = ['FTT7', 'FTT7h', 'FCC5', 'FCC5h',
               'FCC3', 'FCC3h', 'FCC1', 'FCC1h', 'FCCz', 'FCC2h',
               'FCC2', 'FCC4h', 'FCC4', 'FCC6h', 'FCC6', 'FTT8h',
               'FTT8']

# contour_C is plotted as "coronal_T9_Cz_T10"

contour_CCP = ['TTP7', 'TTP7h', 'CCP5', 'CCP5h',
               'CCP3', 'CCP3h', 'CCP1', 'CCP1h', 'CCPz', 'CCP2h',
               'CCP2', 'CCP4h', 'CCP4', 'CCP6h', 'CCP6', 'TTP8h',
               'TTP8']

contour_CP = ['TP7', 'TP7h', 'CP5', 'CP5h', 'CP3',
              'CP3h', 'CP1', 'CP1h', 'CPz', 'CP2h', 'CP2', 'CP4h',
              'CP4', 'CP6h', 'CP6', 'TP8h', 'TP8']

contour_CPP = ['TPP7', 'TPP7h', 'CPP5', 'CPP5h',
               'CPP3', 'CPP3h', 'CPP1', 'CPP1h', 'CPPz', 'CPP2h',
               'CPP2', 'CPP4h', 'CPP4', 'CPP6h', 'CPP6', 'TPP8h',
               'TPP8']

contour_P = ['P7', 'P7h', 'P5', 'P5h', 'P3', 'P3h',
             'P1', 'P1h', 'Pz', 'P2h', 'P2', 'P4h', 'P4', 'P6h',
             'P6', 'P8h', 'P8']

contour_PPO = ['PPO7', 'PPO7h', 'PPO5', 'PPO5h',
               'PPO3', 'PPO3h', 'PPO1', 'PPO1h', 'PPOz', 'PPO2h',
               'PPO2', 'PPO4h', 'PPO4', 'PPO6h', 'PPO6', 'PPO8h',
               'PPO8']

contour_PO = ['PO7', 'PO7h', 'PO5', 'PO5h', 'PO3',
              'PO3h', 'PO1', 'PO1h', 'POz', 'PO2h', 'PO2', 'PO4h',
              'PO4', 'PO6h', 'PO6', 'PO8h', 'PO8']

contour_POO = ['POO7', 'POO7h', 'POO5', 'POO5h',
               'POO3', 'POO3h', 'POO1', 'POO1h', 'POOz', 'POO2h',
               'POO2', 'POO4h', 'POO4', 'POO6h', 'POO6', 'POO8h',
               'POO8']

# List of lists. Note the specific ordering.
all_contours = [sagittal_Nz_Cz_Iz,
                horizontal_Nz_T10_Iz, horizontal_Nz_T9_Iz,
                coronal_T9_Cz_T10,
                horizontal_NFpz_T10h_OIz, horizontal_NFpz_T9h_OIz,
                horizontal_Fpz_T8_Oz, horizontal_Fpz_T7_Oz,
                contour_AFp, contour_AF, contour_AFF, contour_F,
                contour_FFC, contour_FC, contour_FCC, contour_CCP,
                contour_CP, contour_CPP, contour_P, contour_PPO,
                contour_PO, contour_POO]

# Defining which electrodes belong into which standard system
system1020 = ['Fp1', 'Fpz', 'Fp2', 'F7', 'F3', 'Fz', 'F4', 'F8',
              'T7', 'C3', 'Cz', 'C4', 'T8', 'P7', 'P3', 'Pz', 'P4', 'P8',
              'O1', 'Oz', 'O2']

system1010 = system1020 + ['Nz', 'AF7', 'AFz', 'AF8', 'F9', 'F5', 'F1', 'F2',
                           'F6', 'F10', 'FT9', 'FT7', 'FC5', 'FC3', 'FC1',
                           'FCz', 'FC2', 'FC4', 'FC6', 'FT8', 'FT10', 'T9',
                           'C5', 'C1', 'C2', 'C6', 'T10', 'TP7', 'CP5', 'CP3',
                           'CP1', 'CPz', 'CP2', 'CP4', 'CP6', 'TP8', 'P9',
                           'P5', 'P1', 'P2', 'P6', 'P10', 'PO9', 'PO7', 'POz',
                           'PO8', 'PO10', 'I1', 'Iz', 'I2']

system1005 = list(set([label for contour in all_contours
                       for label in contour]))
