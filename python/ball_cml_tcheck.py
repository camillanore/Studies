# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 21:57:25 2015

@author: Camilla Nore
"""
"""
Exercise 4.12: Test validity of input data
Test if the t value read in the program from Exercise 4.10 lies between 0
and 2v0/g. If not, print a message and abort the execution. Filename:
ball_cml_tcheck.py.
"""
import re
import sys

g = 9.81
def main():
        
    try:
        t = float(sys.argv[1])
        v_0 = float(sys.argv[2])
        print "You hav given", len(sys.argv), "arguments."
    except IndexError as e:
        print "Not enough argumenets given, please give manually:"
        t = raw_input("t = ")
        v_0 = raw_input("v_0 = ")
    
    # At this point we are sure that we have two values.
    # Want to convert them to floats.
                    
    try:
        t = float(t)
        v_0 = float(v_0)
    except ValueError as e:
        print "\nNot a number\n", e
        sys.exit(1)
    
    # Check range of input
    if t > (2*v_0)/g or t < 0:
        print 't out of range'
        print easteregg(s2)
        print 'Exceptions? This is an exception.'        
        sys.exit(1)
        
    print "The solution for y is ", y_t(g, t, v_0)

def y_t(g, t, v_0):
    y = v_0*t - 0.5*g*t**2
    return y

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

s2 = '31o32\n29o30$31$38o39o40\n17$18o28o29$31$37o38$39\n15$18$28$29"31$36o37$42o43o44o45\n15$16o18"19$27o28"31$36$37"41o42$43"44"45\n15$16"19"20o26o27$31$35o40o41"42\n15$20$26$27$31$35$39o40"41\n15$16$21$25$26$27"32$34$35"38$39"47o48o50"51\n07$11o15$16$22o23o24"25$32"34"38$39o41o42o43o44o45"46"47"51o52o53o54\n08$12"13o15$16$23"26o27o35o36o39"40"41"47o48o49"50"51"52\n09$13"14$15$16$24o25"28"34"37"44o46"47\n09$10$44"45o46o47o48o49o50\n01o10$36o37o38o47"48"49"50"51"52"53o54o55o56o57\n02"03o10$22o23o24o28o33o34"39"40"41\n00o04"05o06o10"20o21"29"30o32"41"42o48o49o50o51o52\n01"02o06"07"18o19"30$42"43\n03"04o05o17o18"30$31$43$49$50$51$52$53"54"55\n01o02o03o04o05"17$27o28o30$33o34o43$51"52"53"54"55\n01o02o03o04o05o09"17$26$27"28$30$32o33"34$35$43$47o48o49o50o51o52o53o54\n00"01"02"05"06$08"17$26"27$28"30$32$33$34"43"47$48$49"50"51"52"53\n03o04o06$17"18o29o30$32"33"42o47$48$49o50o51o52\n01o02$03"04"05"06"07"18"19o30"31o41o47"48"49"50"51"52$53\n01$02$21"22o23o24o25o26o27$33o39o52$53\n01"02$25$32$33o34"35"37"38"52$53\n03"04o09o27o31o32$33"51"52\n05"06"07o08o09$10o28"29"30"31"45$46o47o48o49"50\n10"11o12o44o45$46"47\n12"13o14o42o43o44"45\n14"15"16o17o26"27"28"39o40o41"42"43\n17"18"19"21o22o35o38"39"40\n22o23"24$25"27o28o29o30o32"33"34"35\n21o22"26$27"28"29"30"31"33o34\n21$22o26o27$33$34o35\n20o21$22o23o24o27$28o29o30o31o32o33$34"35\n20$21"27$35"36\n20$21"22"23"24"25"27$28"29"30"31"32"33"34$35\n20"21o22$23$24"25"26$27$28o29o30o31o32o33o34$35o36$37\n21o22"23$26$35$36\n21$22o23$26$27"28"29"30"32"35$36$37\n16o21"26$31"32"33"34"35"36$37\n16$17o18o26$27o28o29o30o31o32o33o36$37\n17$18"19"22o25o26"36"37$38\n17$18$19"20"21$22$23$24$25$26$27$28$29$30$31$32$33$34o35$36$37$38\n20o21$22$23$24$25$26$27$28$29$30$31$32$33$34$35$36$37$40o41\n16o17o18o19$20"21"22$23$24$25$26$27"28"29"30"31"32"33"34$35$36"37"38"39"40"41"42"43"44o45\n15$16"17"18$19o20o21o22o23$24$25$35$45$46o47\n10"11"12"13"14"15$16o34o35"44o45"46"47"48\n15"16"17$18$19o20o21o22o23o24o25o26o27o28o29o30o31o32o33"34"35"37o38o39o40$41$42"43"44"45\n22"23"24"25"26"27"28"29"30"'
    
if __name__ == '__main__':
    main()


"""
Output when t > (2*v_0)/g:
C:\Users\NBCNO1\Documents\Studies\python>python ball_cml_tcheck.py 40 50
You hav given 3 arguments.
t out of range

Output when t < 0:

C:\Users\NBCNO1\Documents\Studies\python>python ball_cml_tcheck.py -1 3
You hav given 3 arguments.
t out of range
"""