class EmployeeSalary:
    hourly_payment = 400  # Почасовой уровень оплаты (ставка)

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.rest_days = rest_days

        if hours is None:
            self.hours = self.get_hours(rest_days)
        else:
            self.hours = hours

        # Если почта не указана, генерируем
        if email is None:
            self.email = self.get_email(name)
        else:
            self.email = email

    @classmethod
    def get_hours(cls, rest_days):
        # Рассчитывает рабочие часы на основе выходных
        return (7 - rest_days) * 8

    @classmethod
    def get_email(cls, name):
        # Генерирует email из имени
        return name + '@email.com'

    @classmethod
    def set_hourly_payment(cls, new_payment):
        # Изменяет почасовую ставку для всех сотрудников
        cls.hourly_payment = new_payment

    def salary(self):
        # Возвращает зарплату за неделю
        return self.hours * self.hourly_payment