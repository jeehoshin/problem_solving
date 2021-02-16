getwd()
setwd('c:/python/package/2018_2/week1')
library(data.table)
library(dplyr)

x <- data.table::fread('c:/python/package/2018_2/week1/insurance.csv')


lm_fit <- lm(charges~., data = x)
lm_fit %>% summary

par(mfrow = c(2,2))
lm_fit %>% plot()
par(mfrow = c(1,1))
