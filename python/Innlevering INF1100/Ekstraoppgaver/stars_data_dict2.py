# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 09:21:21 2015

@author: Camilla Nore

Exercise 6.6: Make a nested dictionary

Store the data about stars from Exercise 3.33 in a nested 
dictionary such that we can look up the distance, 
the apparent brightness, and the luminosity of a star with name N by:

stars[N]['distance']
stars[N]['apparent brightness']
stars[N]['luminosity']
"""
class StarInfo:
    def __init__(self, data_table):
        self.data = self._convert_table_to_dict(data_table)
    
    def _convert_table_to_dict(self, data_table):
        """From table format to nested dictionary"""
        column_names = ['star_name', 'distance', 'brightness', 'luminosity']
        stars = {}
        for line in data_table:
            stars[line[0]] = {column_names[i] : line[i] for i in range(1, len(column_names))}
        return stars       
        
def main():
    starinfo = StarInfo(data)
    print 'We can now look up the data, by dict indexing:'
    print 'Distance to Wolf 359:', starinfo.data['Wolf 359']['distance']


data = [
('Alpha Centauri A',    4.3, 0.26,      1.56),
('Alpha Centauri B',    4.3, 0.077,     0.45),
('Alpha Centauri C',    4.2, 0.00001,   0.00006),
("Barnard's Star",      6.0, 0.00004,   0.0005),
('Wolf 359',            7.7, 0.000001,  0.00002),
('BD +36 degrees 2147', 8.2, 0.0003,    0.006),
('Luyten 726-8 A',      8.4, 0.000003,  0.00006),
('Luyten 726-8 B',      8.4, 0.000002,  0.00004),
('Sirius A',            8.6, 1.00,      23.6),
('Sirius B',            8.6, 0.001,     0.003),
('Ross 154',            9.4, 0.00002,   0.0005),
]

main()

"""Note:
I did implement it as a class first, as I thought I had to do the sorting of
the data. Upon reading the task again, I see that it was not necessary.

Output:
We can now look up the data, by dict indexing:
Distance to Wolf 359: 7.7
"""