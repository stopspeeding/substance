# Neutral pH
n = 7

# pH function 
def func(s):      
    
    for key in s:
        if s[key] > n:
          label = 'basic.'
        elif s[key] < n:
          label = 'acidic.' 
        elif s[key] == n:
          label = 'neutral.' 
        
        # Prints result
        print("Substance", key, "with pH", s[key], "is", label) 
          
# Data 
pH = {'Water':7, 'Soda':3, 'Beer':4, 'Coffee':5, 'Ammonia':11} 
func(pH) 
