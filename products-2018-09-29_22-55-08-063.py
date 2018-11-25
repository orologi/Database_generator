from random import choice
from parameters import *

'''
Random combinations of product names are generated
from the following list of products for category

'''


def product_gen(words_for_products_name, list_of_products):
    attemps = 0
    list_of_products = []
    tester = False
    while tester is False:
        gen_products = []
        for i in range(50):
            gen_products.append(choice(words_for_products_name) + '_' +
                                choice(list_of_colours) + '_' +
                                choice(list_numbers))
        s = set()
        duplicates = set(x for x in gen_products if x in s or s.add(x))
        list_of_products = list(set(gen_products) - set(duplicates))
        attemps = attemps + 1
        print(attemps)
        print(len(list_of_products))
        if len(list_of_products) < range_products:
            print("Sucess!!!", len(list_of_products), '\n',
                  "number of attemps need:", attemps, 'number of productss',
                  range_products)
            return (list_of_products)
            tester = True


if __name__ == '__main__':
    pro_e_list = []
    pro_list = product_gen(list_1, pro_e_list)
    print(pro_list, len(pro_list))
