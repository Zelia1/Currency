from faker import Faker
fake = Faker()
x = fake.phone_number()
print(dir(fake))
print(x)
