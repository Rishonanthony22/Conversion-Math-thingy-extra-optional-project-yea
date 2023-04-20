# Function to convert height from feet and inches to centimeters
def height_to_cm(height_ft, height_in):
    height_total_inches = height_ft * 12 + height_in
    height_cm = height_total_inches * 2.54
    return height_cm

# Function to convert height from centimeters to feet and inches
def cm_to_height(height_cm):
    height_total_inches = height_cm / 2.54
    height_ft = int(height_total_inches // 12)
    height_in = int(height_total_inches % 12)
    return height_ft, height_in

# Take input from user for conversion type and height
conversion_type = input("Please enter 'ft' to convert from feet and inches to centimeters, or 'cm' to convert from centimeters to feet and inches: ").lower()
height = float(input("Please enter your height: "))

# Convert height based on input type
if conversion_type == 'ft':
    # Convert height from feet and inches to centimeters
    height_ft = int(height)
    height_in = int((height - height_ft) * 12)
    height_cm = height_to_cm(height_ft, height_in)
    print("Your height in centimeters is:", height_cm)
elif conversion_type == 'cm':
    # Convert height from centimeters to feet and inches
    height_ft, height_in = cm_to_height(height)
    print("Your height in feet and inches is:", height_ft, "ft", height_in, "in")
else:
    print("Invalid conversion type entered. Please try again.")

