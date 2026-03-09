# FUNCTION ARGUMENTS

# TYPES OF FUNCTION ARGUMENTS:
# 1. **Positional Arguments** - Arguments that must be passed in the correct order.
# 2. **Keyword (Named) Arguments** - Arguments that are explicitly named when passed.
# 3. **Default Arguments** - Arguments that take a default value if not provided.
# 4. *args (Arbitrary Positional Arguments) - Allows passing multiple positional arguments.
# 5. **kwargs (Arbitrary Keyword Arguments) - Allows passing multiple keyword arguments.

# POSITIONAL AND KEYWORD ARGUMENTS

def display_weather(temp, humidity, wind_speed):
    """Displays the weather conditions."""
    print(f'Temperature: {temp}°C, Humidity: {humidity}%, Wind Speed: {wind_speed} km/h')

# Using keyword arguments (order does not matter)
display_weather(humidity=70, temp=22, wind_speed=15)

# Mixing positional and keyword arguments (order still matters for positional)
display_weather(30, wind_speed=15, humidity=22)

# ❌ This will cause a **SyntaxError**
# display_weather(humidity=70, 15, temp=22)  # Positional argument after keyword argument is not allowed

# ❌ This will cause a **SyntaxError**
# display_weather(70, temp=30, humidity=22)
# TypeError: display_weather() got multiple values for argument 'temp'

# DEFAULT ARGUMENTS

def adjust_lighting(room, brightness=75, color_temp=4000): # parameter with default value must be after parameters without default values
    """Adjusts lighting settings for a given room."""
    print(f'Adjusting lighting in {room} to {brightness}% brightness and {color_temp}K color temp.')

# Function calls with default values
adjust_lighting('Living Room')  # Uses default brightness (75) and color_temp (4000)
adjust_lighting('Bedroom', 50)  # Overrides brightness, keeps default color_temp
adjust_lighting('Kitchen', 50, 3500)  # Overrides both brightness and color_temp
adjust_lighting('Study', 50, color_temp=3750)  # Overrides both brightness and color_temp

def adjust_my_lighting(room, brightness, color_temp=4000):
    """Adjusts lighting settings for a given room."""
    print(f'Adjusting lighting in {room} to {brightness}% brightness and {color_temp}K color temp.')

# ❌ This will cause a **SyntaxError**
# adjust_my_lighting('Living Room')
# TypeError: adjust_my_lighting() missing 1 required positional argument: 'brightness'

# Incorrect because a non-default parameter is after a default parameter
# def change_my_lighting(room, brightness=50, color_temp):
#     pass

# POSITIONAL-ONLY ARGUMENTS
def one_function(a, b, /, c, d):
    print(a, b, c, d)

one_function(1, 2, 3, 4)  # Output: 1 2 3 4
# one_function(1, 2, 3)  # TypeError: my_function() missing 1 required positional argument: 'd'
one_function(1, 2, d=4, c=3)  # Output: 1 2 3 4
# one_function(a=1, b=2, c=3, d=4)  # TypeError: my_function() got some positional-only arguments passed as keyword arguments: 'a, b'

def two_function(a, b, /):
    print(a, b)

# two_function(a=1, b=2)  # TypeError: my_function() got some positional-only arguments passed as keyword arguments: 'a, b'

# KEYWORD-ONLY ARGUMENTS

def three_function(*, d, e):
    print(d, e)

# three_function(1, e=2)
# TypeError: three_function() takes 0 positional arguments but 1 positional argument (and 1 keyword-only argument) were given

# named parameters must follow bare *
# def four_function(d, e, *):
#     print(d, e)

# COMBINING POSITIONAL-ONLY AND KEYWORD-ONLY ARGUMENTS

def five_function(a, b, /, c, *, d, e=10):
    print(a, b, c, d, e)

five_function(1, 2, 3, d=4)  # Output: 1 2 3 4 10
five_function(1, 2, 3, d=4, e=5)  # Output: 1 2 3 4 5
five_function(1, 2, c=3, d=4, e=5)  # Output: 1 2 3 4 5