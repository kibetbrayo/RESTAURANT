from Restaurant import Restaurant
from Review import Review
from Customer import Customer
# Assume you have already defined the Customer, Review, and Restaurant classes

# Create some customer instances
customer1 = Customer("Alice", "Johnson")
customer2 = Customer("Bob", "Smith")

# Create restaurant instances
restaurant1 = Restaurant("Delicious Bites")
restaurant2 = Restaurant("Café Supreme")

# Customers add reviews to restaurants
customer1.add_review(restaurant1, 4)
customer1.add_review(restaurant2, 5)
customer2.add_review(restaurant1, 3)

# Get restaurant names
print(restaurant1.get_name())  # Output: Delicious Bites
print(restaurant2.get_name())  # Output: Café Supreme

# Get reviews for a restaurant
print(restaurant1.get_reviews())  # Output: [<Review object at ...>]
print(restaurant2.get_reviews())  # Output: [<Review object at ...>]

# Get unique customers who reviewed a restaurant
print(restaurant1.get_customers())  # Output: [<Customer object at ...>, <Customer object at ...>]
print(restaurant2.get_customers())  # Output: [<Customer object at ...>]

# Calculate average star rating for a restaurant
print(restaurant1.average_star_rating())  # Output: 3.5
print(restaurant2.average_star_rating())  # Output: 5.0
