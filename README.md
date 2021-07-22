# WebsiteChanges
This script monitors any particular URL and if there are any modifications, it sends Email Notification to the receiver.

Steps to use:
1. Download in local.
2. Open config file.
3. Replace with your email and password.
4. Find below 3 lines and make alterations as per requirement (2 times in code)
msg['To'] = email.utils.formataddr(('The Recipient', 'receiver@email.com')) ##Enter the receiver's id
msg['From'] = email.utils.formataddr(('Sender Name', 'sender_email@gmail.com')) ##Enter the same email id as in config file
server.sendmail('sender_email@gmail.com', ['receiver@email.com'], msg.as_string()) ##Enter the same details as in the above two lines
5. Host the script or Run in Local.
