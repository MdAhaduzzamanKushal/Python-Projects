import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText  # Add this import statement
from email import encoders

sender_email = "kushal.tay@gmail.com"
sender_password = "Give mail password"
recipient_email = "ahk.kushal@gmail.com"
subject = "Email using python"
body = "Download the attachment"

# Path to the file
file_path = r"F:\Security mind pro\Assignment\Python Projects\Send email in python\Exploit vurnerable machines.pdf"

# Read the file content
with open(file_path, "rb") as file:
    file_content = file.read()

# Create a multipart message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = recipient_email
message["Subject"] = subject

# Add body to email
message.attach(MIMEText(body, "plain"))

# Attach the file content
attachment = MIMEBase("application", "octet-stream")
attachment.set_payload(file_content)
encoders.encode_base64(attachment)
attachment.add_header(
    "Content-Disposition",
    f"attachment; filename=Exploit vurnerable machines.pdf",
)
message.attach(attachment)

# Connect to SMTP server and send email
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, message.as_string())

print("Email sent successfully!")
