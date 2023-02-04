# OfficeSpace
A company that I work for is moving to a larger building. The new office is rectangular and will be subdivided into cubicles. My employees want to request particular positions for their cubicles and I want to set up a system that lets them make their requests.
The new office space has been expressed as a coordinate system where each unit is one foot. The south-west corner of this space is assigned the coordinate (0, 0). The positive X axis is aligned with the inner edge of the building's south wall. The positive Y axis is aligned with the west wall. Employees request a position for their cubicle by giving the coordinates of the cubicle's south-west corner and the cubicle's north-east corner.

#Description of Input:

The program will read input from standard input (stdin) in the following format:

33 26
3
Alice 2 3 10 11
Ted 7 2 18 8
GreedyBob 17 11 30 24

Each input should start with a line containing a pair of integers w and h giving the size of the new office space (w is the number of feet west-to-east, h is the number of feet south-to-north). Both of these numbers should be in the range 1 to 100.

After this is a line containing an integer n between 1 and 20 inclusive, giving the number of employees user of this program has. Following this are n cubicle placement requests, one per line.

Each request should start with the name of the employee. The name is a string of 1 to 20 characters (mix of upper and lower case letters a-z, no spaces). The name is followed by four integers x1, y1, x2, y2 where (x1, y1) indicate the coordinates of the south-west corner of the desired cubicle and (x2, y2) indicate the coordinates of the north-east corner. Each set of request coordinates satisfies 0 ≤ x1 ≤ x2 ≤ w and 0 ≤ y1 ≤ y2 ≤ h.

#Description of Output:

The program will print output to standard output (stdout) in the following format:

Total 858
Unallocated 574
Contested 15
Alice 49
Ted 51
GreedyBob 169
For the given input, a report that starts with the total number of square feet in the building and the number of square feet that no employee has requested (the unallocated space) will be generated.

Next, the total number of square feet that are contested because more than one empoyee has requested the same region of the floor will be given

Finally, for each employee the number of square feet that that employee can be guaranteed to have will be given. This is the total area that they requested minus any regions that were requested by another employee.

The employees will be listed in the same order they were given in the input.
