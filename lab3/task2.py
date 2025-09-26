import re

def Regex_Log_Cleaner():
    with open("access.log", "w") as log_file:
        log_file.write("adbdo@gmail.com ucsad\n")
        log_file.write("rafat-email@@comgas bdsgv\n")
        log_file.write("us1.doe@outlook.com asv\n")
        log_file.write("vvcxa wrong line\n")
        log_file.write("asfsadqw@yahoo.com $ asd\n")
        log_file.write("vvdsa@vasad.asdasd\n")
        log_file.write("test.user@company.orgok\n")
        log_file.write("no-sasasa-here\n")
        log_file.write("vvvdsa@my-site.asdkasdasdas\n")
        log_file.write("anoasdsather_invalid_string\n")

    with open("access.log", "r") as log_file:
        text = log_file.read()

    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    emails = re.findall(email_pattern, text)

    unique_emails = set(emails) #remove duplicates

    with open("valid_emails.txt", "w") as valid_file:
        for email in unique_emails:
            valid_file.write(email + "\n")

    print(f" {len(unique_emails)} unique valid emails.")

