import pandas as pd
import numpy as np

desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 10)
df1 = pd.read_csv("EcommercePurchases.csv")

#1. Display Top 10 Rows
# print(df1.head(10))

#2. Display Last 10 Rows
# print(df1.tail(10))

#3. Display Data types
# print(df1.dtypes)

#4. Display Null Values in dataset
# print(df1.isnull().sum())

#5. Display row and columns
# num_of_rows = df1.shape[0]
# num_of_columns = df1.shape[1]
# print(f"Number of rows: {num_of_rows}")
# print(f"Number of columns: {num_of_columns}")

#6. Display Highest and lowest Purchases price
# highest_purchase_price = df1["Purchase Price"].max()
# lowest_purchase_price = df1["Purchase Price"].min()
# print(f"Highest Purchase Price: {highest_purchase_price}")
# print(f"Lowest Purchase Price: {lowest_purchase_price}")

#7. Average Purchase Price
# print(df1["Purchase Price"].mean())

#8. How many people that have french 'fr' as their language
# print(len(df1[df1["Language"] == "fr"]))

#9. Job title contains Engineer
# print(len(df1[df1["Job"].str.contains("Engineer", case=False)]))

#10. Find The Email of the person with the following IP Address: 132.207.160.22
# print(df1["Email"][df1["IP Address"] == "132.207.160.22"])

#11. How many People have Mastercard as their Credit Card Provider and made a purchase above 50?
# print(len(df1[(df1["CC Provider"] == "Mastercard") & (df1["Purchase Price"]>50)]))

#12. Find the email of the person with the following Credit Card Number: 4664825258997302
# print(df1["Email"][df1["Credit Card"] == 4664825258997302])

#13. How many people purchase during the AM and how many people purchase during PM?
# num_of_purchase_AM = len(df1[df1["AM or PM"] == "AM"])
# num_of_purchase_PM = len(df1[df1["AM or PM"] == "PM"])
# print(f"Total purchase during AM :{num_of_purchase_AM}")
# print(f"Total purchase during PM :{num_of_purchase_PM}")
# print(df1["AM or PM"].value_counts())

# 14. How many people have a credit card that expires in 2020?

#1st option v

# def check():
#     count = 0
#     for date in df1["CC Exp Date"]:
#         if date.split("/")[1] == "20":
#             count +=1
#     return count
# print(check())

#2nd option v

# print(len(df1[df1["CC Exp Date"].apply(lambda x:x[3:] == "20")]))

#15. What are the top 5 most popular email providers (e.g. gmail.com, yahoo.com, etc...)

#1st option v
# def check():
#     list1=[]
#     for email in df1["Email"]:
#         list1.append(email.split("@")[1])
#     df1["temp"] = list1
# check()
# print(df1["temp"].value_counts().head())

#2nd option v

# print(df1["Email"].apply(lambda x:x.split("@")[1]).value_counts().head())