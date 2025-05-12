# def format_duration(seconds):
#     # case of 0 second
#     if seconds == 0:
#         return 'now'
#     # Calculate the numbers with divmod 
#     m,s = divmod(seconds,60)
#     h,m = divmod(m,60)
#     d,h = divmod(h,24)
#     y,d = divmod(d,365)

#     # prepare the final variable
#     result = ''
    
#     # initial data
#     ## This does not guarantee that you will have this order 
#     data = {'year':y, 'day':d,'hour':h,'minute':m,'second':s}
    
#     # filtered data
#     filtered_dict = {key:value for key, value in data.items() if value != 0}
    
#     # built the f string format
#     for key, value in filtered_dict.items():
#         word = key if value == 1 else f"{key}s"
        
#         # This is very risky and tricky
#         if len(filtered_dict) > 1 and key == list(filtered_dict.keys())[-2]:
#             result += f"{value} {word} and "
#         else:
#             result += f"{value} {word}, "
#     # strip the last , case
#     result = result.rstrip(", ")
#     return result

# ChatGPT version 
def format_duration(seconds):
    if seconds == 0:
        return 'now'

    # Breakdown into time components
    minutes, sec = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    years, days = divmod(days, 365)

    # Mapping of units to values
    units = [
        ('year', years),
        ('day', days),
        ('hour', hours),
        ('minute', minutes),
        ('second', sec)
    ]

    # Filter out zero values
    # parts list will be like ["1 hour", "1 minute", "2 seconds"]
    parts = [f"{value} {name}{'s' if value != 1 else ''}" 
             for name, value in units if value > 0]

    # Join with commas and "and"
    if len(parts) == 1:
        return parts[0]
    else:
        return ', '.join(parts[:-1]) + ' and ' + parts[-1]
