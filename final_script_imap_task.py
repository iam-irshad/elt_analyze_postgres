
# import imaplib
# import email
# from datetime import datetime

# USERNAME = "mohammad.irshad@truthics.com"
# PASSWORD = "wkhjmhsqjzwpfxqs"
# SUBJECT = "CSV 2023 File Attachment"
# SENDER_EMAIL =  "mohammad.irshad@truthics.com"

# LOGIN_WITH_EMAIL = imaplib.IMAP4_SSL("imap.gmail.com")
# LOGIN_WITH_EMAIL.login(USERNAME, PASSWORD)
# # LOGIN_WITH_EMAIL
# # LOGIN_WITH_EMAIL.select("inbox")
# # today = datetime.today().strftime('%d-%b-%Y')
# # status, message_numbers = LOGIN_WITH_EMAIL.search(None, f'(SINCE "{today}")')

# def check_for_latest_email():
#     LOGIN_WITH_EMAIL
#     LOGIN_WITH_EMAIL.select("inbox")
#     today = datetime.today().strftime('%d-%b-%Y')
#     status, message_numbers = LOGIN_WITH_EMAIL.search(None, f'(SINCE "{today}")')
#     # global status, message_numbers
#     for message in message_numbers:
#         if len(message)>0:
#         # Get the list of message numbers
#             message_numbers = message_numbers[0].split()
#             # Loop through the message numbers and fetch the email data
#             for msg_num in message_numbers:
#                 status, msg_data = LOGIN_WITH_EMAIL.fetch(msg_num, "(RFC822)")
#                 raw_email = msg_data[0][1]
#                 msg = email.message_from_bytes(raw_email)
#             email_sub = msg.get("Subject")
#             sender_id = msg.get("From")
#             # print(email_sub, sender_id)
#             if email_sub == SUBJECT and sender_id == SENDER_EMAIL:
#                 return True 
#         # Logout and close the connection
#         # LOGIN_WITH_EMAIL.logout() ### if i try to check present day ki 2 mail than ye line error de rhi h or comment karne per shi output aa rha hai.and mail agar 1 hi aayi hai tab ye line uncommet karne per bhi theek run ho rha hai.
#             else:
#                 return "There is no email receive today from this id :",SENDER_EMAIL

# print(check_for_latest_email())

    






# # # # # import imaplib
# # # # # import email
# # import os
# # # # # from datetime import datetime

# # # # Your Gmail credentials
# # # username = "mohammad.irshad@truthics.com"
# # # password = "wkhjmhsqjzwpfxqs"

# # # # Connect to the Gmail IMAP server
# # # mail = imaplib.IMAP4_SSL("imap.gmail.com")
# # # mail.login(username, password)

# # # # Select the inbox folder
# # # mail.select("inbox")

# # # # Define the date format for comparison
# # # today = datetime.today().strftime('%d-%b-%Y')

# # # # Search for emails received today
# # # status, message_numbers = mail.search(None, f'(SINCE "{today}")')

# # # # Get the list of message numbers
# # # message_numbers = message_numbers[0].split()

# # # # Define a directory to save attachments

# # # download_dir = "attachments" 


# # # os.makedirs(download_dir, exist_ok=True)

# # # # Loop through the message numbers and fetch the email data
# # # for msg_num in message_numbers:
# # #     status, msg_data = mail.fetch(msg_num, "(RFC822)")
# # #     raw_email = msg_data[0][1]
# # #     msg = email.message_from_bytes(raw_email)
    
# # #     # Print subject and sender
# # #     subject = msg.get('Subject')

# # #     if subject == "CSV 2023 File Attachment":
# # #         # print(subject)
# # #     # print(f"Subject: {msg['Subject']}")
# # #     # print(f"From: {msg['From']}")

# # #     # Iterate through email parts
# # #         for part in msg.walk():
# # #             if part.get_content_maintype() == 'multipart':
# # #                 continue
# # #             if part.get('Content-Disposition') is None:
# # #                 continue

# # #             # Save the attachment
# # #             filename = part.get_filename()
# # #             if filename:
# # #                 filepath = os.path.join(download_dir, filename)
# # #                 with open(filepath, 'wb') as file:
# # #                     file.write(part.get_payload(decode=True))

# # #                 print(f"Attachment saved: {filepath}")

# # # # Logout and close the connection
# # # mail.logout()




 




# # def download_attachment():
# #     global status, message_numbers
# #     # Connect to the Gmail IMAP server
# #     # LOGIN_WITH_EMAIL

# #     # Select the inbox folder
# #     # LOGIN_WITH_EMAIL.select("inbox")

# #     # # Define the date format for comparison
# #     # today = datetime.today().strftime('%d-%b-%Y')

# #     # # Search for emails received today
# #     # status, message_numbers = LOGIN_WITH_EMAIL.search(None, f'(SINCE "{today}")')

