A = input().strip()
B = input().strip()
C = input().strip()

A_sec = int(A[:2]) * 3600 + int(A[3:5]) * 60 + int(A[6:])
B_sec = int(B[:2]) * 3600 + int(B[3:5]) * 60 + int(B[6:])
C_sec = int(C[:2]) * 3600 + int(C[3:5]) * 60 + int(C[6:])

if C_sec < A_sec:
    C_sec += 86400

message_travel_time = (C_sec - A_sec) / 2
if message_travel_time > int(message_travel_time):
    message_travel_time = int(message_travel_time) + 1
else:
    message_travel_time = int(message_travel_time)

exact_time = B_sec + message_travel_time

hours, seconds = divmod(exact_time, 3600)
minutes, seconds = divmod(seconds, 60)
if hours >= 24:
    hours %= 24
result = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)

print(result)
