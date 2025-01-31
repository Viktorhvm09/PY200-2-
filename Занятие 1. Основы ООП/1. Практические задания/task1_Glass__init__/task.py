from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        """
        Класс 'Стакан'
        :param capacity_volume: Объем стакана (вместимость)
        :param occupied_volume: Занятый объём (сколько налили в стакан)
        """

        # TODO создайте атрибут capacity_volume и occupied_volume Обязательно проверяйте типы (TypeError) и значения передаваемых аргументов (ValueError)
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Должно быть int или float")
        if capacity_volume <= 0:
            raise ValueError("Должно быть больше 0")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Должно быть int или float")
        if occupied_volume < 0:
            raise ValueError("Не может быть меньше 0")
        if occupied_volume > capacity_volume:
            raise ValueError("Заполнение превышает объем стакана")
        self.occupied_volume = occupied_volume

if __name__ == "__main__":
    # TODO инициализировать два объекта от класса Стакан (Glass)
    glass1 = Glass(100, 50)
    glass2 = Glass(200, 100)


    try:
        ...  # TODO инициализировать не корректные объекты
        glass3 = Glass(100, 150)
    except Exception as err:
        print(f"Была вызвана ошибка {err!r}")
    else:
        print("Данный код без ошибок")


