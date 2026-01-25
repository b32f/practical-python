# bounce.py
#
# Exercise 1.5
height = 100 # meters
bounce_back = 3/5
bounces = 10

bounced_back_height = height

for _ in range(bounces):
    bounced_back_height *= bounce_back
    print(round(bounced_back_height,2))
