from datetime import datetime

class CourtCase:
    def __init__(self, case_number: str):
        # Обязательный параметр
        self.case_number = case_number
        
        # Атрибуты со значениями по умолчанию
        self.case_participants = []
        self.listening_datetimes = []
        self.is_finished = False
        self.verdict = ""

    def set_a_listening_datetime(self, dt: datetime, description: str = "Плановое заседание"):
        hearing = {
            "datetime": dt,
            "description": description
        }
        self.listening_datetimes.append(hearing)
        print(f"Заседание на {dt.strftime('%d.%m.%Y %H:%M')} добавлено.")

    def add_participant(self, inn: str):
        if inn not in self.case_participants:
            self.case_participants.append(inn)
            print(f"Участник с ИНН {inn} добавлен.")
        else:
            print(f"Участник с ИНН {inn} уже есть в деле.")

    def remove_participant(self, inn: str):
        if inn in self.case_participants:
            self.case_participants.remove(inn)
            print(f"Участник с ИНН {inn} удален из дела.")
        else:
            print(f"Ошибка: участник с ИНН {inn} не найден в деле.")

    def make_a_decision(self, verdict_text: str):
        if self.is_finished:
            print("Дело уже завершено, повторное решение вынести нельзя.")
            return
            
        self.verdict = verdict_text
        self.is_finished = True
        print(f"По делу №{self.case_number} вынесено решение: {self.verdict}")

    def __str__(self):
        status = "Завершено" if self.is_finished else "В процессе"
        return (f"Дело №{self.case_number} | Статус: {status} | "
                f"Участников: {len(self.case_participants)} | "
                f"Заседаний: {len(self.listening_datetimes)}")


# ==========================================
# Пример использования класса
# ==========================================
if __name__ == "__main__":
    my_case = CourtCase(case_number="А45-12345/2023")
    print(my_case)
    print("-" * 40)

    my_case.add_participant("7707083893")
    my_case.add_participant("7710140679")
    my_case.add_participant("7707083893")

    my_case.set_a_listening_datetime(
        dt=datetime(2023, 10, 15, 10, 0), 
        description="Предварительное слушание"
    )
    
    print("-" * 40)
    print(my_case)

    my_case.remove_participant("7710140679")
    
    my_case.make_a_decision("Иск удовлетворен в полном объеме.")
    
    print("-" * 40)
    print("Итоговая информация:")
    print(my_case)
    print(f"Резолютивная часть: {my_case.verdict}")
