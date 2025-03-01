import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EventAPI.settings')
django.setup()

from users.models import CustomUser
from django.contrib.auth.hashers import make_password

def create_users():
    """Creates an admin user and a normal user if they don't exist"""

    if not CustomUser.objects.filter(username="admin").exists():
        CustomUser.objects.create(
            username="admin",
            password=make_password("password"),
            role="Admin",
            is_superuser=True,
            is_staff=True
        )
        print("Admin user created successfully!")

    else:
        print("Admin user already exists!")

    if not CustomUser.objects.filter(username="user").exists():
        CustomUser.objects.create(
            username="user",
            password=make_password("password"),
            role="User"
        )
        print("Normal user created successfully!")

    else:
        print("Normal user already exists!")

if __name__ == "__main__":
    create_users()
