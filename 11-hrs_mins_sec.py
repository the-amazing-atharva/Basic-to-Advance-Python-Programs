def getHoursMinutesSeconds(totalSeconds):
    # If totalSeconds is 0, just return '0s':
    if totalSeconds == 0:
        return '0s'
    # Set hours to 0, then add an hour for every 3600 seconds removed from
    # totalSeconds until totalSeconds is less than 3600:
    hours = 0
    while totalSeconds >= 3600:
        hours += 1
        totalSeconds -= 3600
    # Set minutes to 0, then add a minute for every 60 seconds removed from
    # totalSeconds until totalSeconds is less than 60:
    minutes = 0
    while totalSeconds >= 60:
        minutes += 1
        totalSeconds -= 60
    # Set seconds to the remaining totalSeconds value:
    seconds = totalSeconds
    # Create an hms list that contains the string hour/minute/second amounts:
    hms = []
    # If there are one or more hours, add the amount with an 'h' suffix:
    if hours > 0:
        hms.append(str(hours) + 'h')
    # If there are one or more minutes, add the amount with an 'm' suffix:
    if minutes > 0:
        hms.append(str(minutes) + 'm')
    # If there are one or more seconds, add the amount with an 's' suffix:
    if seconds > 0:
        hms.append(str(seconds) + 's')
    # Join the hour/minute/second strings with a space in between them:
    return ' '.join(hms)
