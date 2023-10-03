# Перечисление количества дней по месяцам, 1 индекс такой, чтобы месяцы соответствовали индексам
days_by_month = ['disabled value', 31, 28,
                 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Сопоставление числа месяца и выводимой информации в соответствии с данным числом
translated_months = {
    1: 'января',
    2: 'февраля',
    3: 'марта',
    4: 'апреля',
    5: 'мая',
    6: 'июня',
    7: 'июля',
    8: 'августа',
    9: 'сентября',
    10: 'октября',
    11: 'ноября',
    12: 'декабря'
}


def isleap(year) -> bool:
    """Определение високосного года"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


class Validations:
    @classmethod
    def _validate_day(cls, day_from: int, month: int, year: int) -> None:
        """Валидация дня"""
        if not isinstance(day_from, int) or not 1 <= day_from <= \
                days_by_month[month] + (isleap(year) and month == 2):
            raise ValueError('Некорректный ввод дня')

    @classmethod
    def _validate_month(cls, month: int) -> None:
        """Валидация месяца"""
        if not isinstance(month, int) or not 1 <= month <= 12:
            raise ValueError('Месяц должен быть в диапазоне от 1 до 12')

    @classmethod
    def _validate_year(cls, year: int) -> None:
        """Валидация года"""
        if not isinstance(year, int) or year < 0:
            raise ValueError('Год должен быть положительным числом')

    @classmethod
    def validations(cls, day_from: int, month: int, year: int) -> None:
        """Основной вызываемый метод для валидации вводимых дат"""
        cls._validate_year(year)
        cls._validate_month(month)
        cls._validate_day(day_from, month, year)


class Calendar:
    def _count_of_month_days(self, month: int, year: int) -> int:
        """Возвращает количество дней в месяце"""
        return days_by_month[month] + (isleap(year) and month == 2)

    def _iter_month(self, day_from: int, month: int, year: int) -> list:
        """Создание списка для итератора начиная с 'day_from' в месяце 'month'"""
        list_for_iter = []
        for day in range(day_from, self._count_of_month_days(month, year)+1):
            list_for_iter.append(f'{day} {translated_months[month]}')
        return list_for_iter

    def _iter_year(self, day_from: int, month: int, year: int) -> list:
        """Создание списка для итератора начиная с 'day_from' месяце 'month' до окончания года 'year'"""
        list_for_iter = []
        while month <= 12:
            list_for_iter.extend(self._iter_month(day_from, month, year))
            month += 1
            day_from = 1
        return list_for_iter

    def iteration(self, day_from: int, month: int, year: int, to_year: bool = False):
        Validations.validations(day_from, month, year)
        if to_year:
            iterable = iter(self._iter_year(day_from, month, year))
        else:
            iterable = iter(self._iter_month(day_from, month, year))
        while True:
            print(next(iterable))


instance = Calendar()
date = (28, 2, 2024)

###Все даты до конца месяца
# instance.iteration(*date)

###Все даты до конца года
instance.iteration(*date, to_year=True)
