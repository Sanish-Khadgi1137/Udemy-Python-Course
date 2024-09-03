import smtplib

my_email = "www.khadgisanish9171@gmail.com"#e=f
#my_password = "password of my mail" after creating "App Password" replay my oringinal password with generated password as below
my_password = "gjyn evpl vswf idhi"

# #creating object form "SMTP()" class
# connection = smtplib.SMTP("smtp.gmail.com")
# #location of our email providers smtp serves; for gmail is "smtp.gmail.com"
# #for "hotmail" = "smtp.live.come"
# #for "yahoo" = "smtp.mail.yahoo.com"

# #starttls is for securing(encryption); tls = Transport Layer Security
# connection.starttls()

# #login to email provider
# connection.login(user=my_email, password=my_password)

# #send email
# connection.sendmail(from_addr=my_email, 
#                     to_addrs="1137sanishkhadgi@gmail.com", 
#                     #msg="hello sani") #save to spam
#                     #for no span
#                     msg= "Subject:Greeting \n\n This is the body of the mail"
# )

# connection.close()

#############333333333333333
#or auto closing

with smtplib.SMTP("smtp.gmail.com") as connection:

    connection.starttls()

    connection.login(user=my_email, password=my_password)

    connection.sendmail(
       
        from_addr=my_email, 
        to_addrs="1137sanishkhadgi@gmail.com", 
        msg= "Subject:Greeting \n\n This is the body of the mail"
    )
