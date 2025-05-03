from pydantic import BaseModel

class User(BaseModel):
    id:int
    name:str
    email:str
    age : int

user = User(id=1, name="John Doe", email="john.doe@example.com", age=20)

print(user)

invalid_user_2 = User(id=1, name="John Doe", email="john.doe@example.com")
invalid_user_3 = User(id=1, name="John Doe", age=20)
invalid_user_4 = User(id=1, name="John Doe", email="john.doe@example.com", age="twenty")
invalid_user_5 = User(id=1, name="John Doe", email=5, age=20)

#age is int but we are passing a string
user_2 = User(id=1, name="John Doe", email="john.doe@example.com", age="20")
print(type(user_2.age))
#id is int but we are passing a string
user_3 = User(id="1", name="John Doe", email="john.doe@example.com", age=20)
print(type(user_3.id))


class Price(BaseModel):
    amount: float
    currency: str


price = Price(amount=100, currency="USD")
print(type(price.amount))
price = Price(amount="100", currency="USD")
print(type(price.amount))

"""
Pydantic, Python'da veri doğrulama (validation) ve veri tip dönüşümü (type coercion) işlemlerini otomatik olarak yaparak geliştiricinin işini büyük ölçüde kolaylaştırır.
Yukarıdaki örneklerde görüldüğü gibi, `age="20"` gibi bir string değeri tanımda `int` olarak belirtilmişse, Pydantic bunu otomatik olarak tam sayıya çevirir.
Aynı şekilde `"100"` stringini `float` olarak yorumlayıp `100.0` yapar.
Eğer çevrilemeyen bir değer verilirse (örneğin `age="twenty"`), hata fırlatır ve problemi net bir şekilde açıklar. 
Bu özellikler sayesinde veri kaynakları (örneğin API istekleri, dosyalar, formlar) ne kadar karmaşık ya da hatalı olursa olsun, uygulamanın içinde güvenilir ve tip güvenliği olan verilerle çalışılmasını sağlar.
Özellikle veri girişlerinin dış kaynaklardan geldiği durumlarda hata ayıklamayı kolaylaştırır ve uygulamanın güvenilirliğini artırır.
"""