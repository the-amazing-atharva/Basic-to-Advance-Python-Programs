# Loop over am and pm:
for meridiem in ['am', 'pm']:
    # Loop over every hour:
    for hour in ['12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']:
        # Loop over every 15 minutes:
        for minutes in ['00', '15', '30', '45']:
            # Print the time:
            print(hour + ':' + minutes + ' ' + meridiem)
