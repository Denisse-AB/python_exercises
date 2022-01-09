'''
Military time conversion
'''

time = '3:15 AM'

def time_conv(time):

    length = len(time)

    if length == 7:
        midnight = time[-2:]

        if midnight == "PM":
            return str(int(time[0]) + 12) + time[1:4]
        else:
            return "0" + time[:4]
    else:
        hour = time[:2]
        minutes = time[2:5]
        midnight = time[-2:]

        if midnight == "AM" and hour == "12":
            return "00" + minutes
        elif midnight == "PM" and hour == "12":
            return time[:5]
        elif midnight == "PM":
            return str(int(time[0:2]) + 12) + minutes
        else:
            return time[:5]

print(time_conv(time.upper()))
