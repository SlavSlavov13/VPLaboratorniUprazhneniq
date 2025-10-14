distance = int(input('Distance = '))
hours = int(input('Hours = '))
minutes = int(input('Minutes = '))
seconds = int(input('Seconds = '))

time_in_seconds = hours * 3600 + minutes * 60 + seconds
mps = distance / time_in_seconds
kph = mps / 1000 * 3600
mph = distance / 1000 / 1.609 / (time_in_seconds / 3600)

print(mps)
print(kph)
print(mph)