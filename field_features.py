from pydantic import BaseModel, Field

class User(BaseModel):
    id: int 
    name: str
    email: str
    age: int
    
user = User(id=1, name="John Doe", email="john.doe@example.com", age=30)

print(user)

#DEFAULT VALUES

class User(BaseModel):
    id: int 
    name: str = "ENES" 
    email: str 
    age: int = 22
    
user = User(id=1, name="John Doe", email="john.doe@example.com", age=30)
user = User(id=1,email="enes@example.com")
print(user)

#FIELD FEATURES

# ? gt: greater than
# ? lt: less than
# ? ge: greater than or equal to
# ? le: less than or equal to

class User(BaseModel):
    id: int 
    name: str
    email: str 
    age: int = Field(gt=18, lt=30)
    
user = User(id=1, name="John Doe", email="john.doe@example.com", age=30)
user = User(id=1, name="John Doe", email="john.doe@example.com", age=17)
user = User(id=1, name="John Doe", email="john.doe@example.com", age=25)


#TEXT FIELD FEATURES

class User(BaseModel):
    username: str = Field(min_length=3)
    bio: str = Field(max_length=10)
    phone_number: str = Field(pattern=r'^\d*$') #REGEX
    
user = User(username="john", bio="developer", phone_number="1234567890")
#will s all error messages
invalid_user = User(username="jo", bio="this bio is way too long for the field", phone_number="ABC") # This will raise a validation error


#NUMERIC FIELD FEATURES decimal


from decimal import Decimal

class User(BaseModel):
    account_balance: Decimal = Field(max_digits=5, decimal_places=2)

user = User(account_balance=Decimal('123.45'))
user = User(account_balance=Decimal("123.456")) # This will raise a validation error
user = User(account_balance=Decimal('12456')) # This will raise a validation error

