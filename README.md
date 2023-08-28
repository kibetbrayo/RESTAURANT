## Challenge1 :Customer.py

Class Definition:
- Create a class called `Customer`.
- Initialize the class attributes: `given_name`, `family_name`, and an empty list `reviews`.
- Initialize a class-level list `all_customers` to store all created customer instances.

Initialization (Constructor):
- Initialize the instance variables `given_name` and `family_name`.
- Initialize the `reviews` list as an empty list.
- Add the instance to the class-level `all_customers` list.

Full Name Method:
- Define a method named `full_name()` that returns the full name of the customer.
  - Concatenate `given_name` and `family_name` with a space in between.
  - Return the full name.

All Customers Class Method:
- Define a class method named `all()` that returns the list of all customer instances.
  - Return the `all_customers` list.

Reviewed Restaurants Method:
- Define a method named `restaurants()` that returns a list of unique reviewed restaurants.
  - Initialize an empty list called `reviewed_restaurants`.
  - Loop through each `review` in the `reviews` list.
    - If the `restaurant` of the review is not in `reviewed_restaurants`, add it to the list.
  - Return the `reviewed_restaurants` list.

Add Review Method:
- Define a method named `add_review(restaurant, rating)` that adds a review for a restaurant.
  - Create a new `Review` instance with the current customer, the given `restaurant`, and `rating`.
  - Append the new review to the `reviews` list.

Number of Reviews Method:
- Define a method named `num_reviews()` that returns the count of reviews given by the customer.
  - Return the length of the `reviews` list.

Find Customer by Name Class Method:
- Define a class method named `find_by_name(name)` that finds and returns a customer instance based on the full name.
  - Loop through each customer in `all_customers`.
    - If the customer's full name matches the given `name`, return the customer.
  - If no match is found, return `None`.

Find All Customers by Given Name Class Method:
- Define a class method named `find_all_by_given_name(name)` that returns a list of customer instances with a given `given_name`.
  - Loop through each customer in `all_customers`.
    - If the customer's `given_name` matches the given `name`, add the customer to the list.
  - Return the list of customers.

## CHALLENGE 2 Review.py
Class Definition:
- Create a class called `Review`.
- Initialize the class attributes: `customer`, `restaurant`, `rating`.
- Initialize a class-level list `all_reviews` to store all created review instances.

Initialization (Constructor):
- Initialize the instance variables `customer`, `restaurant`, and `rating`.
- Add the instance to the class-level `all_reviews` list.

Get Rating Method:
- Define a method named `get_rating()` that returns the rating of the review.
  - Return the `rating` attribute.

All Reviews Class Method:
- Define a class method named `all()` that returns the list of all review instances.
  - Return the `all_reviews` list.

Get Customer Method:
- Define a method named `get_customer()` that returns the associated customer of the review.
  - Return the `customer` attribute.

Get Restaurant Method:
- Define a method named `get_restaurant()` that returns the associated restaurant of the review.
  - Return the `restaurant` attribute.

## CHALLENGE3 Restaurant
Class Definition:
- Create a class called `Restaurant`.
- Initialize the class attribute: `name`.
- Initialize a class-level list `all_restaurants` to store all created restaurant instances.

Initialization (Constructor):
- Initialize the instance variable `name`.
- Initialize an empty list `reviews`.
- Add the instance to the class-level `all_restaurants` list.

Get Name Method:
- Define a method named `get_name()` that returns the name of the restaurant.
  - Return the `name` attribute.

Get Reviews Method:
- Define a method named `get_reviews()` that returns the list of reviews for the restaurant.
  - Return the `reviews` list.

Get Customers Method:
- Define a method named `get_customers()` that returns a list of unique customers who reviewed the restaurant.
  - Initialize an empty list called `unique_customers`.
  - Loop through each `review` in the `reviews` list.
    - If the customer of the review is not in `unique_customers`, add it to the list.
  - Return the `unique_customers` list.

Average Star Rating Method:
- Define a method named `average_star_rating()` that calculates and returns the average star rating of the restaurant.
  - Initialize `total_ratings` to 0.
  - Loop through each `review` in the `reviews` list.
    - Add the rating of the review to `total_ratings`.
  - Calculate the `num_reviews` as the length of the `reviews` list.
  - If `num_reviews` is greater than 0:
    - Return `total_ratings / num_reviews`.
  - Otherwise, return 0.0.

All Restaurants Class Method:
- Define a class method named `all()` that returns the list of all restaurant instances.
  - Return the `all_restaurants` list.

