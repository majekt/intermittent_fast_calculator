import datetime

# Input start time and length of your fast
fast_start_str = input("Enter the start time of your fast in 24-hour format: ")
fast_length_str = input("Enter the length of your fast in hours: ")

# Converting the start time and fast length to datetime objects
start_time = datetime.datetime.strptime(fast_start_str, '%H')
fast_length = datetime.timedelta(hours=int(fast_length_str))

end_time = start_time + fast_length

# Printing when it's okay to eat again
print("You can eat again at:", end_time.strftime('%H'))
