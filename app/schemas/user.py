from pydantic import BaseModel

'''
    Pydantic models - their purpose is to define how JSON looks in API
'''


class SignupRequest(BaseModel):
    firstName: str
    lastName: str
    email: str
    password: str
    confirmPassword: str


class LoginRequest(BaseModel):
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    firstName: str
    lastName: str
    email: str
