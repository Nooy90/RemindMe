import smtplib, ssl

class Email():
    def __init__(self, email):
        self.email = email

    @staticmethod
    def email_information(to, message):
        try:
            server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            gmail_user = 'email@gmail.com'
            gmail_pass = 'password123'
            server_ssl.login(gmail_user, gmail_pass)
            server_ssl.sendmail(gmail_user, to, message)
            server_ssl.close()
        except Exception as e:
            write_error = open('log.txt', 'a')
            write_error.write(f'{e}\n')
            write_error.close()