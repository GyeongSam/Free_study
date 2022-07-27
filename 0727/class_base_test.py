class Nationality:
    def __init__(self, nation):
        self.nation = nation
    
    def introduce(self):
        return f'나의 국적은 {self.nation}'


korea_nationality = Nationality("대한민국")
print(korea_nationality.introduce()) # 나의 국적은 대한민국