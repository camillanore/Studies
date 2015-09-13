# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 22:46:39 2015

@author: Camilla Nore
"""

#Exercise 3.23 Implement the Heaviside function

import numpy as np
import re

def main():
    test_heaviside()
    
def heaviside(x):
    if (x < 0):
        return 0
    else:
        return 1

def test_heaviside():
    test_data = [-10, -10**-15, 0, 10**-15, 10]
    expected_result = [0, 0, 1, 1, 1]    
    for i, x in enumerate(test_data):    
        print "x is:", x, "and H(x) is", heaviside(x)
        print "Expected result:", expected_result[i]
        assert expected_result[i] == heaviside(x), "Heaviside error"
    print "All tests completed without error"
    print easteregg(s1)

def easteregg(charcode):
    regexp = re.compile(r'(\d\d)(.)', re.DOTALL)
    last_pos = 0
    outstring = ''
    for m in regexp.finditer(charcode):
        index = int(m.groups()[0])
        char = m.groups()[1]
        outstring += (index-last_pos)*' ' + char
        last_pos = index+1
        if char == '\n': 
            last_pos = 0
    return outstring

s1 = "27,28-29-30-31.32\n26/31|32\n25/31|32\n24/31|32\n23/31|32\n18_19_20_21,22'31|32\n16<19-20'31:32\n17`18-19.20_21_22.23.24-25-26'27`28`29-30,31_32\\33_34\n20|21o22/24<25o26>27`29:30,31.32)33_34`35>36\n03T04h05o06u08s09h10a11l12l20:21/23`29|30|31/32)33\n04g05i06v07e09f10u11l12l20(21_22.23)24.25_26_27,28-29`31|32\\33\n05s06c07o08r09e10!20/21(23`24.25`26`30`31|33:34\n20\\21'22`23-24.25)28`31;33;34\n20|22`30/31-32<33\n20|26`29/33`34.35\n04,05-06_07-08.09.10_11_12_13_19/20|23`28:29_30_31.32.33-34'35\\36\n03/04,05'06-07.08_09_10\\11\\14`15`16-17.18/20:21`28;36\\37\n03`04\\06`07\\10`11\\12\\15\\17:20(24`27/30,34`35.37\\38\n05\\06`08\\12\\13\\17|20|22`26:29:35.36\\38\\39\n06\\08`09\\10_13)14)17:20;26|29|36)37:39:40\n05(06`07-08.09-10'11\\13|14|17|18\\20\\24`26;29;37|39|40\n06\\07-08_12`13;14;15.16_20(22`25/28/29_37|39|40\n07`08-09.10-11.12/13/15,16'17`18-19.20_21\\22_23_24/25_26,27'37;39|40\n10\\11:12:14:20/26`32,36/39|40\n11|12|14|19(28,29'31/35/39|40\n11|12|29,30'34/39|40\n"
            
if __name__ == "__main__":
    main()

"""Output:
x is: -10 and H(x) is 0
Expected result: 0
x is: -1e-15 and H(x) is 0
Expected result: 0
x is: 0 and H(x) is 1
Expected result: 1
x is: 1e-15 and H(x) is 1
Expected result: 1
x is: 10 and H(x) is 1
Expected result: 1
"""