import smtplib
from password import my_password

my_email = "tomfizzlery@gmail.com"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=my_password)
connection.sendmail(from_addr=my_email, to_addrs="tiddlefizzlery@yahoo.com", msg="Hello")
connection.close()
