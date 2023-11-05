import sqlite3 as sq

class Sqlite:

    def __init__(self, database_file):

        self.db = sq.connect(database_file)
        self.cur = self.db.cursor()

        self.cur.execute("CREATE TABLE IF NOT EXISTS users (id INT, inv TEXT, lvl INT, config_sword TEXT, config_ech TEXT, coin INT, status TEXT)")
        self.db.commit()

    def create_profile(self, id):
        self.cur.execute(f"SELECT * FROM users WHERE id = {id}")
        existing_user = self.cur.fetchone()

        if existing_user is None:
            self.cur.execute(f"INSERT INTO users (id, inv, lvl, config_sword, config_ech, coin, status) VALUES ({id}, '', 1, '', '', 100, 'Игрок')")
            self.db.commit()
        else:
            print("Пользователь с таким ID уже существует.")

    def add_inv(self, id, drop):
        try:
            self.cur.execute('SELECT inv FROM users WHERE id=?', (id,))
            value = self.cur.fetchone()[0]
            new_inv = f"{value}\n {drop}\n"
            self.cur.execute('UPDATE users SET inv=? WHERE id=?', (new_inv, id))
            self.db.commit()
        except Exception as e:
            print(f"An error occurred: {e}")

    def return_inv(self, id):
        for value in self.cur.execute(f'SELECT inv FROM users WHERE id={id}'):
            return value[0]

    def clear_inventory(self, id):
        try:
            self.cur.execute("UPDATE users SET inv='' WHERE id=?", (id,))
            self.db.commit()
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    def add_lvl(self, id, experience):
        try:
            self.cur.execute('SELECT lvl FROM users WHERE id=?', (id,))
            current_level = self.cur.fetchone()[0]
            new_level = current_level + experience
            self.cur.execute('UPDATE users SET lvl=? WHERE id=?', (new_level, id))
            self.db.commit()
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    def set_config_sword(self, id, config):
        self.cur.execute('UPDATE users SET config_sword=? WHERE id=?', (config, id))
        self.db.commit()

    def set_config_enh(self, id, config):
        self.cur.execute('UPDATE users SET config_ech=? WHERE id=?', (config, id))
        self.db.commit()

    def return_config_sword(self, id):
        for value in self.cur.execute(f'SELECT config_sword FROM users WHERE id={id}'):
            return value[0]

    def return_config_enh(self, id):
        for value in self.cur.execute(f'SELECT config_ech FROM users WHERE id={id}'):
            return value[0]

    def return_lvl(self, id):
        for value in self.cur.execute(f'SELECT lvl FROM users WHERE id={id}'):
            return value[0]

    def return_coin(self, id):
        for value in self.cur.execute(f'SELECT coin FROM users WHERE id={id}'):
            return value[0]

    def return_status(self, id):
        for value in self.cur.execute(f'SELECT status FROM users WHERE id={id}'):
            return value[0]

    def add_coin(self, id, coins):
        try:
            self.cur.execute('SELECT coin FROM users WHERE id=?', (id,))
            current_coin = self.cur.fetchone()[0]
            new_level = current_coin + coins
            self.cur.execute('UPDATE users SET coin=? WHERE id=?', (new_level, id))
            self.db.commit()
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    def minus_coin(self, id, coins):
        try:
            self.cur.execute('SELECT coin FROM users WHERE id=?', (id,))
            current_coin = self.cur.fetchone()[0]
            new_level = current_coin - coins
            self.cur.execute('UPDATE users SET coin=? WHERE id=?', (new_level, id))
            self.db.commit()
        except Exception as e:
            print(f"Произошла ошибка: {e}")