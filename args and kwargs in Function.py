# Example of using *args in a function to accept multiple arguments
# args passes a variable number of arguments to a function.
def order_cake(size ,*Flavour):
    print(f"I want to order two cakes of {size} with the following flavours:")
    for flavour in Flavour:
         print(f"- {flavour}")
order_cake( "big","chocolate","vanilla")

# Example of using **kwargs in a function to accept multiple keyword arguments
# kwargs passes key-value pairs to arguments in a function. 
# It allows you to pass a variable number of keyword arguments to a function.

def order_cake_with_details(size, **details):
    print(f"I want to order a {size} cake with the following details:")
    for key, value in details.items():
        print(f"{key}: {value}")
order_cake_with_details("big", frosting="chocolate", candles=5)
