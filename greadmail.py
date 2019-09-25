import imaplib, email, os

user = 'andersonaathomas@gmail.com'
password = 'REDACTED'
imap_url = 'imap.gmail.com'
attachment_dir ='C:\\Users\\REDACTED\\Desktop\\attachdir'

def auth(user,password,imap_url):
    con = imaplib.IMAP4_SSL(imap_url)
    con.login(user,password)
    return con

con = auth(user,password,imap_url)
con.select("INBOX")

x = 10  #picks 10 emails, change for more.
result, data = con.fetch(f"{x}",'(RFC822)')


def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    return msg.get_payload(None,True)

def search(key,value,con):
    result, data = con.search(None,key,'"{}"'.format(value))
    return data

def get_emails(result_bytes):
    msgs = []
    for num in result_bytes[0].split():
        typ, data = con.fetch(num,'(RFC822)')
        msgs.append(data)
    return msgs

def get_attachments(msg):
    for part in msg.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get("Content-Disposition") is None:
            continue
        fileName = part.get_filename()

        if bool(fileName):
            filePath = os.path.join(attachment_dir, fileName)
            with open(filePath,'wb') as f:
                f.write(part.get_payload(decode=True))


raw = email.message_from_bytes(data[0][-1])

mylist = list(str(get_body(raw)))

for x in range(len(get_body(raw))):
    if x % 130 == 0:
      mylist.insert(x,"\n")

print(''.join(mylist))
for msg in get_emails(search("FROM",'REDACTED@gmail.com',con)):
    pass
   # print("\n")
    #print(get_body(email.message_from_bytes(msg[0][1])))

 
