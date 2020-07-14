# put your python code here
n_hours1 = int(input())
n_minutes1 = int(input())
n_seconds1 = int(input())
n_hours2 = int(input())
n_minutes2 = int(input())
n_seconds2 = int(input())
total_seconds1 = n_hours1 * 60 ** 2 + n_minutes1 * 60 + n_seconds1
total_seconds2 = n_hours2 * 60 ** 2 + n_minutes2 * 60 + n_seconds2
print(total_seconds2 - total_seconds1)
