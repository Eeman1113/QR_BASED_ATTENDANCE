import smtplib
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security
s.starttls()
# Authentication
s.login("eeman.majumder@gmail.com", "Eeman2003#")
# message to be sent
message = "A bot sent this message"
# sending the mail
s.sendmail("eeman.majumder@gmail.com", "anishrajmehta@gmail.com ", message)
# terminating the session
s.quit()