import random
import pandas as pd
from date_gen import random_date
from ran_gen import *
from products import *
from parameters import *
# import sqlite3
# import sqlalchemy


start_date_iter = iter(start_date)
end_date_iter = iter(end_date)

countries = []
profit = []
list_date = []
count = 0


def generator(country, start_date, end_date):
    for i in range(range_entries):
        category_creator(category_1, rp_clothing, True)
        countries.append(country)
        list_date.append(random_date(start_date, end_date, random.random()))
        profit.append(profit_clothing)

    for i in range(range_entries1):
        category_creator(category_2, rp_eletronics, False)
        countries.append(country)
        list_date.append(random_date(start_date, end_date, random.random()))
        profit.append(profit_eletronic)

    for i in range(range_entries2):
        category_creator(category_3, rp_forniture, False)
        countries.append(country)
        list_date.append(random_date(start_date, end_date, random.random()))
        profit.append(profit_furniture)


def month(c1, c2, c3, c4, c5, start_date, end_date):
    generator(c1, start_date, end_date)
    generator(c2, start_date, end_date)
    generator(c3, start_date, end_date)
    generator(c4, start_date, end_date)
    generator(c5, start_date, end_date)


for date in range(12):
    sti = next(start_date_iter)
    edi = next(end_date_iter)
    for i in range(3):
        month(random.choice(list_country),
              random.choice(list_country),
              random.choice(list_country),
              random.choice(list_country),
              random.choice(list_country),
              sti, edi)
    month(uk, de, fr, it, es, sti, edi)
    count = count + 1
    print(count, "of months", 12)

# build dataframe

row = list(zip(list_date, category_output, product_output, review,
               review_answer, countries, gender, profit))


# print("content",category_output, product_output, review, review_answer, countries, list_date )

labels = ["date", 'category', 'product', "review",
          "review_answer", "Country", "gender", "profit in euro"]
df = pd.DataFrame.from_records(row, columns=labels)

'''
#This code is to export it in a sql DATABASE
db = sqlite3.connect('out2.db')
df.to_sql('table1', db, if_exists='append', index=False)
'''

df.to_csv("out1.csv", sep='\t', float_format='%.3f')

print("Explore your fake DB")
