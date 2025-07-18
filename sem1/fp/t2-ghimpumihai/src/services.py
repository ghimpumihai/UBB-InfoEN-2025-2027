from domain import Address
from math import sqrt
class Services:
    def __init__(self,repository):
        self.repository=repository
    def add_address(self,address_id,street_name,street_number,x,y):
        address=Address(address_id,street_name,street_number,x,y)
        self.repository.add(address)
    def distance_from_d(self,d,x,y):
        """
        THe taxi stations that are the sorted by the distance from a given point and have a minimum distance of d
        :param d: The minimum distance
        :param x: The x coordinate
        :param y: The y coordinate
        :return: The list of taxi stations
        """
        addresses=self.repository.get_all()
        list_address= {}
        for i in addresses:
            if sqrt((i.x-x)**2+(i.y-y)**2)<d:
                list_address[sqrt((i.x-x)**2+(i.y-y)**2)]=i
        return list_address
    def minimize_average(self):
        addresses=self.repository.get_all()
        avx=0
        avy=0
        for i in addresses:
            avx+=i.x
            avy+=i.y
        avx=avx//len(addresses)
        avy=avy//len(addresses)
        return avx,avy



