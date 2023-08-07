import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import font_manager


#사고량
accident=pd.read_excel('project/사고/차종별_교통사고_2018_01.xls',skiprows=1)
accident=accident[(accident['시군구']=='합계') & (accident['사고년도']=='사고건수[건]')] #지역별 사고건수 추출
accident = accident.drop(columns=['시군구'])  #시군구 열 제외
accident = accident[['시도','승용차','승합차','화물차','특수차']] #자동차들만추출
accident=accident.replace('-',0)
accident['Sum'] = accident[['승용차','승합차','화물차','특수차']].sum(axis=1)
accident = pd.concat([accident.iloc[1:], accident.iloc[[0]]]).reset_index(drop=True)
accident

#등록량
register = pd.read_excel('project/등록/차종별_등록량_2018_01.xlsx',header=None)
register = register.iloc[:,[0,5,9,13,17,21]]
register = register.drop([0,1,2,4,23,24,25,26,27,28],axis=0)
register=register.drop(register.index[0])
register.columns=['시도','승용차','승합차','화물차','특수차','Sum']
register=register.reset_index(drop=True)
register


cols_to_divide = accident.columns[1:]

# Divide the corresponding columns and calculate the ratio
df_ratio = accident.copy()
df_ratio[cols_to_divide] = (accident[cols_to_divide].div(register[cols_to_divide]))

# Print the ratio DataFrame
print(df_ratio)
months=['01','02','03','04','05','06','07','08','09','10','11','12']
combined_df = pd.DataFrame()
for i in months:
    accident_path=f'project/사고/차종별_교통사고_2018_{i}.xls'
    accident=pd.read_excel(accident_path,skiprows=1)
    accident=accident[(accident['시군구']=='합계') & (accident['사고년도']=='사고건수[건]')] #지역별 사고건수 추출
    accident = accident.drop(columns=['시군구'])  #시군구 열 제외
    accident = accident[['시도','승용차','승합차','화물차','특수차']] #자동차들만추출
    accident['Sum'] = accident[['승용차','승합차','화물차','특수차']].sum(axis=1)
    accident = pd.concat([accident.iloc[1:], accident.iloc[[0]]]).reset_index(drop=True)

    register_path=f'project/등록/차종별_등록량_2018_{i}.xlxs'
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
    df_ratio.columns=['시도','2018.{i}']

    if combined_df.empty:
        combined_df = df_ratio
    else:
        combined_df = pd.merge(combined_df, df_ratio, on='시도', how='outer')

