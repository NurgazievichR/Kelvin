import os 
import json

# folder_path = 'data/AddressRU/data'

# output_file_path = "output.json"

# all_arguments = []


# for filename in os.listdir(folder_path):
#     if filename.endswith(".json"):
#         file_path = os.path.join(folder_path, filename)
#         with open(file_path,'r',encoding='utf-8' ) as json_file:
#             data = json.load(json_file)
#             if isinstance(data, list):
#                 all_arguments.extend(data)


# with open(output_file_path , 'w' , encoding='utf-8') as output_file:
#     json.dump(all_arguments, output_file)

# print("Аргументы были успешно объединены в файл output.json")




# with open('output.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)


# result = []

# for k in data:
#     for u in k:
#         if type(u) != int and u.isdigit() == False:
#             result.append(u)


# with open('result.json' , 'w' , encoding='utf-8') as output_file:
#     json.dump(result, output_file)


#python shell

from apps.order.models import Street

with open('result.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

for i in data:
    Street.objects.create(name=i)

    