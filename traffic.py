import pandas as pd
import numpy as np
import os
os.getcwd()
data=pd.read_excel('project/사고일반/사고유형별_교통사고.xls')
data
pd.read_excel('project/사고일반/경찰서별_월별_교통사고_2018.xls')
directory='project/시도별_시군구별_교통사고'
file_extension='.xls'
file_list=[file for file in os.listdir(directory) if file.endswith(file_extension)]
for file in file_list:
    file_path=os.path.join(directory,file)
    df=pd.read_excel(file_path)

for year in range(2018, 2023):
    file_path = f'{directory}/시도_시군구별_월별_교통사고_{year}{file_extension}'
    df = pd.read_excel(file_path)
print(df)
df=pd.read_excel('project/시도별_시군구별_교통사고/시도_시군구별_월별_교통사고_2018.xls')
df[df['시도']=='서울']
df[df['시도']=='부산']
df[df['시도']=='대구']
df[df['시도']=='인천']
df[df['시도']=='광주']
df[df['시도']=='대전']
df[df['시도']=='울산']
df[df['시도']=='세종']
df[df['시도']=='경기']
df[df['시도']=='강원']
df[df['시도']=='충북']
df[df['시도']=='충남']
df[df['시도']=='전북']
df[df['시도']=='전남']
df[df['시도']=='경북']
df[df['시도']=='경남']
df[df['시도']=='제주']
region=('서울','부산','대구','인천','광주','대전','울산','세종','경기','강원','충북','충남','전북','전남','경북','경남','제주')

df=pd.read_excel('project/시도별_시군구별_교통사고/시도_시군구별_월별_교통사고_2018.xls')
filter_df=df[(df['시군구']=='합계') & (df['사고년도']=='사고건수[건]')]
df=filter_df.drop([filter_df.columns[1],filter_df.columns[2],filter_df.columns[3]],axis=1)
df
filtered_df = df[df['시도'] != '합계']  # '합계' 행 제외
filtered_df = filtered_df.drop(columns=['시도'])  # '시도' 열 제외
filtered_df
months = filtered_df.columns
months
data = filtered_df.values
data
df[df['시도'] != '합계'] 
regions = df[df['시도'] != '합계']['시도']
regions

#월별,지역별 사고량 OLAP 

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import font_manager

# 폰트 설정
font_path = '/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf'  # NanumBarunGothic 폰트 파일 경로
font_prop = font_manager.FontProperties(fname=font_path).get_name()
plt.rcParams['font.family'] = font_prop

df=pd.read_excel('project/시도별_시군구별_교통사고/시도_시군구별_월별_교통사고_2018.xls')
filter_df=df[(df['시군구']=='합계') & (df['사고년도']=='사고건수[건]')]
df=filter_df.drop([filter_df.columns[1],filter_df.columns[2],filter_df.columns[3]],axis=1)
df=df.sort_values('2018.1')
# 필요한 데이터 선택
filtered_df = df[df['시도'] != '합계']  # '합계' 행 제외
filtered_df = filtered_df.drop(columns=['시도'])  # '시도' 열 제외

# 데이터 변환
months = filtered_df.columns
data = filtered_df.values
regions = df[df['시도'] != '합계']['시도']

# 3D 그래프 생성
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# 막대 그래프 생성
for i in range(len(months)):
    for j in range(len(data)):
        ax.bar3d(i, j, 0, 0.5, 0.5, data[j][i], alpha=0.8)

# 축 설정
ax.set_xlabel('월')
ax.set_ylabel('지역')
ax.set_zlabel('사고건수')

# x, y 축 눈금 설정
ax.set_xticks(range(len(months)))
ax.set_yticks(range(len(regions)))
ax.set_xticklabels(months, rotation=20)
ax.set_yticklabels(regions, rotation=-10)

plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)

# 그래프 출력
plt.show()

