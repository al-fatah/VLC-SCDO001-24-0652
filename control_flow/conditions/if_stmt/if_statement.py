# conditionally executing statements
# using the if statement
# indententation levels are important
#  when standalone if statements are written all the statements are executed

# season = "winter"
season = input("Enter the season: ")

if season == "winter":
    print("wear woolen clothes")
    print("stay indoors")

if season == "summer":
    print("wear cotton clothes")
    print("use air conditioner")

if season == "rainy":
    print("carry an umbrella")