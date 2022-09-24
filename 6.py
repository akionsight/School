angle1 = int(input("Enter 1st angle: "))
angle2 = int(input("Enter 2nd angle: "))
angle3 = int(input("Enter 3rd angle: "))

if angle1 + angle2 + angle3 == 180:
    print("There is a high probability that these angles can form a triangle")
else: 
    print("There is a high probability that these angles cannot form a triangle")

"""
Enter 1st angle: 90
Enter 2nd angle: 45
enter 3nd angle: 45

There is a high probability that these angles can form a triangle

---------------------

Enter 1st angle: 38
Enter 2nd angle: 45
enter 3nd angle: 45

There is a high probability that these angles cannot form a triangle

"""