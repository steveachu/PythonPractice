class Restaurant():
    """A simple class to represent a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant name is: " + self.restaurant_name.title() + ".")
        print("The cuisine type is: " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is now open!")

my_restaurant = Restaurant("Steve's place", "Korean")
print("Name is " + my_restaurant.restaurant_name)
print("Cuisine type is " + my_restaurant.cuisine_type)

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

