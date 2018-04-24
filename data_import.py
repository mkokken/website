# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 12:37:34 2018

@author: nlkokke2
"""

import pandas as pd


#headers = [STN,YYYYMMDD,DDVEC,FHVEC,   FG,  FHX, FHXH,  FHN, FHNH,  FXX, FXXH,   TG,   TN,  TNH,   TX,  TXH, T10N,T10NH,   SQ,   SP,    Q,   DR,   RH,  RHX, RHXH,   PG,   PX,  PXH,   PN,  PNH,  VVN, VVNH,  VVX, VVXH,   NG,   UG,   UX,  UXH,   UN,  UNH, EV24]
def create_dataset(s):
    var = str(s)
    filename = 'dataset_'+var
    data = pd.read_table('KNMI_20180403.txt', delimiter=",", skiprows = 97)
    data.columns = data.columns.str.strip()
    data.rename(columns = {'# STN':'STN'}, inplace=True)
    dataset = data.loc[data.STN ==s]
    
    dataset.to_pickle(filename)
    
                       

#set_209 = data.loc[data.STN == '  209']
#set_249 = data.loc[data.STN ==249]


def data_extract(b):
    import pandas as pd
    length = b*365
    dataset = pd.read_pickle('dataset_249')
#    dataset = data.loc[data.STN ==s]

    sun_e = dataset.reset_index(drop=True).Q
    time  = dataset.reset_index(drop=True).YYYYMMDD
    
    sun_e_list = sun_e.tolist()
    time_list  = time.tolist()
    
    for i in range(len(sun_e_list)):
        sun_e_list[i] = float(sun_e_list[i])
        time_list[i] = float(time_list[i])
    
    return sun_e_list[-length:]
