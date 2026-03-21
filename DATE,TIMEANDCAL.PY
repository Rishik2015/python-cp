# from datetime import date , time , datetime

# today = date.today()
# now = datetime.now()
# print("todays date is ",today)
# print("\n Current date and time is ",now)
# print("\n Date components  ", today.day,today.month,today.year)



def hotel_cost(nights):
    return 140000*nights

def plane_ride_cost(city):
    if "Las Vegas" == city:
        return 183
    elif "Berlin" == city:
        return 220
    elif "Sydney" == city:
        return 222
    elif "Paris" == city:
        return 475
    
def rental_car_cost(days):
    if days>=7  :
        return 40*days - 50
    elif days>=3 :
        return 40*days - 20
    else:
        return 40*days
    
def trip_cost(city,days,spending_money):    
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

print("Cost of car rental is ", rental_car_cost(5))
print("Cost of plane ride ",plane_ride_cost("Berlin"))
print("Cost of hotel room ",hotel_cost(7))
print("Total trip cost ",trip_cost("Berlin",7,500))
print(trip_cost("Sydney",6,500))
    