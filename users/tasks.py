# from celery import shared_task
# from django.core.mail import send_mail
# from .models import CustomUser
#
# @shared_task
# def send_welcome_email(user_id):
#     user = CustomUser.objects.get(id=user_id)
#     send_mail('Welcome to Our E-commerce Platform',
#               f'Hello {user.name}, welcome to our E-commerce Platform',
#               'from@example.com',
#               [user.email],
#               fail_silently=False,
#               )
#
#
#
#
#
#
#
