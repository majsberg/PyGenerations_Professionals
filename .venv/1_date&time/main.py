# from datetime import date
#
# date_list = [date.fromisoformat(input()) for i in range(2)]
# print(min(date_list).strftime("%d-%m (%Y)"))


from datetime import date

n = int(input())
list_dates = [date.fromisoformat(input()) for _ in range(n)]
for each in sorted(list_dates):
    print(each.strftime("%d/%m/%Y"))