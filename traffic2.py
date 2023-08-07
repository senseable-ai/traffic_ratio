import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import font_manager

#for문 
combined_df = pd.DataFrame()
for year in range(2018,2023):
    file_path=f'project/시도별_시군구별_교통사고/시도_시군구별_월별_교통사고_{year}.xls'
    df=pd.read_excel(file_path)
    df=df[(df['시군구']=='합계') & (df['사고년도']=='사고건수[건]')]
    filter_df = df.iloc[:, [0, 3]]
    if combined_df.empty:
        combined_df = filter_df
    else:
        combined_df = pd.merge(combined_df, filter_df, on='시도', how='outer')

#2018년 기준으로 정렬하기 combined_df=combined_df.sort_values('2018')
# 폰트 설정
font_path = '/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf'  # NanumBarunGothic 폰트 파일 경로
font_prop = font_manager.FontProperties(fname=font_path).get_name()
plt.rcParams['font.family'] = font_prop

# 필요한 데이터 선택
filtered_df = combined_df[combined_df['시도'] != '합계']  # '합계' 행 제외
filtered_df = filtered_df.drop(columns=['시도'])  # '시도' 열 제외


# 데이터 변환
years = filtered_df.columns
data = filtered_df.values
regions = combined_df[combined_df['시도'] != '합계']['시도']

# 3D 그래프 생성
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