from abc import ABC, abstractmethod

class MessageProcessor(ABC):
    def process_message(self, message):
        self.parse_message(message)
        self.validate_message()
        self.send_message()
        self.log_message()

    @abstractmethod
    def parse_message(self, message):
        pass

    @abstractmethod
    def validate_message(self):
        pass

    @abstractmethod
    def send_message(self):
        pass

    def log_message(self):
        print("Message logged.")

# Конкретные классы для обработки различных типов сообщений

class EmailMessageProcessor(MessageProcessor):
    def parse_message(self, message):
        self.email_content = message
        print("Parsing email message...")

    def validate_message(self):
        print("Validating email message...")
        if "@" not in self.email_content:
            raise ValueError("Invalid email message: missing '@'")

    def send_message(self):
        print("Sending email message...")

class SMSMessageProcessor(MessageProcessor):
    def parse_message(self, message):
        self.sms_content = message
        print("Parsing SMS message...")

    def validate_message(self):
        print("Validating SMS message...")
        if len(self.sms_content) > 160:
            raise ValueError("Invalid SMS message: too long")

    def send_message(self):
        print("Sending SMS message...")

# Пример использования

def main():
    email_processor = EmailMessageProcessor()
    sms_processor = SMSMessageProcessor()

    email_message = "user@example.com: Hello, this is an email message!"
    sms_message = "Hello, this is an SMS message!"

    print("Processing Email message:")
    email_processor.process_message(email_message)

    print("\nProcessing SMS message:")
    sms_processor.process_message(sms_message)

if __name__ == "__main__":
    main()
