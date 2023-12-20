from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

password = 'adminpassword'
password_hash = '$2b$12$wuEY/GY7eGu0qxtPTiMmrOU2ByGm8Vf7mKguosznP22HTU0rVkjWu'

print(pwd_context.hash(password))
print(pwd_context.verify(password, password_hash))
