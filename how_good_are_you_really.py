# There was a test in your class and you passed it. Congratulations!

# But you're an ambitious person. You want to know if you're better than the average student in your class.

# You receive an array with your peers' test scores. Now calculate the average and compare your score!

# Return true if you're better, else false!

# Note:
# Your points are not included in the array of your class's points. Do not forget them when calculating the average score!

my_class_points = [100, 40, 34, 57, 29, 72, 57, 88]
my_points = 75

def better_than_average(class_points, your_points):
    len_class_points = len(class_points)
    class_average = (sum(class_points)) / len_class_points
    print(f"The length of the class_points array is: {len_class_points}")
    print(f"The class average is: {class_average}")
    
better_than_average(my_class_points, my_points)