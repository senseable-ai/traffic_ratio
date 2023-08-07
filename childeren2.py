import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import font_manager

font_path = '/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf'  # NanumBarunGothic 폰트 파일 경로
font_prop = font_manager.FontProperties(fname=font_path).get_name()
plt.rcParams['font.family'] = font_prop

#%% 2018 어린이 피해자
children_2018=pd.read_excel('project/어린이_교통사고_관련/지역별_시간대별_스쿨존내_어린이(12세이하)_교통사고_2018.xls',skiprows=1)
children_2018=children_2018[(children_2018['기준년도']=='사고[건]')].reset_index(drop=True)
children_2018=children_2018.replace('-',0)
children_2018=children_2018.iloc[[0],:]
children_2018

time_intervals = children_2018.columns[3:]
total_accidents = children_2018.iloc[0, 3:].values

# Plotting the graph
plt.figure(figsize=(10, 6))
#plt.plot(time_intervals, total_accidents, marker='o', linestyle='-')
plt.bar(time_intervals,total_accidents,align='center',color='blue',edgecolor='black')
plt.xlabel('Time Intervals')
plt.ylabel('Total Accidents [Cases]')
plt.title('Total Accidents Over Time 2018')
plt.ylim([0,160])
plt.xticks(rotation=45)
plt.grid()
plt.show()

#%% 2019 어린이 피해자
children_2019=pd.read_excel('project/어린이_교통사고_관련/지역별_시간대별_스쿨존내_어린이(12세이하)_교통사고_2019.xls',skiprows=1)
children_2019=children_2019[(children_2019['기준년도']=='사고[건]')].reset_index(drop=True)
children_2019=children_2019.replace('-',0)
children_2019=children_2019.iloc[[0],:]
children_2019=children_2019.iloc[:,[0,1,2,6,7,8,9,10,11,12,13,14]]

time_intervals = children_2019.columns[3:]
total_accidents = children_2019.iloc[0, 3:].values

# Plotting the graph
plt.figure(figsize=(10, 6))
#plt.plot(time_intervals, total_accidents, marker='o', linestyle='-')
plt.bar(time_intervals,total_accidents,align='center',color='blue',edgecolor='black')
plt.xlabel('Time Intervals')
plt.ylabel('Total Accidents [Cases]')
plt.title('Total Accidents Over Time 2019')
plt.xticks(rotation=45)
plt.grid()
plt.show()

#%% 2021 어린이 피해자
children_2021=pd.read_excel('project/어린이_교통사고_관련/지역별_시간대별_스쿨존내_어린이(12세이하)_교통사고_2021.xls',skiprows=1)
children_2021=children_2021[(children_2021['기준년도']=='사고[건]')].reset_index(drop=True)
children_2021=children_2021.replace('-',0)
children_2021=children_2021.iloc[[0],:]
children_2021

time_intervals = children_2021.columns[3:]
total_accidents = children_2021.iloc[0, 3:].values

# Plotting the graph
plt.figure(figsize=(10, 6))
#plt.plot(time_intervals, total_accidents, marker='o', linestyle='-')
plt.bar(time_intervals,total_accidents,align='center',color='blue',edgecolor='black')
plt.xlabel('Time Intervals')
plt.ylabel('Total Accidents [Cases]')
plt.title('Total Accidents Over Time 2021')
plt.xticks(rotation=45)
plt.grid()
plt.show()

#%% 2022 어린이 피해자
children_2022=pd.read_excel('project/어린이_교통사고_관련/지역별_시간대별_스쿨존내_어린이(12세이하)_교통사고_2022.xls',skiprows=1)
children_2022=children_2022[(children_2022['기준년도']=='사고[건]')].reset_index(drop=True)
children_2022=children_2022.replace('-',0)
children_2022=children_2022.iloc[[0],:]
children_2022

time_intervals = children_2022.columns[3:]
total_accidents = children_2022.iloc[0, 3:].values

# Plotting the graph
plt.figure(figsize=(10, 6))
#plt.plot(time_intervals, total_accidents, marker='o', linestyle='-')
plt.bar(time_intervals,total_accidents,align='center',color='blue',edgecolor='black')
plt.xlabel('Time Intervals')
plt.ylabel('Total Accidents [Cases]')
plt.title('Total Accidents Over Time 2022')
plt.xticks(rotation=45)
plt.grid()
plt.show()

#%% 18년19년21년22년
children=pd.DataFrame()
children=children_2018
children=pd.concat([children, children_2019], ignore_index=True)
children=pd.concat([children, children_2021], ignore_index=True)
children=pd.concat([children, children_2022], ignore_index=True)
children['기준년도']=[2018,2019,2021,2022]
children=children.iloc[:,[1,3,4,5,6,7,8,9,10,11]]

# Plotting the multi-bar graph
fig, ax = plt.subplots(figsize=(10, 6))

bar_width = 0.2
time_periods = children.columns[1:]
years = children['기준년도']

for i, year in enumerate(years):
    x = [j + bar_width * i for j in range(len(time_periods))]
    plt.bar(x, children.loc[i, time_periods], width=bar_width, label=f'{year}')

plt.xlabel('Time Period')
plt.ylabel('Number of Accidents')
plt.title('Multi-Bar Graph of Accidents Over Time')
plt.xticks([j + bar_width * (len(years) / 2) for j in range(len(time_periods))], time_periods)
plt.legend(title='Year')
plt.grid()
plt.show()

# %%
