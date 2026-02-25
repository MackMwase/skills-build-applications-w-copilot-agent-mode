"""
populate_db.py - Script to create test data for Octofit Tracker

Usage:
    python manage.py shell < octofit_tracker/populate_db.py
"""

from django.contrib.auth import get_user_model
from octofit_tracker import settings

User = get_user_model()

# Create test users
def create_test_users():
    users_data = [
        {"username": "alice", "email": "alice@example.com", "password": "testpass123"},
        {"username": "bob", "email": "bob@example.com", "password": "testpass123"},
        {"username": "carol", "email": "carol@example.com", "password": "testpass123"},
    ]
    for user_data in users_data:
        if not User.objects.filter(username=user_data["username"]).exists():
            user = User.objects.create_user(
                username=user_data["username"],
                email=user_data["email"],
                password=user_data["password"]
            )
            print(f"Created user: {user.username}")
        else:
            print(f"User {user_data['username']} already exists.")

if __name__ == "__main__":
    create_test_users()
else:
    create_test_users()
