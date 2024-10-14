import colorama
from colorama import Fore, Style

month_name = ["一月份", "二月份", "三月份", "四月份", "五月份", "六月份", \
              "七月份", "八月份", "九月份", "十月份", "十一月份", "十二月份"]
month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
year = int(input("請問你要列印西元哪一年的年曆: "))
#判斷閏年
is_leap_year = (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))
if is_leap_year:
    month_day[1] = 29
next_position = ((year - 1) + (year - 1) // 4 - (year - 1) // 100 + (year - 1) // 400 + 1) % 7

# 輸出年曆標題（顏色和字體大小）
print(Fore.YELLOW + Style.BRIGHT + f"<西元 {year} 年的年曆>" + Style.RESET_ALL)

for j in range(1, 13):
    print(month_name[j - 1])
    print("週日 週一 週二 週三 週四 週五 週六")
    if next_position != 0:
        print("     " * next_position, end="")  # 較英文版調整改為5個空格
    for i in range(1, month_day[j - 1] + 1):
        print(f"{i:4d}", end=" ")  # 較英文版調整i:4d
        next_position += 1
        if next_position == 7:
            next_position = 0
            print()
    print()  # 每個月份後增加一行空白
    print()  # 再增加一行空白行