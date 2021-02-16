# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#[1]회귀분석
## 1.insurance 데이터를 가지고 선형회귀식에 적합하라.(반응변수는 charges이다.)
#%% [1]
import pandas as pd
import numpy as np
import statsmodels.api as sm

insure = pd.read_csv("C:/Users/jiho0/Desktop/Data_Analysis/(p-sat)package/2018_2/week1/insurance.csv")
insure.head(5)

#%% [2] data 전처리 - dummy 변수 화
x_data = insure.drop(['charges'], axis = 1)
y_data = insure['charges']

#dummy화 진행
dummy_dat = x_data[['sex', 'smoker', 'region']]
dummy_dat1 = pd.get_dummies(dummy_dat, drop_first = True)

#다시 데이터 붙이기
x_data1 = pd.concat([x_data[['age', 'bmi', 'children']], dummy_dat1], axis = 1)

#상수항 만들어주기
x_data2 = sm.add_constant(x_data1)

#선형회귀적합
ls = sm.OLS(y_data, x_data2).fit()

##2. 적합한 회귀식의 잔차 plot을 그리고 잔차의 선형성, 정규성, 
##등분산성에 대해서 그래프를 근거로 판단하라.