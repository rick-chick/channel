from pydantic import ValidationError


class BusinessException(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class ValidationException(BusinessException):
    def __init__(self, error: ValidationError):
        super().__init__("invalid_input")


class UnauthorizedException(BusinessException):
    def __init__(self):
        super().__init__("unauthorized")


class UserExistsException(BusinessException):
    def __init__(self):
        super().__init__("user_exists")


class UserNotFoundException(BusinessException):
    def __init__(self):
        super().__init__("user_not_found")


class UnauthenticateException(BusinessException):
    def __init__(self):
        super().__init__("unauthenticated")


class RecordExistsException(BusinessException):
    def __init__(self):
        super().__init__("record_exists")


class ChannelNotFoundException(BusinessException):
    def __init__(self):
        super().__init__("channel_not_found")


class InvalidSignupTokenException(BusinessException):
    def __init__(self):
        super().__init__("invalid_signup_token")
