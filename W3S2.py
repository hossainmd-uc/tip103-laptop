
# Output: Number of buildings that can be built

def build_skyscrapers(floors):
    
    # keep track of current largest
    # create var for total skyscrapers
    # keep track of current height
    
    last = floors[0]
    total = 0

    for current_height in floors:
        if current_height >= last:
            total += 1
        
        last = current_height
    
    return total
        
    

print(build_skyscrapers([10, 5, 8, 3, 7, 2, 9])) 
print(build_skyscrapers([7, 3, 7, 3, 5, 1, 6]))  
print(build_skyscrapers([8, 6, 4, 7, 5, 3, 2])) 