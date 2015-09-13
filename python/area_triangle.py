# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 15:55:53 2015

@author: NBCNO1
"""
    
def main():
    triangle1 = area([[0,0], [1,0], [0,2]])
    v1 = (0,0); v2 = (1,0); v3 = (0,2)
    vertices = [v1, v2, v3]
    triangle1 = area(vertices)   
    print 'Area of triangle is %.2f' % triangle1
    test_area()
    
def area(vertices):
    v0 = vertices[0]
    v1 = vertices[1]
    v2 = vertices[2]
    result = 0.5 * abs(v1[0]*v2[1]-v2[1]*v1[1]
                       - v0[0]*v2[1] + v2[0]*v0[1]+v0[0]*v1[1]
                       - v1[0]*v0[1])
    return result
   
def test_area():
    v1 = (0,0); v2 = (3,0); v3 = (0,3)
    vertices = [v1, v2, v3]
    area_triangle1 = area(vertices)
    expected_area_triangle1 = 4.5
    assert expected_area_triangle1 == area_triangle1, 'error wrong area'
    print 'Test success the imput triangle points', vertices, 'result is', area_triangle1
if __name__ == "__main__":
    main()
    
"""
Output:
Area of triangle is 1.00
Test success the imput triangle points [(0, 0), (3, 0), (0, 3)] result is 4.5
"""