# #     # # Get the list of message numbers
# #     message_numbers = message_numbers[0].split()
# #     # print(status,message_numbers)

# #     # Define a directory to save attachments

# #     download_dir = "attachments" 


# #     os.makedirs(download_dir, exist_ok=True)

# #     # Loop through the message numbers and fetch the email data
# #     for msg_num in message_numbers:
# #         status, msg_data = LOGIN_WITH_EMAIL.fetch(msg_num, "(RFC822)")
# #         raw_email = msg_data[0][1]
# #         msg = email.message_from_bytes(raw_email)
    
# #         # Print subject and sender
# #         subject = msg.get('Subject')
# #         sender_id = msg.get("From")
# #         print(subject)
# #         if subject == SUBJECT and sender_id == SENDER_EMAIL:
# #             # print("1")
            
# #             # print(subject)
# #         # print(f"Subject: {msg['Subject']}")
# #         # print(f"From: {msg['From']}")

# #         # Iterate through email parts
# #             for part in msg.walk():
# #                 if part.get_content_maintype() == 'multipart':
# #                     continue
# #                 if part.get('Content-Disposition') is None:
# #                     continue

# #                 # Save the attachment
# #                 filename = part.get_filename()
# #                 if filename:
# #                     filepath = os.path.join(download_dir, filename)
# #                     with open(filepath, 'wb') as file:
# #                         file.write(part.get_payload(decode=True))

# #                     print(f"Attachment saved: {filepath}")
# #                     # print("2")

# #     # Logout and close the connection
# #     LOGIN_WITH_EMAIL.logout()



# # # download_attachment()




# # # if check_for_latest_email() is True:
# # #     print("HLO")
# # #     download_attachment()
# # #     # print("hello")















import imaplib
import email
import os
from datetime import datetime
import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

 

USERNAME = "mohammad.irshad@truthics.com"
PASSWORD = "wkhjmhsqjzwpfxqs"
SENDER_EMAIL = "arshad tasleem <arshadtasleem83@gmail.com>"
GIVEN_EMAIL_SUBJECT = "CSV 2023 File Attachment"

def check_for_latest_email():
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(USERNAME, PASSWORD)
    mail.select("inbox")
    today = datetime.today().strftime('%d-%b-%Y')
    status, message_numbers = mail.search(None, f'(SINCE "{today}")')
    for message in message_numbers:
        if len(message)>0:
        # Get the list of message numbers
            message_numbers = message_numbers[0].split()
        # print(message_numbers)
        # Loop through the message numbers and fetch the email data
            for msg_num in message_numbers:
                status, msg_data = mail.fetch(msg_num, "(RFC822)")
                raw_email = msg_data[0][1]
                msg = email.message_from_bytes(raw_email)
                received_email_sub = msg.get("Subject")
                # print(received_email_sub)
                received_email_message_id = msg.get("Message-ID")
                # print(received_email_message_id)
                received_email_sender_id = msg.get("From")
                # print(received_email_sender_id)
                if received_email_sender_id == SENDER_EMAIL and received_email_sub == GIVEN_EMAIL_SUBJECT:
                    # print(received_email_message_id,received_email_sub,received_email_sender_id)
                    return  True,received_email_message_id, received_email_sender_id
        else:
            return False, None, None
                    # print('hello')
                    # print("There is no email receive today from this sender id:",SENDER_EMAIL)
                
        
        # else:
        #     return False, None, None


print(check_for_latest_email())


# get_true_or_false , received_mess_id , received_mess_sender_id = check_for_latest_email()
# print(received_mess_id)
# print(get_true)
    






# def download_attachment(message_id):
#     # message_id = received_mess_id
#     # Connect to the Gmail IMAP server
#     mail = imaplib.IMAP4_SSL("imap.gmail.com")
#     mail.login(USERNAME, PASSWORD)

#     # Select the inbox folder
#     mail.select("inbox")

#     # Define the date format for comparison
#     today = datetime.today().strftime('%d-%b-%Y')

#     # Search for emails received today
#     status, message_numbers = mail.search(None, f'(SINCE "{today}")')

#     # Get the list of message numbers
#     message_numbers = message_numbers[0].split()

#     # Define a directory to save attachments

#     download_dir = "attachments" 


#     os.makedirs(download_dir, exist_ok=True)

#     # Loop through the message numbers and fetch the email data
#     for msg_num in message_numbers:
#         status, msg_data = mail.fetch(msg_num, "(RFC822)")
#         raw_email = msg_data[0][1]
#         msg = email.message_from_bytes(raw_email)
    
#         # Print subject and sender
#         msg_id = msg.get('Message-ID')
#         if msg_id == message_id:
#             print(msg_id, message_id)
     
#         # Iterate through email parts
#             for part in msg.walk():
#                 if part.get_content_maintype() == 'multipart':
#                     continue
#                 if part.get('Content-Disposition') is None:
#                     continue

