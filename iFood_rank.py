from operator import attrgetter

# class to define Restaurant structure
class Restaurant:
    def __init__(self, name, rank, distance):
        self.name = name
        self.rank = rank
        self.distance = distance

restaurantsList = []

# appending Restaurants 'object' inside the list
restaurantsList.append(Restaurant("O Mineiro", 4.2, 1.7))
restaurantsList.append(Restaurant("Lamen Kazu", 4.6, 0.7))
restaurantsList.append(Restaurant("Amor Aos Pedaços", 4.3, 1.2))
restaurantsList.append(Restaurant("Mr. Pretzels", 4.7, 1.1))
restaurantsList.append(Restaurant("We Coffee", 4.5, 0.8))
restaurantsList.append(Restaurant("Brigaderia Shopping Paulista", 4.7, 1.2))



# sorting list by rank
print('----- BY RANK -----')
restaurantsList.sort(key=lambda x: x.rank, reverse=True)
for restaurant in restaurantsList:
    print('Name: {}, Rank: {}, Distance: {}km'.format(restaurant.name, restaurant.rank, restaurant.distance))

# sorting list by distance
# print('----- BY DISTANCE -----')
# restaurantsList.sort(key=lambda x: x.distance)
# for restaurant in restaurantsList:
#     print('Name: {}, Rank: {}, Distance: {}km'.format(restaurant.name, restaurant.rank, restaurant.distance))