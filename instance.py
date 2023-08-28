from Customer import Customer
from Review import Review
from Restaurant import Restaurant

# Create customer instances
customer1 = Customer("George", "Washington")
customer2 = Customer("John", "Doe")

# Create restaurant instances
restaurant1 = Restaurant("Delicious Bites")
restaurant2 = Restaurant("Café Supreme")

# Customers add reviews to restaurants
customer1.add_review(restaurant1, 4)
customer1.add_review(restaurant2, 5)
customer2.add_review(restaurant1, 3)

# Get all customers and reviews
all_customers = Customer.all()
all_reviews = Review.all()

# Display all customers
for customer in all_customers:
    print(customer.full_name())

# Display all reviews
for review in all_reviews:
    print(f"Customer: {review.get_customer().full_name()}, Restaurant: {review.get_restaurant().get_name()}, Rating: {review.get_rating()}")

