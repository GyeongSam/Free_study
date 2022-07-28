

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

bus=PublicTransport('BUS',1200)
bus.get_in(30)
bus.profit()