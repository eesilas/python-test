print("歡迎使用拉麪點餐機")
print("使用者可選擇以下三種拉麪")
print("(1) 神虎拉麪 $149")
print("(2) 黑虎拉麪 $142")
print("(3) 赤虎拉麪 $159")

# 讓使用者輸入選擇的拉麪種類
choice = int(input("請輸入(輸入1, 2 或3): "))

# 設定拉麵價格
if choice == 1:
    price = 149
    noodle_type = "神虎拉麪"
elif choice == 2:
    price = 142
    noodle_type = "黑虎拉麪"
elif choice == 3:
    price = 159
    noodle_type = "赤虎拉麪"
else:
    print("輸入錯誤！")

# 問使用者是否加大
add_on = input("是否加大加$20？(Y 或 N):")
if add_on == ("Y" or "y"):
    price += 20
    size = "加大"
else: 
    price += 0
    size = "普通"

# 問使用者是否加糖心蛋
egg = input("是否加糖心蛋$10？(Y 或 N):")
if egg == ("Y" or "y"):
    price += 10
    egg_option = "加糖心蛋"
else:
    egg_option = "不加糖心蛋"

# 顯示最終訂單和總價格
print("您選擇的是", size, noodle_type, egg_option)
print("總價格為 $", price)
