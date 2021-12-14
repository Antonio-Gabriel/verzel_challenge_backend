from django.conf import settings
from datetime import datetime, timedelta
import jwt


def generate_access_token(user_data):

    payload = {
        "username": user_data,
        "exp": datetime.utcnow() + timedelta(days=1, minutes=0),
        "iat": datetime.utcnow(),
    }

    return jwt.encode(payload, 'secret_key', algorithm="HS256")
