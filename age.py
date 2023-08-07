#%% 어린이 피해자
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import font_manager

#2018 어린이 피해자
age_2018=pd.read_excel('project/시도별_시군구별_교통사고/시도_시군구별_연령층별_사상자_2018.xls',skiprows=1)
age_2018=age_2018[(age_2018['시군구 ']=='합계')] #지역별 사망자수 부상자수 추출
age_2018=age_2018.iloc[:,[0,2,4]]
age_2018=age_2018.iloc[2:36]
age_2018=age_2018.rename(columns={'12세이하':'2018'})
age_2018=age_2018.reset_index(drop=True)
age_2018

#2019 어린이 피해자
age_2019=pd.read_excel('project/시도별_시군구별_교통사고/시도_시군구별_연령층별_사상자_2019.xls',skiprows=1)
age_2019=age_2019[(age_2019['시군구 ']=='합계')] #지역별 사망자수 부상자수 추출
age_2019=age_2019.iloc[:,[0,2,4]]
age_2019=age_2019.iloc[2:36]
age_2019=age_2019.rename(columns={'12세이하':'2019'})
age_2019=age_2019.reset_index(drop=True)
age_2019

#2021 어린이 피해자
age_2021=pd.read_excel('project/시도별_시군구별_교통사고/시도_시군구별_연령층별_사상자_2021.xls',skiprows=1)
age_2021=age_2021[(age_2021['시군구 ']=='합계')] #지역별 사망자수 부상자수 추출
age_2021=age_2021.iloc[:,[0,2,4]]
age_2021=age_2021.iloc[2:36]
age_2021=age_2021.rename(columns={'12세이하':'2021'})
age_2021=age_2021.reset_index(drop=True)
age_2021

#2022 어린이 피해자
age_2022=pd.read_excel('project/시도별_시군구별_교통사고/시도_시군구별_연령층별_사상자_2022.xls',skiprows=1)
age_2022=age_2022[(age_2022['시군구 ']=='합계')] #지역별 사망자수 부상자수 추출
age_2022=age_2022.iloc[:,[0,2,4]]
age_2022=age_2022.iloc[2:36]
age_2022=age_2022.rename(columns={'12세이하':'2022'})
age_2022=age_2022.reset_index(drop=True)
age_2022

age_2018
age_2019
age_2021
age_2022

age=pd.DataFrame()
age=pd.concat([age_2018,age_2019],axis=1)
age=age.iloc[:,[0,1,2,5]]
age=pd.concat([age,age_2021],axis=1)
age=age.iloc[:,[0,1,2,3,6]]
age=pd.concat([age,age_2022],axis=1)
age=age.iloc[:,[0,1,2,3,4,7]]
age

#%% 2018,2019,2021,2022 12세이하 사고 사망자수 + 부상자수

grouped = age_2018.groupby(['시도 '])['2018'].sum().reset_index()
original_order = age_2018['시도 '].unique()
grouped['시도 '] = pd.Categorical(grouped['시도 '], categories=original_order, ordered=True)
grouped.sort_values(by='시도 ', inplace=True)
grouped2018=grouped.reset_index(drop=True)

grouped = age_2019.groupby(['시도 '])['2019'].sum().reset_index()
original_order = age_2019['시도 '].unique()
grouped['시도 '] = pd.Categorical(grouped['시도 '], categories=original_order, ordered=True)
grouped.sort_values(by='시도 ', inplace=True)
grouped2019=grouped.reset_index(drop=True)

grouped = age_2021.groupby(['시도 '])['2021'].sum().reset_index()
original_order = age_2021['시도 '].unique()
grouped['시도 '] = pd.Categorical(grouped['시도 '], categories=original_order, ordered=True)
grouped.sort_values(by='시도 ', inplace=True)
grouped2021=grouped.reset_index(drop=True)

grouped = age_2022.groupby(['시도 '])['2022'].sum().reset_index()
original_order = age_2022['시도 '].unique()
grouped['시도 '] = pd.Categorical(grouped['시도 '], categories=original_order, ordered=True)
grouped.sort_values(by='시도 ', inplace=True)
grouped2022=grouped.reset_index(drop=True)

grouped2018
grouped2019
grouped2021
grouped2022

