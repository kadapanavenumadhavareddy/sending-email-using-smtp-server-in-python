import smtplib
mail=smtplib.SMTP("smtp.gmail.com",587)
mail.ehlo()
mail.starttls()
# make sure that turn on the Less secure app access in sender mail id browser
#if not open the link  https://myaccount.google.com/lesssecureapps and turn the Less secure app access
# if u forget to turn it on it will show the below error
#-------------------------------------------------------------------------------------------------------------------------------------------
#Traceback (most recent call last):
#  File "V:\python speech\sending mail.py", line 11, in <module>
#   mail.login(g,p)
#File "C:\Users\venum\AppData\Local\Programs\Python\Python37\lib\smtplib.py", line 730, in login
# raise last_exception
#File "C:\Users\venum\AppData\Local\Programs\Python\Python37\lib\smtplib.py", line 721, in login
 # initial_response_ok=initial_response_ok)
#File "C:\Users\venum\AppData\Local\Programs\Python\Python37\lib\smtplib.py", line 642, in auth
# raise SMTPAuthenticationError(code, resp)
#smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials z14sm40937714pfn.161 - gsmtp')
g=input("enter sender mail ID:")
p=input("enter the sender mail password:")
message=str(input("enter the message u need to send:"))
r=input("enter receiver mail ID:")
mail.login(g,p)
mail.sendmail(g,r,message)
mail.close()
print("mail send succesfully")

