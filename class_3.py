from flask import Flask

from data import db_session

from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars.db")

    user = User()
    user.surname = 'Scott'
    user.name = 'Ridley'
    user.age = 21
    user.position = 'captain'
    user.speciality = 'research engineer'
    user.address = 'module_1'
    user.email = 'scott_chief@mars.org'

    user2 = User()
    user2.surname = 'Test'
    user2.name = 'Test'
    user2.age = 10 ** 10
    user2.position = 'tester'
    user2.speciality = 'teste'
    user2.address = 'test_0'
    user2.email = 'test@mars.org'

    user3 = User()
    user3.surname = 'Roitenberg'
    user3.name = 'Daniil'
    user3.age = 15
    user3.position = 'noname'
    user3.speciality = 'prgrammer'
    user3.address = 'hose'
    user3.email = 'danya@mars.org'

    sess = db_session.create_session()
    sess.add(user)
    sess.add(user2)
    sess.add(user3)
    sess.commit()

if __name__ == '__main__':
    main()
