#print star patter 
def star(n):
    for i in range(1,n+1):
        print('*'*i)
star(5)
'''
*
**
***
****
*****
output
'''
def inverted_right_angle_triangle(n):
    for i in range(n, 0, -1):
        print('*' * i)

# Example usage
inverted_right_angle_triangle(5)
