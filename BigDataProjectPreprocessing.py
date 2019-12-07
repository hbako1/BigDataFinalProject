# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd

#Dataframe containing data about trending videos in Japan
#JPV = pd.read_csv("JPvideos.csv") 

#Dataframe containing data about trending videos in South Korea
#KRV = pd.read_csv("KRvideos.csv") 

#Dataframe containing data about trending videos in Mexico
#MXV = pd.read_csv("MXvideos.csv") 

#Dataframe containing data about trending videos in Russia
#RUV = pd.read_csv("RUvideos.csv") 

#We are only going to work with the following dataset 

#Dataframe containing data about trending videos in Canada
CAV = pd.read_csv("CAvideos.csv") 

#Dataframe containing data about trending videos in Germany
DEV = pd.read_csv("DEvideos.csv")

#Dataframe containing data about trending videos in France
FRV = pd.read_csv("FRvideos.csv") 

#Dataframe containing data about trending videos in Great Britain
GBV = pd.read_csv("GBvideos.csv") 

#Dataframe containing data about trending videos in Inida
INV = pd.read_csv("INvideos.csv") 

USV = pd.read_csv("USvideos.csv") 
#Dataframe containing data about trending videos in the USA


#Let's look at how the data in the dataframes 
showCAV = CAV.head(5)
showDEV = DEV.head(5)
shwoFRV = FRV.head(5)
showGBV = GBV.head(5)
showINV = INV.head(5)
showUSV = USV.head(5)

#Lets check out the number of rows and columns in each dataframe
USVdescription = USV.shape
CAVdescription = CAV.shape
GBVdescription = GBV.shape
FRVdescription = FRV.shape
DEVdescription = DEV.shape
INVdescription = INV.shape

#All the different countries dataframes have the same number of columns
#All the diffent countries have roughly about 40 000 rows 
#The data organization is similar for all the countries dataframes
#Lets check out the columns to see which one won't be needed 
#Let's take the US dataframes as an example 
print(USV.columns)
print(USV.dtypes)

#Lets delete the columns we do not need.
USV = USV.drop(columns = ['comment_count', 'thumbnail_link', 'comments_disabled', 'ratings_disabled', 'video_error_or_removed', 'description'])
print(USV.columns)

CAV = CAV.drop(columns = ['comment_count', 'thumbnail_link', 'comments_disabled', 'ratings_disabled', 'video_error_or_removed', 'description'])
print(CAV.columns)

GBV = GBV.drop(columns = ['comment_count', 'thumbnail_link', 'comments_disabled', 'ratings_disabled', 'video_error_or_removed', 'description'])
print(GBV)

FRV = FRV.drop(columns = ['comment_count', 'thumbnail_link', 'comments_disabled', 'ratings_disabled', 'video_error_or_removed', 'description'])
print(FRV.columns)

DEV = DEV.drop(columns = ['comment_count', 'thumbnail_link', 'comments_disabled', 'ratings_disabled', 'video_error_or_removed', 'description'])
print(DEV.columns)

INV = INV.drop(columns = ['comment_count', 'thumbnail_link', 'comments_disabled', 'ratings_disabled', 'video_error_or_removed', 'description'])
print(INV.columns)

#Let's check for null values 
USVnull = USV[USV.isnull().any(axis = 1)].head()
CAVnull = CAV[CAV.isnull().any(axis = 1)].head()
GBVnull = GBV[GBV.isnull().any(axis = 1)].head()
FRVnull = FRV[FRV.isnull().any(axis = 1)].head()
DEVnull = DEV[DEV.isnull().any(axis = 1)].head()
INVnull = INV[INV.isnull().any(axis = 1)].head()
#no null values where found 

#let's check for duplicates values 
USVduplicates = USV[USV.duplicated()].head()
CAVduplicates = CAV[CAV.duplicated()].head()
GBVduplicates = GBV[GBV.duplicated()].head()
FRVduplicates = FRV[FRV.duplicated()].head()
DEVduplicates = DEV[DEV.duplicated()].head()
INVduplicates = INV[INV.duplicated()].head()

#Let's delete these duplicates values
USV = USV.drop_duplicates()
CAV = CAV.drop_duplicates()
GBV = GBV.drop_duplicates()
FRV = FRV.drop_duplicates()
DEV = DEV.drop_duplicates()
INV = INV.drop_duplicates()

#Let's create a csv files with the nicely preprocessed dataframes
USV.to_csv("C:/Users/bakoe/Desktop/Bachelor degree/Fall 2019/Big Data Programming/USV.csv", index = True)
CAV.to_csv("C:/Users/bakoe/Desktop/Bachelor degree/Fall 2019/Big Data Programming/CAV.csv", index = True)
GBV.to_csv("C:/Users/bakoe/Desktop/Bachelor degree/Fall 2019/Big Data Programming/GBV.csv", index = True)
FRV.to_csv("C:/Users/bakoe/Desktop/Bachelor degree/Fall 2019/Big Data Programming/FRV.csv", index = True)
DEV.to_csv("C:/Users/bakoe/Desktop/Bachelor degree/Fall 2019/Big Data Programming/DEV.csv", index = True)
INV.to_csv("C:/Users/bakoe/Desktop/Bachelor degree/Fall 2019/Big Data Programming/INV.csv", index = True)