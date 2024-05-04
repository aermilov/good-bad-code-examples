from abc import ABC, abstractmethod

class FileSystemComponent(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def move(self, new_path):
        pass

    @abstractmethod
    def copy(self, new_path):
        pass

    @abstractmethod
    def delete(self):
        pass


class File(FileSystemComponent):
    def display(self):
        print(f"Файл: {self.name}")

    def move(self, new_path):
        print(f"Перемещение файла {self.name} в {new_path}")

    def copy(self, new_path):
        print(f"Копирование файла {self.name} в {new_path}")

    def delete(self):
        print(f"Удаление файла {self.name}")


class Folder(FileSystemComponent):
    def __init__(self, name):
        super().__init__(name)
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

if __name__ == '__main__':
    # Создаем файлы
    file1 = File("file1.txt")
    file2 = File("file2.txt")
    file3 = File("file3.txt")
    
    # Создаем папки
    folder1 = Folder("Folder 1")
    folder2 = Folder("Folder 2")
    
    # Добавляем файлы в папки
    folder1.add_child(file1)
    folder1.add_child(file2)
    folder2.add_child(file3)
    
    # Добавляем папки в другую папку
    main_folder = Folder("Main Folder")
    main_folder.add_child(folder1)
    main_folder.add_child(folder2)
    
    # Отображаем содержимое
    main_folder.display()
    
    # Перемещаем папку
    main_folder.move("/New Location")
    
    # Копируем папку
    main_folder.copy("/Backup")
    
    # Удаляем папку
    main_folder.delete()


