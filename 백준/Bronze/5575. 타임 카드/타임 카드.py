for i in range(3):
    h1, m1, s1, h2, m2, s2 = map(int,input().split())
    start = (h1*3600) + (m1*60) +s1
    done = (h2*3600) + (m2*60) +s2
    t = done - start
    h = t//3600
    m = (t%3600)//60
    s = (t%3600)%60
    
    print(h, m, s)