#!/usr/bin/env python
# coding: utf-8

# ### 1. Simple Data Exploration(data = insurance.csv)

# #### 1.1 변수탐색

# ##### 1. age, charges, bmi, children의 분포를 본 후, 어떤 정보를 얻을 수 있는지 간략하게 서술하시오.

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_insure = pd.read_csv('c:/python/package/2018_2/week1/insurance.csv')
df_insure


# ##### 2. 아이가 있는 경우에는 o, 없는 경우에는 X라고 표시하는 열을 만드시오.

# ##### 3. 다음 문장의 T,F를 판단할 수 있는 근거를 코드와 함께 제시하라
# 
# - 아이가 있는 경우보다 아이가 없는 경우에 흡연자비율이 더 많다.
# - southwest 지역은 아이가 있는 경우보다 아이가 없는 경우에 흡연자 수가 더 많다. 
# - 의료보험비가 가장 많이 나오는 사람은 southwest 지역에서 산다.

# #### 1.2 Linear Regression

# ##### 1. charges를 Y로 하는 회귀식을 세운 후, beta hat(LSE), R-square, Adjusted R-square, p-value를 구하라

# ### 2.Simple Data Exploration(data = scores.csv, question.csv)

# #### 2.1 변수탐색

# ##### 1. 학생별로 4번의 시험점수를 평균을 내어 이를 scoreboard로 저장하라.

# ##### 2. question.csv를 이용하여 scoreboard에 학생 별 질문 횟수가 기록된 n_question이라는 새로운 열을 생성하라. 이후, 학생 별로 계산한 평균점수에 학생 별 질문횟수를 더해 최종 점수를 계산한 totalscore이라는 새로운 열을 생성하라

# ##### 3. totalscore를 기준으로 상위 30%까지 A, 상위 60%까지 B, 상위 90%까지 C, 나머지는 F. grade라는 열에 이 기준에 의거하여 학점을 부여하라

# ##### 4. A,B,C,F 학점별로 시험 별 평균점수의 차이가 있었는데 시각화해보기 위해 다음을 수행하라
# 
# - 학생 별 학점을 grades라는 이름으로 scoresdp 포함시키고
# - 다음에 해당하는 데이터 프레임인 scores_gg를 생성하라. 학점 별로 1~4차 mean_first부터 mean_fourth를 낸 다음 key를 test, value를 score로 지정하여 하나의 열로 정리한 데이터 프레임
# - scores_gg안의 test열에 있는 mean_first를 1,,, mean_fourth를 4로 바꾼 다음 이 열을 factor처리. 그리고 다음 시각화를 수행

# In[ ]:




