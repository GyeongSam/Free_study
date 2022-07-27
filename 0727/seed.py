from faker import Faker
fake1 = Faker('ko_KR')
Faker.seed(87654321)
print(fake1.name()) # 1
fake2 = Faker('ko_KR')
print(fake2.name()) # 