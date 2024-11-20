
"""

283. Move Zeroes

Attempted

Easy

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

"""


#%%

array = [0,1,0,-3,12]


#%% this solution passed 67/74 test cases --- it failed due to time-complexity (it was too slow)

for e in range(len(array)-1):
    
    p0 = 0

    p1 = 1
    
    for e in range(len(array)-1):
        
        if array[p0] == 0 and array[p1] != 0 :
            
            #swap position
            
            array[p0] = array[p1]
            
            array[p1] = 0
            
        p0 += 1
        
        p1 += 1
        
        

#%% considerations for next attempt

# keep track of where the last zero was first found and start from there

# Try to do the full task in one pass

# study the two pointer technique more

# time complexity O(n**2)-->O(n)

# currently it will traverse the list a set amount of times.

# Find a way to stop once all the zeros have been moved.


