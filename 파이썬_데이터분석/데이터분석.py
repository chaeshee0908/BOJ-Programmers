# -- 데이터분석

# csv파일 tsv파일
# csv : ','를 기준으로 데이터가 나눠져있는 파일
# tsv : tap을 기준으로 데이터가 나눠져있는 파일

import pandas as pd
from pandas.core.series import Series
# csv를 읽어오는 함수는 있는데 tsv를 읽어오는 함수는 없음
df = pd.read_csv('concat_1.csv')
# csv를 읽어오는 함수를 사용하여 ','를 't'으로 바꿔 읽어옴
df = pd.read_csv("gapminder.tsv", sep = '\t')
print(df.head())

# 표 : 데이터프레임
# 열 : 시리즈

type(df)
df.shape
df.columns
df.dtypes   # object는 객체가 아니라 문자열을 의미
df.info()   # non-null : 빈칸이 없다 => 빈칸 있는지 없는지 확인할 때 좋음


# 열에 접근
df['country']  # 'country'열에만 접근하고 싶을 때
df[['country', 'continent', 'year']]    # 여러 개의 열에 접근하고 싶을 때
# 행열에 접근
# loc : 이름에 접근
# iloc : 순서에 접근 (-1로 접근 가능)
df.loc[[0,10,100,1000]]     # 여러 가지 행에 접근할 때
# 왼쪽이 행, 오른쪽이 열
df.loc[[0,10,100,1000], ['country', 'year']]
df.iloc[[0,10,100,1000], [0, 2]]
df.iloc[:, [0,2]]   # ':'으로 모든 행에 접근

# 그룹화
a = df.groupby('year')['lifeExp'].mean()
a.to_excel('result1.xlsx')  # 원하는 내용을 엑셀파일로 만들어줌
a.plot()    # 그림을 통해 가시화해줌
# 생년월일별로 그룹화를 한 후에, 대륙별로 그룹화를 또 한 후에, 기댜수명을 평균내기
a = df.groupby(['year', 'continent'])['lifeExp'].mean()
# 대륙별로 나라가 몇 개인지 확인 -> nunique()
df.groupby('continent')['country'].nunique()


# 시리즈 만들기
a = pd.Series(['장원영', '백현', '김우빈', '아이유'])
a = pd.DataFrame({
    '이름' : ['장원영', '백현', '아이유'],
    '나이' : [17, 29, 28],
    '성별' : ['여자', '남자', '여자']
})
scientists = pd.read_csv('scientists.csv')
age = scientists['Age']
age.max()
age.min()
age.mean()
age.median()
# 퀴즈 : age에서 평균값보다 큰 age값만 뽑아보기
age[age > age.mean()]
age + age
age * age
age + 100
a = pd.Series([100, 100])
scientists[age > age.mean()]

born_dt = pd.to_datetime(scientists['Born'], format = '%Y-%m-%d')
died_dt = pd.to_datetime(scientists['Died'], format = '%Y-%m-%d')
scientists['Born'] = born_dt
scientists['Died'] = died_dt
# 'days'라는 새로운 열을 추가
# born, died 날짜를 문자에서 숫자로 바꿨기 때문에 계산 가능
scientists['days'] = scientists['Died'] - scientists['Born']


# 시리즈 저장하기, 데이터프레임
names = scientists['Name']
# pickle파일 만들기
names.to_pickle('names_series.pickle')
a = pd.read_pickle('names_series.pickle')

import seaborn as sns   # 데이터분석에 사용할 연습용 데이터 + 가시화
anscombe = sns.load_dataset('anscombe')
# 퀴즈 : 로마숫자 1 데이터 프레임
anscombe[anscombe['dataset'] == 'I']