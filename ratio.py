import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import font_manager

#2018년
months=['01','02','03','04','05','06','07','08','09','10','11','12']
combined_df = pd.DataFrame()
for i in months:
    accident_path=f'project/사고/차종별_교통사고_2018_{i}.xls'
    accident=pd.read_excel(accident_path,skiprows=1)
    accident=accident[(accident['시군구']=='합계') & (accident['사고년도']=='사고건수[건]')] #지역별 사고건수 추출
    accident = accident.drop(columns=['시군구'])  #시군구 열 제외
    accident = accident[['시도','승용차','승합차','화물차','특수차']] #자동차들만추출
    accident=accident.replace('-',0)
    accident['Sum'] = accident[['승용차','승합차','화물차','특수차']].sum(axis=1)
    accident = pd.concat([accident.iloc[1:], accident.iloc[[0]]]).reset_index(drop=True)

    register_path=f'project/등록/차종별_등록량_2018_{i}.xlsx'
    register=pd.read_excel(register_path,header=None)
    register = register.iloc[:,[0,5,9,13,17,21]]
    register = register.drop([0,1,2,4,23,24,25,26,27,28],axis=0)
    register=register.drop(register.index[0])
    register.columns=['시도','승용차','승합차','화물차','특수차','Sum']
    register=register.reset_index(drop=True)

    cols_to_divide = accident.columns[1:]
    df_ratio = accident.copy()
    df_ratio[cols_to_divide] = (accident[cols_to_divide].div(register[cols_to_divide]))
    df_ratio=df_ratio.iloc[:,[0,5]]
    df_ratio.columns=['시도','2018_'+i]

    if combined_df.empty:
        combined_df = df_ratio
    else:
        combined_df = pd.merge(combined_df, df_ratio, on='시도', how='outer')

combined_df['2018_avg']=combined_df.iloc[:,1:].mean(axis=1)
avg_2018=pd.DataFrame()
avg_2018=combined_df.iloc[:,[0,13]]
avg_2018

#2019년
months=['01','02','03','04','05','06','07','08','09','10','11','12']
combined_df = pd.DataFrame()
for i in months:
    accident_path=f'project/사고/차종별_교통사고_2019_{i}.xls'
    accident=pd.read_excel(accident_path,skiprows=1)
    accident=accident[(accident['시군구']=='합계') & (accident['사고년도']=='사고건수[건]')] #지역별 사고건수 추출
    accident = accident.drop(columns=['시군구'])  #시군구 열 제외
    accident = accident[['시도','승용차','승합차','화물차','특수차']] #자동차들만추출
    accident=accident.replace('-',0)
    accident['Sum'] = accident[['승용차','승합차','화물차','특수차']].sum(axis=1)
    accident = pd.concat([accident.iloc[1:], accident.iloc[[0]]]).reset_index(drop=True)

    register_path=f'project/등록/차종별_등록량_2019_{i}.xlsx'
    register=pd.read_excel(register_path,header=None)
    register = register.iloc[:,[0,5,9,13,17,21]]
    register = register.drop([0,1,2,4,23,24,25,26,27,28],axis=0)
    register=register.drop(register.index[0])
    register.columns=['시도','승용차','승합차','화물차','특수차','Sum']
    register=register.reset_index(drop=True)

    cols_to_divide = accident.columns[1:]
    df_ratio = accident.copy()
    df_ratio[cols_to_divide] = (accident[cols_to_divide].div(register[cols_to_divide]))
    df_ratio=df_ratio.iloc[:,[0,5]]
    df_ratio.columns=['시도','2019_'+i]

    if combined_df.empty:
        combined_df = df_ratio
    else:
        combined_df = pd.merge(combined_df, df_ratio, on='시도', how='outer')

combined_df['2019_avg']=combined_df.iloc[:,1:].mean(axis=1)
avg_2019=pd.DataFrame()
avg_2019=combined_df.iloc[:,[0,13]]
avg_2019

#2020년
months=['01','02','03','04','05','06','07','08','09','10','11','12']
combined_df = pd.DataFrame()
for i in months:
    accident_path=f'project/사고/차종별_교통사고_2020_{i}.xls'
    accident=pd.read_excel(accident_path,skiprows=1)
    accident=accident[(accident['시군구']=='합계') & (accident['사고년도']=='사고건수[건]')] #지역별 사고건수 추출
    accident = accident.drop(columns=['시군구'])  #시군구 열 제외
    accident = accident[['시도','승용차','승합차','화물차','특수차']] #자동차들만추출
    accident=accident.replace('-',0)
    accident['Sum'] = accident[['승용차','승합차','화물차','특수차']].sum(axis=1)
    accident = pd.concat([accident.iloc[1:], accident.iloc[[0]]]).reset_index(drop=True)

    register_path=f'project/등록/차종별_등록량_2020_{i}.xlsx'
    register=pd.read_excel(register_path,header=None)
    register = register.iloc[:,[0,5,9,13,17,21]]
    register = register.drop([0,1,2,4,23,24,25,26,27,28],axis=0)
    register=register.drop(register.index[0])
    register.columns=['시도','승용차','승합차','화물차','특수차','Sum']
    register=register.reset_index(drop=True)

    cols_to_divide = accident.columns[1:]
    df_ratio = accident.copy()
    df_ratio[cols_to_divide] = (accident[cols_to_divide].div(register[cols_to_divide]))
    df_ratio=df_ratio.iloc[:,[0,5]]
    df_ratio.columns=['시도','2020_'+i]

    if combined_df.empty:
        combined_df = df_ratio
    else:
        combined_df = pd.merge(combined_df, df_ratio, on='시도', how='outer')

