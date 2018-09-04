import random

'''
Values can be set for the range of entries to be generated
Valus can be set for profit range for category
'''

# number of entries
range_entries = random.randint(0, 300)
range_entries1 = random.randint(0, 300)
range_entries2 = random.randint(0, 300)

# values of profits for category
profit_clothing = random.randint(1, 200)
profit_eletronic = random.randint(1, 200)
profit_furniture = random.randint(1, 200)

# list for name of pruducts and number of products

list_1 = ['Microwave', 'air_conditioner', 'washing_machine ',
          ' fireplace', 'Refrigerators', 'water_heater',
          'Vacuum_cleaner',  'window_fan', 'dryer'
          ]

list_2 = ['Bed', 'Daybed', 'Futon', 'Hammock',
          'Headboard', 'cradle,', 'Mattress', 'Sofa_Bed'
          ]

list_3 = ['shirt', 't-shirt', 'coat', 'suit', 'hat',
          'underwear', 'swimsuit', 'trousers',  'bag'
          ]

list_of_colours = ['Red', 'Orange', 'Yellow', 'Green',
                   'Blue', 'Indigo',  'Magenta',
                   'Violet', 'Purple', 'Pink', 'Brown',
                   'White', 'Gray', 'Black', 'Cyan'
                   ]


list_numbers = ['1', '2']


range_products = random.randint(51, 100)

# percentage of reviews and positive or negative

review_weight = random.randint(10, 100)
review_answer_weight = random.randint(10, 100)

# dates for months to have an even number of entries for each of them

start_date = [("1/1/2017"), ("2/1/2017"), ("3/1/2017"), ("4/1/2017"), ("5/1/2017"), ("6/1/2017"),
              ("7/1/2017"), ("8/1/2017"), ("9/1/2017"), ("10/1/2017"), ("11/1/2017"), ("12/1/2017")]


end_date = [("1/31/2017"), ("2/28/2017"), ("3/31/2017"), ("4/30/2017"), ("5/31/2017"), ("6/30/2017"),
            ("7/31/2017"), ("8/31/2017"), ("9/30/2017"), ("10/31/2017"), ("11/30/2017"), ("12/31/2017")]


# countries

uk, de, fr, it, es = "UK", "DE", "FR", "IT", "ES"
list_country = [uk, de, fr, it, es]


# name of the categories
category_1 = "Clothing"
category_2 = "Eletronics"
category_3 = "Forniture"

# gender
gender_choice = ["M", "F"]
