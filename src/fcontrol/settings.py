from decimal import Decimal

from PySide6.QtCore import QSettings


class AppSettings:
    LAST_INCOME = "allocation/last_income"
    DEFAULT_CURRENCY = "app/default_currency"

    def __init__(self):
        self._s = QSettings()

    def get_last_income(self) -> Decimal:
        return Decimal(str(self._s.value(self.LAST_INCOME, 0.0, type=float)))

    def set_last_income(self, value: Decimal):
        self._s.setValue(self.LAST_INCOME, float(value))

    def get_default_currency(self) -> str:
        return self._s.value(self.DEFAULT_CURRENCY, "PLN", type=str)

    def set_default_currency(self, value: str):
        self._s.setValue(self.DEFAULT_CURRENCY, value)
