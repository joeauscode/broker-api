# from django.core.mail import send_mail
# from django.conf import settings

# def SendMail(email, fullname):
#     subject = "Welcome to Star Web"
#     message = f'''
# Welcome {fullname},

# This is a welcome message from the DevOps team.
# We want to specially thank you for registering with us.

# Best regards,
# Star Web Team
# '''

#     send_mail(
#         subject,
#         message,
#         settings.EMAIL_HOST_USER,
#         [email],  # only email addresses should go here
#         fail_silently=False,
#     )


from django.core.mail import send_mail
from django.conf import settings

def SendMail(to_email, fullname):
    subject = "Welcome to Our Service"
    message = f"Hello {fullname},\n\nThank you for registering with us!\n\nBest regards,\nYour Company"
    from_email = settings.DEFAULT_FROM_EMAIL  # Make sure to define this in your settings.py
    
    send_mail(subject, message, from_email, [to_email])
