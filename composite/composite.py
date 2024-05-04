class File:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Файл: {self.name}")

    def move(self, new_path):
        print(f"Перемещение файла {self.name} в {new_path}")

    def copy(self, new_path):
        print(f"Копирование файла {self.name} в {new_path}")

    def delete(self):
        print(f"Удаление файла {self.name}")


class Folder:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def display(self):
        print(f"Папка: {self.name}")
        for child in self.children:
            child.display()

    def move(self, new_path):
        print(f"Перемещение папки {self.name} в {new_path}")
        for child in self.children:
            child.move(new_path)

    def copy(self, new_path):
        print(f"Копирование папки {self.name} в {new_path}")
        for child in self.children:
            child.copy(new_path)

    def delete(self):
        print(f"Удаление папки {self.name} и всех её содержимых")
        for child in self.children:
            child.delete()
        self.children.clear()