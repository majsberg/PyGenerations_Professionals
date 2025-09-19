# from datetime import date
#
# date_list = [date.fromisoformat(input()) for i in range(2)]
# print(min(date_list).strftime("%d-%m (%Y)"))


# from datetime import date
#
# n = int(input())
# list_dates = [date.fromisoformat(input()) for _ in range(n)]
# for each in sorted(list_dates):
#     print(each.strftime("%d/%m/%Y"))

# from datetime import date
#
# def print_good_dates(dates):
#     interesting_dates = list(filter(lambda x: x, (map(lambda each: each if each.year == 1992 and each.month + each.day == 29 else None, dates))))
#     interesting_dates.sort(key=lambda each: each.month)
#     for each in interesting_dates:
#         print(each.strftime("%B %d, %Y"))
#
# print(print_good_dates([]))

# from datetime import date
#
# def is_correct(day, month, year):
#     try:
#         if date(year, month, day):
#             return True, 1
#     except:
#         return False
#
# input_date = input()
# count_correct = 0
# while input_date != "end":
#     day, month, year = map(int, input_date.split('.'))
#     if is_correct(day, month, year):
#         print("Корректная")
#         count_correct += 1
#     else:
#         print("Некорректная")
#     input_date = input()
# print(count_correct)

# from datetime import datetime
#
# my_datetime = datetime.fromtimestamp(datetime.timestamp(datetime.now()))
# print(my_datetime)

from datetime import datetime

birthday = datetime(1992, 10, 6, 9, 48, 17)

birthday = birthday.replace(year=1993, month=12)

print(birthday)