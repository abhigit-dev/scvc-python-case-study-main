from pydantic import BaseModel, Field, field_validator
from datetime import date

class CustomerBase(BaseModel):
    name: str
    email: str
    age: int

class CustomerCreate(CustomerBase):
    signup_date: date

    @field_validator('signup_date')
    def signup_date_must_be_today_or_earlier(cls, v):
        if v > date.today():
            raise ValueError('signup date must be today or earlier')
        return v

class CustomerUpdate(CustomerBase):
    pass

class Customer(CustomerBase):
    id: int
    signup_date: date

    class Config:
        from_attributes = True
