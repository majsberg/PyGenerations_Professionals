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

# from datetime import datetime
#
# birthday = datetime(1992, 10, 6, 9, 48, 17)
#
# birthday = birthday.replace(year=1993, month=12)
#
# print(birthday)


# from datetime import datetime
#
# text = 'Уважаемый пациент, доктор готов принять Вас 15.07.2022 в 08:30'
#
# dt = datetime.strptime(text, 'Уважаемый пациент, доктор готов принять Вас %d.%m.%Y в %H:%M')
#
# print(dt)

# from datetime import datetime
#
# seconds = 2483228800
# dt = datetime(2011, 11, 4)
#
# print(datetime.fromtimestamp(seconds))
# print(dt.timestamp())

# from datetime import datetime
#
# times_of_purchases = [datetime(2017, 10, 1, 12, 23, 25), datetime(2017, 10, 1, 15, 26, 26),
#                       datetime(2017, 10, 1, 15, 42, 57), datetime(2017, 10, 1, 17, 49, 59),
#                       datetime(2017, 10, 2, 6, 37, 10), datetime(2017, 10, 2, 6, 42, 53),
#                       datetime(2017, 10, 2, 8, 56, 45), datetime(2017, 10, 2, 9, 18, 3),
#                       datetime(2017, 10, 2, 12, 23, 48), datetime(2017, 10, 2, 12, 45, 5),
#                       datetime(2017, 10, 2, 12, 48, 8), datetime(2017, 10, 2, 12, 10, 54),
#                       datetime(2017, 10, 2, 19, 18, 10), datetime(2017, 10, 2, 12, 31, 45),
#                       datetime(2017, 10, 3, 20, 57, 10), datetime(2017, 10, 4, 7, 4, 57),
#                       datetime(2017, 10, 4, 7, 13, 31), datetime(2017, 10, 4, 7, 13, 42),
#                       datetime(2017, 10, 4, 7, 21, 54), datetime(2017, 10, 4, 14, 22, 12),
#                       datetime(2017, 10, 4, 14, 50), datetime(2017, 10, 4, 15, 7, 27),
#                       datetime(2017, 10, 4, 12, 44, 49), datetime(2017, 10, 4, 12, 46, 41),
#                       datetime(2017, 10, 4, 16, 32, 33), datetime(2017, 10, 4, 16, 34, 44),
#                       datetime(2017, 10, 4, 16, 46, 59), datetime(2017, 10, 4, 12, 26, 6)]
#
# list_before = list(filter(lambda x: x.hour < 12, times_of_purchases))
# list_after = list(filter(lambda x: x.hour >= 12, times_of_purchases))
# print("До полудня") if len(list_before) > len(list_after) else print("После полудня")

from datetime import date, time, datetime

dates = [date(1793, 8, 23), date(1410, 3, 11), date(804, 11, 12), date(632, 6, 4),
         date(295, 1, 23), date(327, 8, 24), date(167, 4, 16), date(229, 1, 24),
         date(1239, 2, 5), date(1957, 7, 14), date(197, 8, 24), date(479, 9, 6)]

times = [time(7, 33, 27), time(21, 2, 10), time(17, 20, 47), time(20, 8, 59),
         time(12, 42, 56), time(15, 9, 57), time(17, 47, 9), time(9, 40, 2),
         time(11, 47, 1), time(17, 27, 10), time(17, 55, 40), time(9, 14, 9)]

zip_list = list(zip(dates, times))
result_list = list(map(lambda x: datetime.combine(x[0], x[1]), zip_list))
result_list = sorted(result_list, key=lambda x: x.second)
for each in result_list:
    print(each)