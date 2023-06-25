total = 0
tickets = int(input("Введите количество билетов:\n"))
for age in range(tickets):
    age = int(input("Введите возраст посетителя:\n"))
    if age < 18:
        total += 0
        print("Бесплатно")
    if 18 <= age <= 25:
        total += 990
        print("Цена 990 р.")
    if age > 25:
        total += 1390
        print("Цена 1390 р.")
print("Кол-во билетов:", tickets, "шт." )
if tickets > 3:
    discount = total / 100 * 10
    print("Скидка составляет:", "%.2f" % discount, "руб.")
    print("К оплате с учетом скидки:", "%.2f" % (total -discount), "руб.")
