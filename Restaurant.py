class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        self.reviews = []
        Restaurant.all_restaurants.append(self)

    def get_name(self):
        return self.name

    def get_reviews(self):
        return self.reviews

    def get_customers(self):
        unique_customers = []
        for review in self.reviews:
            if review.get_customer() not in unique_customers:
                unique_customers.append(review.get_customer())
        return unique_customers

    def average_star_rating(self):
        total_ratings = sum(review.get_rating() for review in self.reviews)
        num_reviews = len(self.reviews)
        if num_reviews > 0:
            return total_ratings / num_reviews
        else:
            return 0.0