#                 # Save the attachment
#                 filename = part.get_filename()
#                 if filename:
#                     filepath = os.path.join(download_dir, filename)
#                     with open(filepath, 'wb') as file:
#                         file.write(part.get_payload(decode=True))

#                     print(f"Attachment saved: {filepath}")



# # download_attachment(received_mess_id)



# # if check_for_latest_email() is get_true , received_mess_id , received_mess_sender_id is True:
# #     download_attachment(received_mess_id)
# #     print("hello")









# first_file_path = "C:\\Users\\Irshad\\attachments\\idera.csv"
# second_file_path = "C:\\Users\\Irshad\\attachments\\qubole.csv"

# def combine_data(file_path1,file_path2):

#     file_1 = open(file_path1,"r")
#     file_2 = open(file_path2,"r")

#     read_file_1 = csv.DictReader(file_1)
#     read_file_2 = csv.DictReader(file_2)
    
#     my_file_1 = list(read_file_1)
#     my_file_2 = list(read_file_2)

#     field_name = ["id","name","customer_id","organization_id","engagement_type_id","engagement_date","salesforce_id","reseller","email_domains","salesforce_id "]
#     result = []
#     for dictionary in my_file_1:                          
#         # print(dictionary)
#         for line in my_file_2:
#             if dictionary['name'] == line['name']:
#                 salesforce_id = dictionary['salesforce_id']
#                 line.update(key=salesforce_id)
#                 result.append(line)
#                 break



#     with open("C:\\Users\\Irshad\\new_marge_file.csv","w",newline='') as meri_file:
#         write_data = csv.DictWriter(meri_file, fieldnames= field_name)
#         write_data.writeheader()
#         for row in result:
#             # print(row)
#             row["salesforce_id "] = row.pop("key") # ye line me key name change kiya hai name 'key' change into 'salesforce_id '
#             write_data.writerow(row)


# # combine_data(first_file_path, second_file_path)


# # get_true , received_mess_id , received_mess_sender_id = check_for_latest_email()








# file_path_for_reply = "C:\\Users\\Irshad\\new_marge_file.csv"

# def send_combined_data_as_reply():

#     mail = imaplib.IMAP4_SSL("imap.gmail.com")
#     mail.login(USERNAME, PASSWORD)

#     # Select the inbox folder
#     mail.select("inbox")

#     # Define the date format for comparison
#     today = datetime.today().strftime('%d-%b-%Y')


#     # Search for emails received today
#     status, message_numbers = mail.search(None, f'(SINCE "{today}")')

#     # Get the list of message numbers
#     message_numbers = message_numbers[0].split()

#     # Create a reply email
#     reply_email = MIMEMultipart()
#     reply_email['From'] = received_mess_sender_id

#     for msg_num in message_numbers:
#         status, msg_data = mail.fetch(msg_num, "(RFC822)")
#         raw_email = msg_data[0][1]
#         msg = email.message_from_bytes(raw_email)
    
#         # Print subject and sender
#         subject = msg.get('Subject')
#         # print(f"email-subject: {subject}")

#         # Extract Message-ID
#         message_id = msg.get('Message-ID')
#         # print(f"Message-ID: {message_id}")

#         sender_email = msg.get("From")
#         # print(f"sender-email: {sender_email}")

#         if message_id == received_mess_id:

#         # receiver_email = received_mess_sender_id
#         # print(f"receiver-email: {receiver_email}")

#             with open(file_path_for_reply, "rb") as f:
#                 part = MIMEApplication(f.read(), Name=os.path.basename(file_path_for_reply))
#                 part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file_path_for_reply))
#                 reply_email.attach(part)

#             # Set email headers for the reply
#             reply_email['To'] = sender_email
#             reply_email['Subject'] = "Re: " + subject
#             reply_email['In-Reply-To'] = message_id

#             # Connect to the SMTP server and send the email
#             smtp_server = "smtp.gmail.com"
#             smtp_port = 587
#             with smtplib.SMTP(smtp_server, smtp_port) as server:
#                 server.starttls()
#                 server.login(USERNAME, PASSWORD)
#                 server.sendmail(received_mess_sender_id, sender_email, reply_email.as_string())
#                 print("Email sent successfully.")

#         # Logout and close the connection
#         mail.logout()


# # send_combined_data_as_reply()



# get_true_or_false , received_mess_id , received_mess_sender_id = check_for_latest_email()

# # def main():
# #     if get_true_or_false:
# #         print("message received")
# #         download_attachment(received_mess_id)
# #         print("attachment downloded")
# #         combine_data(first_file_path,second_file_path)
# #         print("file created")
# #         send_combined_data_as_reply()
# #         print("your email reply is send successfully")
# #     else:
# #         get_true_or_false is False
# #         print("something wrong in this")


# # if __name__ == "__main__":
# #     main()

