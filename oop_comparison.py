from pydantic import BaseModel
import json

#Pydantic Model

class User(BaseModel):
    id: int
    name: str
    email: str
    age: float
    
user = User(id=1, name="John Doe", email="john.doe@example.com", age=30)

#OOP Model

class TraditionalUser:
    def __init__(self, id: int, name: str, email: str, age: float):
        self.id = id
        self.name = name
        self.email = email
        self.age = float(age)       
    #Bu sayede nesneyi yazdırırken okunabilir ve anlamlı bir format elde edilir.
    #Eğer __str__ metodunu tanımlamazsan, Python nesneyi yazdırırken aşağıdaki gibi bir varsayılan gösterim kullanır:
    #<__main__.User object at 0x105ce4f40>

    def __str__(self):
        return f"TraditionalUser(id={self.id}, name='{self.name}', email='{self.email}', age={self.age})"
    
traditional_user = TraditionalUser(id=1, name="John Doe", email="john.doe@example.com", age=30)

user = User(id=1, name="John Doe", email="john.doe@example.com", age=30)



# ? ----------------------------------------------------------
# ?                   COMPARISON NOTES                        
# ? ----------------------------------------------------------
# ? 1. Pydantic provides automatic validation based on type hints
# ? 2. Traditional OOP requires manual validation if needed
# ? 3. Pydantic models have built-in serialization/deserialization
# ? 4. Both approaches allow for attribute updates after creation

# ----------------------------------------------------------
#                 UPDATING VALUES COMPARISON                
# ----------------------------------------------------------

# Updating Pydantic model values
user.name = "Jane Smith"
user.age = 35
print(f"Updated Pydantic user: {user}")

# Updating Traditional OOP model values
traditional_user.name = "Jane Smith"
traditional_user.age = 35
print(f"Updated Traditional user: {traditional_user}")

#INVALİD INPUTS

#Pydantic Model    
#Hata veriyor. Doğrulama yapıyor
user = User(id=1, name="John Doe", email="john.doe@example.com", age="thirty")                

#Traditional OOP Model
#Hata vermiyor. Doğrulama yapmıyor
traditional_user = TraditionalUser(id=1, name="John Doe", email="john.doe@example.com", age="thirty")


#WRONG DATA TYPE

#Pydantic Model
#Integer 30'u Float 30.0'a çeviriyor
user = User(id=1, name="John Doe", email="john.doe@example.com", age=30)
print(type(user.age))

#Traditional OOP Model
#Hata vermiyor. Doğrulama yapmıyor
#Tip float ama  int kabul ediyor.
traditional_user = TraditionalUser(id=1, name="John Doe", email="john.doe@example.com", age=30)
print(type(traditional_user.age))





#SERIALIZATION COMPARISON

user_dict = user.model_dump()
user_json = user.model_dump_json()

print(user_dict)
print(user_json)


# Traditional OOP requires manual serialization
def traditional_to_dict(user):
    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "age": user.age
    }

#JSON'a çevirmek için önce dict'e çevirmeliyiz.
traditional_dict = traditional_to_dict(traditional_user)
traditional_json = json.dumps(traditional_dict)

print(traditional_dict)
print(traditional_json)



