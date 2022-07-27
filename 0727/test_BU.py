from faker import Faker # 1 faker 모듈의 Faker를 사용 하기 위한 코드이다.
fake = Faker() # 2 Faker는 클래스, fake는 인스턴스이다.
print(fake.name()) # 3 name()은 fake의 인스턴스 변수이다.