import smtplib

sender_email = "jackfrostbyte799@gmail.com"
rec_email = "Fernandzerom@gmail.com"
password = input(str("Password:"))
message = "HEY!"

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email,password)
server.sendmail(sender_email,rec_email,message)
print("success!")