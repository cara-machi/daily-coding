# Week3 Day1
1. usage of () and []
- calling function 
``` python 
input()      
split()     
append()     
print()      
len()     
```
- list operations 
``` python 
my_list[0]    
my_list[1:3]   
my_list[-1]    
[]            
[1, 2, 3]      
```
2. split usage
```python
#  ❌
str_numbers = user_input.split  
sum += list(n)                  

#  ✅  
str_numbers = user_input.split() 
sum += list[n]                    
```

# Week3 Day2
1. dictionary using instead of looping- alternative way
```python
a_count = e_count = i_count = o_count = u_count = 0

for char in sentence:
    lower_char = char.lower()
    if lower_char == 'a':
        a_count += 1
    elif lower_char == 'e':
        e_count += 1
```
2. different ways to count various space
- Whitespace characters: tab, newline 
- space characters only
```python
char_count = 0
for char in sentence:
    if not char.isspace(): 
        char_count += 1
char_count = len(sentence) - sentence.count(" ") # only space space 
```
