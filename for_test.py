import work_with_text_file as wwt
import random

d = {}
for i in range(5):
    dict_l = wwt.read_dict()
    # print(dict_l)
    rand = random.choice(list(dict_l))
    # print(rand)
    rand_doble = random.choice(dict_l[rand])
    # print(rand_doble)
    d[rand] = rand_doble



# small_dict_l = wwt.random_5(dict_l)
# print(small_dict_l)