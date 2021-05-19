# Python code to illustrate Sending mail from
# your Gmail account
import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

sender_email_id = '123jhghfuiakh@gmail.com'
receiver_email_id = 'hjkzkhkz@gmail.com'

# start TLS for security
s.starttls()

# Authentication
s.login(sender_email_id, sender_email_id)
# message to be sent
message = "a quick brown fox jumps over the lazy dog."

# sending the mail

for i in range(100):

    s.sendmail(sender_email_id, receiver_email_id, message)

# terminating the session
s.quit()
