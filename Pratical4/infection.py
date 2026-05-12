# Initialize
#   total students = 91
#   starting infected = 5
#   daily growth rate = 0.4
#   days passed = 0
#   current infected = starting infected

# Repeat while current infected < total students
    #   Add 1 to days
    #   Calculate new infections = current * growth rate
    #   Update current infected = current + new infections
    #   
    #   If current infected > total:
    #       Set current infected to total

    #   Print "infected students on [day] day: [current]"

# Print total days needed


total_number = 91
starting_number = 5
growth_rate = 0.4
days = 0
current_number = starting_number
while current_number < total_number:
    days += 1
    new_infected = current_number * growth_rate
    current_number += new_infected

    if current_number>total_number:
        current_number = total_number
    
    print("infected students on day", days, ":", current_number)
print("it takes", days, "days to infect all the students.")