from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def save(self, content):
        pass


class PDFDocument(Document):
    def save(self, content):
        print(f"Saving PDF document with content: {content}")

class WordDocument(Document):
    def save(self, content):
        print(f"Saving Word document with content: {content}")

class TXTDocument(Document):
    def save(self, content):
        print(f"Saving TXT document with content: {content}")

class DocumentCreator(ABC):
    @abstractmethod
    def create_document(self):
        pass

class PDFCreator(DocumentCreator):
    def create_document(self):
        return PDFDocument()

class WordCreator(DocumentCreator):
    def create_document(self):
        return WordDocument()

class TXTCreator(DocumentCreator):
    def create_document(self):
        return TXTDocument()

def client_code(creator: DocumentCreator):
    document = creator.create_document()
    document.save("Hello, World!")


def create():
    creator_type = 'pdf'
    creator: DocumentCreator = None

    match (creator_type):
        case 'pdf':
            creator = PDFCreator()
        case 'word':
            creator = WordCreator()
        case 'txt':
            creator = TXTCreator()

    return creator.create_document()

if __name__ == "__main__":
    creator = create()
    client_code(creator)
