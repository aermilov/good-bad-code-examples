from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


# Конкретные команды для управления заметками
class CreateNoteCommand(Command):
    def __init__(self, notes, note):
        self.notes = notes
        self.note = note

    def execute(self):
        self.notes.create(self.note)

    def undo(self):
        self.notes.delete(self.note)


class DeleteNoteCommand(Command):
    def __init__(self, notes, note):
        self.notes = notes
        self.note = note

    def execute(self):
        self.notes.delete(self.note)

    def undo(self):
        self.notes.create(self.note)


class UpdateNoteCommand(Command):
    def __init__(self, notes, old_note, new_note):
        self.notes = notes
        self.old_note = old_note
        self.new_note = new_note

    def execute(self):
        self.notes.update(self.old_note, self.new_note)

    def undo(self):
        self.notes.update(self.new_note, self.old_note)


# Получатель, управляющий заметками
class Notes:
    def create(self, note):
        print(f"Creating note: {note}")
        # Добавить в базу данных

    def delete(self, note):
        print(f"Deleting note: {note}")
        # Удалить из базы данных

    def update(self, old_note, new_note):
        print(f"Updating note from {old_note} to {new_note}")
        # Обновить в базе данных


# Инициатор, вызывающий команды
class CommandManager:
    def __init__(self):
        self.history = []

    def execute_command(self, command):
        command.execute()
        self.history.append(command)

    def undo_command(self):
        if self.history:
            command = self.history.pop()
            command.undo()


# Клиентский код
if __name__ == "__main__":
    notes = Notes()
    manager = CommandManager()

    # Создание заметки
    create_cmd = CreateNoteCommand(notes, "Note 1")
    manager.execute_command(create_cmd)

    # Удаление заметки
    delete_cmd = DeleteNoteCommand(notes, "Note 1")
    manager.execute_command(delete_cmd)

    # Отмена удаления
    manager.undo_command()
