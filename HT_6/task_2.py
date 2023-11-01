# 2. Написати функцію <bank> , яка працює за наступною логікою: користувач робить вклад у розмірі <a> одиниць строком на <years> років під <percents> відсотків (кожен рік сума вкладу збільшується на цей відсоток, ці гроші додаються до суми вкладу і в наступному році на них також нараховуються відсотки). Параметр <percents> є необов'язковим і має значення
# по замовчуванню <10> (10%). Функція повинна принтануть суму, яка буде на рахунку, а також її повернути (але округлену до копійок).

def bank(deposit, years, percents=10):
    try:
        for _ in range(years):
            deposit += (deposit / 100) * percents

        deposit = round(deposit, 2)
        print(deposit)
        return deposit
    except TypeError:
        print("Invalid value. Provide a number.")
        return


bank(1568.25, 2)