all=pd.DataFrame()
all=grouped2018
all=pd.merge(all,grouped2019,on='시도 ',how='outer')
all=pd.merge(all,grouped2021,on='시도 ',how='outer')
all=pd.merge(all,grouped2022,on='시도 ',how='outer')
#all=all.sort_values('2018') #2018년 기준으로 정렬해주기

years = all.iloc[:,[1,2,3,4]].columns
data = all.iloc[:,[1,2,3,4]].values
regions = all['시도 ']

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

#%% 2018,2019,2021,2022 12세이하 사고 사망자수 + 부상자수 정렬

grouped = age_2018.groupby(['시도 '])['2018'].sum().reset_index()
original_order = age_2018['시도 '].unique()
grouped['시도 '] = pd.Categorical(grouped['시도 '], categories=original_order, ordered=True)
grouped.sort_values(by='시도 ', inplace=True)
grouped2018=grouped.reset_index(drop=True)

grouped = age_2019.groupby(['시도 '])['2019'].sum().reset_index()
original_order = age_2019['시도 '].unique()
grouped['시도 '] = pd.Categorical(grouped['시도 '], categories=original_order, ordered=True)
grouped.sort_values(by='시도 ', inplace=True)
grouped2019=grouped.reset_index(drop=True)

grouped = age_2021.groupby(['시도 '])['2021'].sum().reset_index()
original_order = age_2021['시도 '].unique()
grouped['시도 '] = pd.Categorical(grouped['시도 '], categories=original_order, ordered=True)
grouped.sort_values(by='시도 ', inplace=True)
grouped2021=grouped.reset_index(drop=True)

grouped = age_2022.groupby(['시도 '])['2022'].sum().reset_index()
original_order = age_2022['시도 '].unique()
grouped['시도 '] = pd.Categorical(grouped['시도 '], categories=original_order, ordered=True)
grouped.sort_values(by='시도 ', inplace=True)
grouped2022=grouped.reset_index(drop=True)

grouped2018
grouped2019
grouped2021
grouped2022

all=pd.DataFrame()
all=grouped2018
all=pd.merge(all,grouped2019,on='시도 ',how='outer')
all=pd.merge(all,grouped2021,on='시도 ',how='outer')
all=pd.merge(all,grouped2022,on='시도 ',how='outer')
all=all.sort_values('2018') #2018년 기준으로 정렬해주기

years = all.iloc[:,[1,2,3,4]].columns
data = all.iloc[:,[1,2,3,4]].values
regions = all['시도 ']

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

#%% 2018,2019,2021,2022년 12세이하 사고 사망자수
age_death=age.iloc[[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32],:]
age_death=age_death.reset_index(drop=True)
age_death

filter_age_death=age_death.iloc[:,[2,3,4,5]]
years = filter_age_death.columns
data = filter_age_death.values
regions = age_death['시도 ']

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

#%% 2018,2019,2021,2022 12세이하 사고 사망자수 상위 5개 지역
age_death_top5=age.iloc[[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32],:]
age_death_top5=age_death_top5.reset_index(drop=True)
age_death_top5=age_death_top5.sort_values(['2018','2019','2021','2022'],ascending=False)
age_death_top5=age_death_top5.iloc[0:5,:].reset_index(drop=True)

filter_age_death_top5=age_death_top5.iloc[:,[2,3,4,5]]
years = filter_age_death_top5.columns
data = filter_age_death_top5.values
regions = age_death_top5['시도 ']

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

#%% 2018,2019,2021,2022년 12세이하 사고 부상자수
age_injured=age.iloc[[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33],:]
age_injured=age_injured.reset_index(drop=True)
age_injured

filter_age_injured=age_injured.iloc[:,[2,3,4,5]]
years = filter_age_injured.columns
data = filter_age_injured.values
regions = age_injured['시도 ']

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

#%% 2018,2019,2021,2022 12세이하 사고 사망자수 상위 5개 지역
age_injured_top5=age.iloc[[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33],:]
age_injured_top5=age_injured_top5.reset_index(drop=True)
age_injured_top5=age_injured_top5.iloc[0:5,:].reset_index(drop=True)
age_injured_top5

filter_age_injured_top5=age_injured_top5.iloc[:,[2,3,4,5]]
years = filter_age_injured_top5.columns
data = filter_age_injured_top5.values
regions = age_injured_top5['시도 ']

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
# %%
