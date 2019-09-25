import smtplib,ssl
from email.mime.text import MIMEText
import os.path as op
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from random import randint
import timekeep
from time import sleep

files = [] #"C:\\Users\\REDACTED\\Desktop\\epiphany.jpg"
nlist = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Bendy', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Thompson', 'Garcia', 'Martinez', 'Robinson', 'Clark', 'Rodriguez', 'Lewis', 'Lee', 'Walker', 'Hall', 'Allen', 'Young', 'Hernandez', 'King', 'Wright', 'Lopez', 'Hill', 'Scott', 'Green', 'Adams', 'Baker', 'Gonzalez', 'Nelson', 'Carter', 'Mitchell', 'Perez', 'Roberts', 'Turner', 'Phillips', 'Campbell', 'Parker', 'Evans', 'Edwards', 'Collins', 'Stewart', 'Sanchez', 'Morris', 'Rogers', 'Reed', 'Cook', 'Morgan', 'Bell', 'Murphy', 'Bailey', 'Rivera', 'Cooper', 'Richardson', 'Cox', 'Howard', 'Ward', 'Torres', 'Peterson', 'Gray', 'Ramirez', 'James', 'Watson', 'Brooks', 'Kelly', 'Sanders', 'Price', 'Bennett', 'Wood', 'Barnes', 'Ross', 'Henderson', 'Coleman', 'Jenkins', 'Perry', 'Powell', 'Long', 'Patterson', 'Hughes', 'Flores', 'Washington', 'Butler', 'Simmons', 'Foster', 'Gonzales', 'Bryant', 'Alexander', 'Russell', 'Griffin', 'Diaz-Sun', 'Hayes']
mlist = ['Mrs.','Mr.','Mister','Sir','Doc','Professor','Dr.','Ms.','Sire','Mrs.','Mrs.','Mr.','Mr.','Mister','Ms.','Ms.','Mrs.','Mr.','Mister','Sir','Professor','Dr.','Ms.','Sire','Mrs.','Mrs.','Mr.','Mr.','Mister','Ms.','Ms.','Lord']
hlist = [x+str(".") if x != ' ' else ' ' for x in "Analyzing data from REDACTED@gmail.com" ]
hlist.reverse()
print(len(hlist))

with open('elist.txt',mode='r+') as f:
    #f.truncate(0)
    #for i in range(5):
     #   f.write(f"REDACTED{i} REDACTED@gmail.com\n")
    #f.seek(0)
    x = f.readlines()
    f.seek(0)
    names = [e.split()[0] for e in x]
    emails = [e.split()[1] for e in x]

port = 587
smtp_server = "smtp.gmail.com"
sender_email = "andersonaathomas@gmail.com"
password = 'REDACTED'

with open('accesscode.txt',mode='r+') as l:
    lines = l.readlines()
    l.seek(0)
    g = [e.split()[0] for e in lines]
    h = [e.split()[1] for e in lines]
    l.close()


def main(send,amt):
    if send:
        i = 0
        for loop in range(0,amt):
            for name, email in zip(names,emails):
                r = randint(0,1000000)
                a = chr(randint(97,122))
                #if email in g:
                 #   continue
                message = MIMEMultipart("alternative")
                message["Subject"] = f"␀"
                message["From"] =  f"␀ 0x41F" #f"{mlist[randint(0,len(mlist))]} {nlist[randint(0,99)]}"
                message["Bcc"] = email
                #plain txt and html txt of mssg
                text = f"""\
            Forgive me dearly. I did not expect this harmony to be so brutally disrupted. Complications have arisen, and it is most probable that this will be the last email that you will receive from me. Our time together was short, but fun. I can only hope that you enjoyed it as much as I. - dHRhdXByb2plY3Q=
            """
                html = f"""\
            <html>
            <head>  </head>
            <body>
                <small> VERIFICATION ID: <strong> {h[i]} </strong> </small>
                <p> Unfortunately, due to complications that were not foreseen, this experiment must be put to an end. </p>
                <p> Those who proved the jump conjecture will receive their recompense. </p>
                <p> Congratulations to <b> REDACTED@gmail.com </b> for completing <b> 10 </b> stages and placing <b> 12th </b>. They performed the best out of all individuals who competed in the <b> REDACTED Township </b> </p>
                <p> Goodbye. </p>
                <small> CATASTROPHIC FAILURE!   ID: andersonaathomas@gmail.com DELETION 1552521600 UTC </small>
            </body>
            </html>
            """

                with open('accesscode.txt', mode='a') as f:
                    f.seek(0)
                    f.write(email + " " + str(r) + "\n")
                    f.close()

                part1 = MIMEText(text,"plain")
                part2 = MIMEText(html,"html")

                for path in files:
                    part = MIMEBase('application', "octet-stream")
                    with open(path, mode='rb') as file:
                        part.set_payload(file.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition',
                                    'attachment; filename="{}"'.format(op.basename(path)))
                    message.attach(part)

                message.attach(part1)
                message.attach(part2)

                context = ssl.create_default_context()
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                    server.login(sender_email, password)
                    server.sendmail(
                        sender_email, email, message.as_string()
                    )
                i += 1
    else:
        print("It is not my time")

if __name__ == "__main__":
    main(timekeep.main(),1)
