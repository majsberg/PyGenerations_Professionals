# from zipfile import ZipFile
#
# with ZipFile("files/workbook.zip", "r") as zip:
#     info = zip.infolist()
#     list_files = [i.is_dir() for i in info if i.is_dir() is False]
#     print(len(list_files))


from zipfile import ZipFile

with ZipFile("files/workbook.zip", "r") as zip:
    info = zip.infolist()
    size_before, size_after = 0, 0
    for each in info:
        size_before += each.file_size
        size_after += each.compress_size
    print(f"Объем исходных файлов: {size_before} байт(а)")
    print(f"Объем сжатых файлов: {size_after} байт(а)")