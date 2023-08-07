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
avg_2021
avg_2022

child=pd.DataFrame()
child=avg_2018
child=pd.merge(child,avg_2019,on='시도',how='outer')
child=pd.merge(child,avg_2021,on='시도',how='outer')
child=pd.merge(child,avg_2022,on='시도',how='outer')
child

import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import font_manager

# with open('avg_data.pkl','wb') as file_obg:
#     pickle.dump(child, file_obg)

with open('avg_data.pkl','rb') as file_obg:
    child=pickle.load(file_obg)

# 폰트 설정
font_path = '/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf'  # NanumBarunGothic 폰트 파일 경로
font_prop = font_manager.FontProperties(fname=font_path).get_name()
plt.rcParams['font.family'] = font_prop

child = child[0:17]
filter_child = child.iloc[:,[1,2,3,4]]
years = filter_child.columns
data = filter_child.values
regions = child['시도']

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# 막대 그래프 생성
for i in range(len(years)):
    for j in range(len(data)):
        ax.bar3d(i, j, 0, 0.7, 0.7, data[j][i], alpha=0.8)

# 축 설정
# ax.set_xlabel('년도')
# ax.set_ylabel('지역')
# ax.set_zlabel('사고건수')

# x, y 축 눈금 설정
ax.set_xticks(range(len(years)))
ax.set_yticks(range(len(regions)))
ax.set_xticklabels(years, rotation=10)
ax.set_yticklabels(regions, rotation=-20)

plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)

# 그래프 출력
plt.show()