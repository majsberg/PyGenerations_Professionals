# from zipfile import ZipFile
#
# with ZipFile("files/workbook.zip", "r") as zip:
#     info = zip.infolist()
#     list_files = [i.is_dir() for i in info if i.is_dir() is False]
#     print(len(list_files))


# from zipfile import ZipFile
#
# with ZipFile("files/workbook.zip", "r") as zip:
#     info = zip.infolist()
#     size_before, size_after = 0, 0
#     for each in info:
#         size_before += each.file_size
#         size_after += each.compress_size
#     print(f"Объем исходных файлов: {size_before} байт(а)")
#     print(f"Объем сжатых файлов: {size_after} байт(а)")

# from zipfile import ZipFile
#
# with ZipFile("files/workbook.zip", "r") as zip_file:
#     info = zip_file.infolist()
#     k_list = list()
#     for each in info:
#         if each.is_dir() == False:
#             k = each.compress_size / each.file_size
#             k_list.append((each.filename, k))
#     minimum = min(k_list, key=lambda x: x[1])
#     print(minimum[0].split("/")[1])

# from zipfile import ZipFile
# from datetime import datetime
#
# with ZipFile("files/workbook.zip", "r") as zip_file:
#     info = zip_file.infolist()
#     list_result_names = list()
#     for each in info:
#         if each.is_dir() is False:
#             if datetime(*each.date_time) > datetime(2021, 11, 30, 14, 22, 00):
#                 list_result_names.append(each.filename.split('/')[-1])
#     list_result_names.sort()
#     for item in list_result_names:
#         print(item)

# from zipfile import ZipFile
# from datetime import datetime
#
# with ZipFile('files/workbook.zip') as zip:
#     info = zip.infolist()
#     files_list = [item for item in info if item.is_dir() is False]
#     files_list.sort(key=lambda x: x.filename.split('/')[-1])
#     for each in files_list:
#         print(each.filename.split('/')[-1])
#         print(f'  Дата модификации файла: {datetime(*each.date_time)}')
#         print(f'  Объем исходного файла: {each.file_size} байт(а)')
#         print(f'  Объем сжатого файла: {each.compress_size} байт(а)')
#         print()

# import json
# from zipfile import ZipFile
#
# def is_correct_json(file):
#     try:
#         data = json.load(file)
#         return data
#     except:
#         return False
#
# with ZipFile('files/data.zip') as zip_file:
#     info = zip_file.infolist()
#     jsons_list = [item for item in info if item.filename[-5:] == '.json']
#     for json_ in jsons_list:
#         zip_file.extract(json_, "files/extracted")
#
# players_list = list()
# for each in jsons_list:
#     with open(f"files/extracted/{each.filename}", 'r') as json_file:
#         dict_ = is_correct_json(json_file)
#         if dict_ and dict_["team"] == "Arsenal":
#             players_list.append(dict_)
#
# players_list.sort(key=lambda x: (x["first_name"], x["last_name"]))
#
# for each in players_list:
#     print(f'{each["first_name"]} {each["last_name"]}')


from zipfile import ZipFile

def get_size(size):
    if size < 1024:
        return f"{round(each.file_size)} B"
    elif 1024 < each.file_size < 1024 ** 2:
        return f"{round(each.file_size / 1024)} KB"
    else:
        return f"{round(each.file_size / 1024 ** 2)} MB"

with ZipFile('files/desktop.zip') as zip_file:

    for each in zip_file.infolist():
        indent = each.filename.count('/')
        #print(f'Название: {each.filename}, кол-во разделителей: {indent}, размер: {each.file_size}')
        if indent == 1 and each.file_size == 0:
            print(f"{each.filename.split('/')[-2]}")
        elif indent == 1 and each.file_size > 0:
            print(f"{' ' * indent * 2}{each.filename.split('/')[-1]} {get_size(each.file_size)}")
        elif 1 < indent < 3 and each.file_size == 0:
            print(f"{' ' * indent}{each.filename.split('/')[-2]}")
        elif indent >= 3 and each.file_size == 0:
            print(f"{' ' * indent + ' '}{each.filename.split('/')[-2]}")
        elif indent > 1 and each.file_size > 0:
            print(f"{' ' * indent * 2}{each.filename.split('/')[-1]} {get_size(each.file_size)}")
        elif indent == 0 and each.file_size > 0:
            print(f"{each.filename} {get_size(each.file_size)}")