combined_df['2020_avg']=combined_df.iloc[:,1:].mean(axis=1)
avg_2020=pd.DataFrame()
avg_2020=combined_df.iloc[:,[0,13]]
avg_2020

#2021년
months=['01','02','03','04','05','06','07','08','09','10','11','12']
combined_df = pd.DataFrame()
for i in months:
    accident_path=f'project/사고/차종별_교통사고_2021_{i}.xls'
    accident=pd.read_excel(accident_path,skiprows=1)
    accident=accident[(accident['시군구']=='합계') & (accident['사고년도']=='사고건수[건]')] #지역별 사고건수 추출
    accident = accident.drop(columns=['시군구'])  #시군구 열 제외
    accident = accident[['시도','승용차','승합차','화물차','특수차']] #자동차들만추출
    accident=accident.replace('-',0)
    accident['Sum'] = accident[['승용차','승합차','화물차','특수차']].sum(axis=1)
    accident = pd.concat([accident.iloc[1:], accident.iloc[[0]]]).reset_index(drop=True)

    register_path=f'project/등록/차종별_등록량_2021_{i}.xlsx'
    register=pd.read_excel(register_path,header=None)
    register = register.iloc[:,[0,5,9,13,17,21]]
    register = register.drop([0,1,2,4,23,24,25,26,27,28],axis=0)
    register=register.drop(register.index[0])
    register.columns=['시도','승용차','승합차','화물차','특수차','Sum']
    register=register.reset_index(drop=True)

    cols_to_divide = accident.columns[1:]
    df_ratio = accident.copy()
    df_ratio[cols_to_divide] = (accident[cols_to_divide].div(register[cols_to_divide]))
    df_ratio=df_ratio.iloc[:,[0,5]]
    df_ratio.columns=['시도','2021_'+i]

    if combined_df.empty:
        combined_df = df_ratio
    else:
        combined_df = pd.merge(combined_df, df_ratio, on='시도', how='outer')

combined_df['2021_avg']=combined_df.iloc[:,1:].mean(axis=1)
avg_2021=pd.DataFrame()
avg_2021=combined_df.iloc[:,[0,13]]
avg_2021

#2022년
months=['01','02','03','04','05','06','07','08','09','10','11','12']
combined_df = pd.DataFrame()
for i in months:
    accident_path=f'project/사고/차종별_교통사고_2022_{i}.xls'
    accident=pd.read_excel(accident_path,skiprows=1)
    accident=accident[(accident['시군구']=='합계') & (accident['사고년도']=='사고건수[건]')] #지역별 사고건수 추출
    accident = accident.drop(columns=['시군구'])  #시군구 열 제외
    accident = accident[['시도','승용차','승합차','화물차','특수차']] #자동차들만추출
    accident=accident.replace('-',0)
    accident['Sum'] = accident[['승용차','승합차','화물차','특수차']].sum(axis=1)
    accident = pd.concat([accident.iloc[1:], accident.iloc[[0]]]).reset_index(drop=True)

    register_path=f'project/등록/차종별_등록량_2022_{i}.xlsx'
    register=pd.read_excel(register_path,header=None)
    register = register.iloc[:,[0,5,9,13,17,21]]
    register = register.drop([0,1,2,4,23,24,25,26,27,28],axis=0)
    register=register.drop(register.index[0])
    register.columns=['시도','승용차','승합차','화물차','특수차','Sum']
    register=register.reset_index(drop=True)

    cols_to_divide = accident.columns[1:]
    df_ratio = accident.copy()
    df_ratio[cols_to_divide] = (accident[cols_to_divide].div(register[cols_to_divide]))
    df_ratio=df_ratio.iloc[:,[0,5]]
    df_ratio.columns=['시도','2022_'+i]

    if combined_df.empty:
        combined_df = df_ratio
    else:
        combined_df = pd.merge(combined_df, df_ratio, on='시도', how='outer')

combined_df['2022_avg']=combined_df.iloc[:,1:].mean(axis=1)
avg_2022=pd.DataFrame()
avg_2022=combined_df.iloc[:,[0,13]]
avg_2022

#전체
avg_2018
avg_2019
avg_2020
avg_2021
avg_2022

avg=pd.DataFrame()
avg=avg_2018
avg=pd.merge(avg,avg_2019,on='시도',how='outer')
avg=pd.merge(avg,avg_2020,on='시도',how='outer')
avg=pd.merge(avg,avg_2021,on='시도',how='outer')
avg=pd.merge(avg,avg_2022,on='시도',how='outer')
avg