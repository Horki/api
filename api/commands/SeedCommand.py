import random
from flask_script import Command
from faker import Factory
from api.app import db
from api.app.models.User import User
from api.app.models.Book import Book


class SeedCommand(Command):
    def __init__(self):
        self.emails = []
        self.users = []
        self.faker = Factory.create('hr_HR')

    def run(self):
        try:
            print("Adding mock users")
            for _ in range(1, 10):
                user = User(
                    username=self.faker.name(),
                    password='123456',
                    email=self.__unique_email(),
                    active=True)
                self.users.append(user)
                db.session.add(user)

            print("Add mock books")
            for _ in range(1, 20):
                book = Book(
                    title=self.faker.sentence(nb_words=4),
                    author=self.faker.name(),
                    user=random.choice(self.users)
                )
                db.session.add(book)

            db.session.commit()

        except BaseException as error:
            print(error)
            db.session.rollback()

    def __unique_email(self):
        email = self.faker.email()
        if email in self.emails:
            return self.__unique_email()
        self.emails.append(email)
        return email
