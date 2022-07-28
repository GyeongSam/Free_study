class PublicTransport:
    total_passenger=0
    now_passenger=0

    def __init__(self, name, fare):
        self.name=name
        self.fare=fare
    
    def get_in(self,passenger):
        PublicTransport.total_passenger+=passenger
        PublicTransport.now_passenger+=passenger

    def get_off(self,passenger):
        PublicTransport.now_passenger-=passenger
    
    def profit(self):
        print(PublicTransport.total_passenger*self.fare)

class Bus(PublicTransport):
    def __init__(self, name, fare, max):
        super().__init__(name, fare)
        self.max=max

    def get_in(self,passenger):
        if PublicTransport.now_passenger+passenger>self.max:
            print('더이상 탑승할 수 없습니다.')
            quit()
        else:
            super().get_in(passenger)
    
bus1=Bus('타요빠스','5000',50)
bus1.get_in(30)
print(PublicTransport.now_passenger)
bus1.get_in(15)
print(PublicTransport.now_passenger)
bus1.get_off(10)
print(PublicTransport.now_passenger)
bus1.get_in(20)
print(PublicTransport.now_passenger)