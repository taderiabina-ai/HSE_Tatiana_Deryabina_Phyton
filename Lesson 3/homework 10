class LegalEntity:
    def __init__(self, inn: str, name: str, case_number: str):
        self.inn = inn
        self.name = name
        self.case_number = case_number
        self.is_bankrupt = False
        self.bankruptcy_date = None

    def check_bankruptcy_status(self):
        """Проверяет статус банкротства (имитация)."""
        if self.is_bankrupt:
            print(f"⚠️ {self.name} (ИНН {self.inn}) - БАНКРОТ!")
            print(f"Дата: {self.bankruptcy_date}")
            print(f"Дело: {self.case_number}")
            print("\nНеобходимые действия:")
            print("1. Подать заявление в реестр кредиторов")
            print("2. Оспорить сделки должника")
        else:
            print(f"✅ {self.name} - действует, банкротства нет")

    def mark_as_bankrupt(self, date: str):
        """Отмечает должника как банкрота."""
        self.is_bankrupt = True
        self.bankruptcy_date = date
        print(f"{self.name} признан банкротом {date}")

    def get_info(self):
        """Выводит информацию о должнике."""
        status = "БАНКРОТ" if self.is_bankrupt else "Действует"
        return f"{self.name} (ИНН {self.inn}) - {status}"


# Пример использования
if __name__ == "__main__":
    debtor = LegalEntity("7707083893", 'ООО "Должник"', "А40-12345/2024")
    
    print(debtor.get_info())
    debtor.check_bankruptcy_status()
    
    debtor.mark_as_bankrupt("15.01.2024")
    debtor.check_bankruptcy_status()
