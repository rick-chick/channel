DATABASE_URL = 'postgresql+pg8000://channel:password@127.0.0.1:5432/channel'
ALLOWD_ORIGINS = '[http://127.0.0.1:4200, http://localhost:4200]'

try:
    from channel.driver.env_local import (
        GMAIL_ACCOUNT,
        GMAIL_PASSWORD,
        PASSWORD_RESET_URL
    )
except ImportError:
    GMAIL_ACCOUNT = '***'
    GMAIL_PASSWORD = '***'
    PASSWORD_RESET_URL = '***'
