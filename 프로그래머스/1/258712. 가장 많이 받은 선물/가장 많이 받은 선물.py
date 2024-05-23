def solution(friends, gifts):
    answer = 0
    
    gift_list = {} # 1번 조건 
    gift_num = {}  # 2번 조건
    will_gift = [0 for _ in friends]
    
    for i in friends:
        gift_list[i] = {}
        gift_num[i] = 0
        
    for i in gifts:
        a,b = i.split(' ')
        if b in gift_list[a]:
            gift_list[a][b]+=1
        else:
            gift_list[a][b]=1
        gift_num[a]+=1
        gift_num[b]-=1
        
    for i in range(len(friends)):
        now = friends[i]
        for j in range(i+1,len(friends)):
            another = friends[j]
            if another in gift_list[now]:
                give = gift_list[now][another]
            else:
                give = 0
            if now in gift_list[another]:
                get = gift_list[another][now]
            else:
                get = 0
            
            
            if give > get:
                will_gift[i]+=1
            elif give < get:
                will_gift[j]+=1
            elif give == get:
                give_num = gift_num[now]
                get_num = gift_num[another]
                if give_num > get_num:
                    will_gift[i] +=1
                elif give_num < get_num:
                    will_gift[j] +=1
    
    answer = max(will_gift)
    return answer
