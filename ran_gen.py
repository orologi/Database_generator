import random
from products import product_gen
import parameters as pm

'''
Random reviews are assigned to every product entries
It can have 3 values "NULL", "POSITIVE", "NEGATIVE"
Reviews are set to have higher percentage of NULLs and Nega
'''


date = []
review = []
review_answer = []
list_date = []


def review_gen(num_range, review_l, review_answer_l):
    neg_review_weight = (100 - pm.review_weight)
    neg_review_answer_weight = (100 - pm.review_answer_weight)
    my_list = [1] * (pm.review_weight) + [2] * (neg_review_weight)
    my_list_2 = [1] * (pm.review_answer_weight) + [2] * (neg_review_answer_weight)
    count = 0
    count_1 = 0
    for i in range(num_range):
        if (random.choice(my_list)) == 2:
            review_l.append("answer")
            count += 1
            if (random.choice(my_list_2)) == 1:
                review_answer_l.append("negative")
                count_1 += 1
                # print(count_1)
            else:
                review_answer_l.append("positive")
        else:
            review_l.append("no_answer")
            review_answer_l.append("")


function_clothing = []
function_eletronics = []
function_furniture = []

rp_clothing = product_gen(pm.list_1, function_clothing)
rp_eletronics = product_gen(pm.list_2, function_eletronics)
rp_forniture = product_gen(pm.list_3, function_furniture)

gender = []
category_output = []
product_output = []


def category_creator(name, category_product, gender_o=False, ):
    category_output.append(name)
    product_output.append(random.choice(category_product))
    review_gen(1, review, review_answer)

    if gender_o is True:
        gender.append(random.choice(pm.gender_choice))

    else:
        gender.append("Null")
