import os
from pathlib import Path

class SeteupSecretEnv:

    username = None
    key = None
    secret_dir_path = Path('core/secret/')

    def ask_for_username(self):
        self.username = input("What is your jamf username?")

    def ask_for_key(self):
        self.key = input("What os your jamf key/password?")

    def take_care_of_secret_dir(self):
        if os.path.isdir(self.secret_dir_path):
            secret_dir = True
        else:
            os.mkdir(self.secret_dir_path)
            secret_dir = True

        return secret_dir

    def create_key_file(self):
        with open(Path(f'{self.secret_dir_path}/key.py'), 'w') as key_file:
            key_file.write(f"username = '{self.username}'\n")
            key_file.write(f"key = '{self.key}'")

    def main(self):
        self.ask_for_username()
        self.ask_for_key()
        self.take_care_of_secret_dir()
        self.create_key_file()


if __name__ == '__main__':
    SeteupSecretEnv().main()
