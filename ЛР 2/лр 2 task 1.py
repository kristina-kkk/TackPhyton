money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month_count = 0
available_money = money_capital
while True:
    current_spend = spend * ((1 + increase) ** month_count)
    budget = salary + available_money
    if current_spend > budget:
        break
    available_money = budget - current_spend
    month_count += 1

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

print("Количество месяцев, которое можно протянуть без долгов:",month_count)
