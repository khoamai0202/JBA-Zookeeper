# put your python code here
number_of_days = int(input())
number_of_nights = number_of_days - 1
food_cost_per_day = int(input())
one_way_flight_cost = int(input())
hotel_cost_per_night = int(input())
print(food_cost_per_day * number_of_days
      + hotel_cost_per_night * number_of_nights
      + one_way_flight_cost * 2)
