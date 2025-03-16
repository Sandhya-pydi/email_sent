import smtplib
import random
def read_data_send_mail():
    try:
        f=open('student_mails.txt',"r")
        student_mails=f.read()
        student_mails=student_mails.split(",")
        print(student_mails)
    except:
        print("file not available")

    sender_email="sandhyapydi630@gmail.com"

    for i in student_mails:
        otp_number=random.randint(00000,9999)
        print(otp_number)
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(sender_email, "xxxx xxxx xxxx xxxx") #this key differs from mail to mail
        # open settings> 
        message = f"Hi your OTP number is {otp_number}"
        try:
            s.sendmail(sender_email, i, message)
            print("mail sent sucessfully")
            s.quit()
        except:
            print("mail not sent")
read_data_send_mail()
