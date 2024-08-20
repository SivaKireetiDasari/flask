from itsdangerous import URLSafeSerializer
from key import salt,secret_key
def token(data):
    Serializer=URLSafeSerializer(secret_key)
    return Serializer.dumps(data,salt=salt)
def dtoken(data):
    serializer=URLSafeSerializer(secret_key)
    return serializer.loads(data,salt=salt)