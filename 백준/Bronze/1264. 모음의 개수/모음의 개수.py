vowel=['a','e','i','o','u']

while True:
    s=input()
    if s == '#':
        break
        
    cnt=0
    s=s.lower()
    
    for i in s:
        if i in vowel:
            cnt += 1
            
    print(cnt)