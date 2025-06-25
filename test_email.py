import os
from dotenv import load_dotenv
from django.core.mail import send_mail

load_dotenv()

# Set up Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

import django
django.setup()

send_mail(
    subject="✅ Test Email from Appointment Booking",
    message="This is a test email from your Django app.",
    from_email=os.getenv("EMAIL_HOST_USER"),
    recipient_list=["your_email@gmail.com"],  # ✅ Change to your target email
    fail_silently=False,
)

print("Email sent.")
