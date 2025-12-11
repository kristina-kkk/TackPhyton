salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
needed_money = 0
for month in range(months):
    current_spend = spend * ((1 + increase) ** month)
    deficit = current_spend - salary
    if deficit > 0:
        needed_money += deficit
    needed_money = round(needed_money)

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", needed_money)
