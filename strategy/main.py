from abc import ABC, abstractmethod

# Интерфейс стратегии
class BattleStrategy(ABC):
    @abstractmethod
    def execute(self):
        pass

# Конкретные стратегии
class SwordStrategy(BattleStrategy):
    def execute(self):
        print("Рыцарь сражается с врагом, используя свой мощный меч!")

class MagicStrategy(BattleStrategy):
    def execute(self):
        print("Рыцарь использует заклинание огненного шара для атаки врага!")

class FleeStrategy(BattleStrategy):
    def execute(self):
        print("Рыцарь решает, что бегство – лучшая стратегия и убегает от врага!")

# Класс рыцаря
class Knight:
    def __init__(self, name, strategy: BattleStrategy):
        self.name = name
        self._strategy = strategy

    def set_strategy(self, strategy: BattleStrategy):
        self._strategy = strategy

    def battle(self):
        print(f"{self.name} готов к битве!")
        self._strategy.execute()

# Пример использования
knight = Knight("Sir Lancelot", SwordStrategy())

# Рыцарь использует стратегию боя мечом
knight.battle()  # Ожидается: "Рыцарь сражается с врагом, используя свой мощный меч!"

# Меняем стратегию на магию
knight.set_strategy(MagicStrategy())
knight.battle()  # Ожидается: "Рыцарь использует заклинание огненного шара для атаки врага!"

# Рыцарь решает убежать
knight.set_strategy(FleeStrategy())
knight.battle()  # Ожидается: "Рыцарь решает, что бегство – лучшая стратегия и убегает от врага!"
