#13. Send reminder emails and text notifications
import smtplib
server = smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("srinithachinthala4@gmail.com","srinitha@11")
server.sendmail("srinithachinthala4@gmail.com",
                "ginnarapuprasad@gmail.com",
                "hello how are you")
server.quit()
