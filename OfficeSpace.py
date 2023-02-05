#  File: OfficeSpace.py

#  Description: Setting up a system for employees to input their preferred cubicle spaces on a coordinate grid

#  Student Name: Abdulateef Oyegbefun

#  Student UT EID: Afo296

#  Partner Name: Jesus Marcos

#  Partner UT EID: Jam27482

#  Course Name: CS 313E

#  Unique Number: 52038

#  Date Created: 02/04/2022

#  Date Last Modified:02/06/2022

import sys
import os
os.system('cls')

# Input: a rectangle which is a tuple of 4 integers (x1, y1, x2, y2)
# Output: an integer giving the area of the rectangle

def area (rect):
    x_distance = abs(rect[2]-rect[0])
    y_distance = abs(rect[3]-rect[1])

    rect_area = x_distance * y_distance
    return rect_area

def dotherectanglesoverlap(rect1,rect2):
    rect1_x1=rect1[0]
    rect1_y1=rect1[1]
    rect1_x2=rect1[2]
    rect1_y2=rect1[3]

    rect2_x1=rect2[0]
    rect2_y1=rect2[1]
    rect2_x2=rect2[2]
    rect2_y2=rect2[3]

    x2s = (rect1_x2,rect2_x2)
    min_of_max_x = min(x2s)

    x1s = (rect1_x1,rect2_x1)
    max_of_min_x = max(x1s)
    
    y2s = (rect1_y2,rect2_y2)
    min_of_max_y = min(y2s)

    y1s = (rect1_y1,rect2_y1)
    max_of_min_y = max(y1s)
    if (not (max_of_min_x < min_of_max_x)) or (not (max_of_min_y < min_of_max_y)):
        return False


    return True

# Input: two rectangles in the form of tuples of 4 integers
# Output: a tuple of 4 integers denoting the overlapping rectangle.
#         return (0, 0, 0, 0) if there is no overlap
def overlap (rect1, rect2):
    # assigning parts of the rectangle from the tuple to variables
    if not dotherectanglesoverlap(rect1,rect2):
        return (0,0,0,0)
    rect1_x1=rect1[0]
    rect1_y1=rect1[1]
    rect1_x2=rect1[2]
    rect1_y2=rect1[3]

    rect2_x1=rect2[0]
    rect2_y1=rect2[1]
    rect2_x2=rect2[2]
    rect2_y2=rect2[3]

    # Finding max and min of x-coordinate of both rectangles
    rect1_x_max = max(rect1_x1,rect1_x2)
    rect1_x_min = min(rect1_x1,rect1_x2)

    rect2_x_max = max(rect2_x1,rect2_x2)
    rect2_x_min = min(rect2_x1,rect2_x2)
    
    # Finding the min of the maximum x-coordinates and the 
    # the max of the minimum x-coordinates found above 
    max_x = min(rect1_x_max,rect2_x_max)
    min_x = max(rect1_x_min,rect2_x_min)


    # The above is repeated for the y-coordinates
    rect1_y_max = max(rect1_y1,rect1_y2)
    rect1_y_min = min(rect1_y1,rect1_y2)

    rect2_y_max = max(rect2_y1,rect2_y2)
    rect2_y_min = min(rect2_y1,rect2_y2)
    
    max_y = min(rect1_y_max,rect2_y_max)
    min_y = max(rect1_y_min,rect2_y_min)

    # x0, x1, x2, x3 = min_x,min_y,max_x,max_y
    return (min_x,min_y,max_x,max_y)
# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the unallocated 
#         space in the office
def unallocated_space (bldg):
  return None
# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the contested 
#         space in the office
def contested_space (bldg):
  return None
# Input: bldg is a 2-D array representing the whole office space
#        rect is a rectangle in the form of a tuple of 4 integers
#        representing the cubicle requested by an employee
# Output: a single integer denoting the area of the uncontested 
#         space in the office that the employee gets
def uncontested_space (bldg, rect):
  return None
# Input: office is a rectangle in the form of a tuple of 4 integers
#        representing the whole office space
#        cubicles is a list of tuples of 4 integers representing all
#        the requested cubicles
# Output: a 2-D list of integers representing the office building and
#         showing how many employees want each cell in the 2-D list
def request_space (office, cubicles):
  return None
# Input: no input
# Output: a string denoting all test cases have passed
def test_cases ():
  assert area ((0, 0, 1, 1)) == 1
  assert area ((2, 3, 10, 11)) == 64
  assert area ((7, 2, 18, 8)) == 66
  assert area ((17, 11, 30, 24)) == 169
  rect1=(2,3,10,11)
  rect2=(7,2,18,8)
  assert overlap(rect1,rect2) == (7,3,10,8)
  rect1=(2,3,10,11)
  rect2=(17,11,30,24)
  assert overlap(rect1,rect2) == (0,0,0,0)


  # write your own test cases

  return "all test cases passed"

def main():
  # read the data
    grid_size = sys.stdin.readline().split()
    total_area = int(grid_size[0])*int(grid_size[1])

    number_of_people = sys.stdin.readline().strip()
    number_of_people = int(number_of_people)
    for i in range(number_of_people):
        employee = sys.stdin.readline().strip()
        employee = employee.split()
        name = employee[0]
        rectangle_coords = [int(i) for i in employee[1:]]
        rectangle_coords=tuple(rectangle_coords)
        #print(name)
        #print(rectangle_coords)
  # run your test cases
    #rect1=(2,3,10,11)
    #rect2=(7,2,18,8)
    #print(overlap(rect1,rect2))

    print (test_cases())


  # print the following results after computation

  # compute the total office space
    print(f'Total {total_area}')
  # compute the total unallocated space

  # compute the total contested space

  # compute the uncontested space that each employee gets

if __name__ == "__main__":
  main()