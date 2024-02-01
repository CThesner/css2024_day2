#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:39:11 2024

@author: C_Thesner
"""

import pandas as pd

# # file = pd.read_csv("data_02/iris.csv")

# # fie2 = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

# # # url1 = "https://github.com/CThesner/css2024_day1/blob/main/housing_data.csv"

# # # file3 = pd.read_csv(url1)

# # file4 = pd.read_csv("data_02/Geospatial Data.txt", sep=";")

# # file5 = pd.read_excel("data_02/residentdoctors.xlsx") #can specify sheet aswell, in pandas doc

# # url2 = "https://raw.githubusercontent.com/Asabele240701/css4_day02/main/effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv"

# # df = pd.read_csv(url2)


# # df2 = pd.read_csv("chatFiles/Accelerometer_data.csv", names=["date_time", "x", "y", "z"])

# # df = pd.read_csv("data_02/country_data_index.csv", index_col=0)

# df = pd.read_excel("data_02/residentdoctors.xlsx")

# print(df.info())

# """

# Regulat expressions

# 30-01-2024
# 01-30-2024


# """

# df["LOWER_AGE"] = df["AGEDIST"].str.extract("(\d+)-")

# print(df.info())

# df["LOWER_AGE"] = df["LOWER_AGE"].astype(int)

# print(df.info())


# """

# working with dates

# """

# df = pd.read_csv("data_02/time_series_data.csv", index_col=0)

# print(df.info())

# # df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y")

# df["Date"] = pd.to_datetime(df["Date"])

# print(df.info())

# df["Year"] = df["Date"].dt.year
# df["Month"] = df["Date"].dt.month
# df["Day"] = df["Date"].dt.day

# #######################################################

# import pandas as pd

# df = pd.read_csv("data_02/patient_data_dates.csv", index_col=0)

# # # Allows you to see all rows
# # pd.set_option('display.max_rows',None)

# # print(df)

# df.drop(index=26, inplace=True)

# df["Date"] = pd.to_datetime(df["Date"])

# avg_cal = df["Calories"].mean()

# df["Calories"].fillna(avg_cal, inplace=True)



# """

# Best practices

# """

# df.dropna(inplace=True)

# df = df.reset_index(drop=True)

# df.loc[7, "Duration"] = 45


##############################

df = pd.read_csv("data_02/iris.csv")

col_names = df.columns.tolist()

df["sepal_length_sq"] = df["sepal_length"]**2

df["sepal_length_sq2"] = df["sepal_length"].apply(lambda x: x**2)

grouped = df.groupby("class")

mean_sq_values = grouped["sepal_length_sq"].mean()

print(mean_sq_values)

df["class"] = df["class"].str.replace("Iris-", "")

#filter data

df = df[df["sepal_length"]>5]


df = df[df["class"] == "virginica"]

df.to_csv("virginica_sepal_len_larger_5")



# ##########
# df1 = pd.read_csv("data_02/person_split1.csv")
# df2 = pd.read_csv("data_02/person_split2.csv")


# # df = pd.concat([df1,df2]) #uses each df's index

# df = pd.concat([df1,df2], ignore_index=True) #Creates a new index that suits the new df

# #######################


# df1 = pd.read_csv("data_02/person_education.csv")
# df2 = pd.read_csv("data_02/person_work.csv")


# #inner join

# df_merge_inner = pd.merge(df1, df2, on="id")



















