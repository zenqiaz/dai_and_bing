import copy
def combine(num,list_of_list):
    res=[]
    for i in list_of_list:
         res.append([num]+i)
    return res

def findpattern(nums,tiles):
    if tiles==0:
        return [[0]*nums]
    if tiles>(nums*4):
        return []
    if nums==1:
        return [[tiles]]
    res=[]
    for i in range(5):
        if (tiles-i)>=0:
            res+=combine(i,findpattern(nums-1,tiles-i))
    return res

def hu_nohead(hand):
    for i in range(9):
        if hand[i]>0:
            if hand[i]>2:
                handcopy=copy.deepcopy(hand)
                handcopy[i]-=3
                if hu_nohead(handcopy):
                    return True
            elif i<7 and hand[i+1]>0 and hand[i+2]>0:
                handcopy=copy.deepcopy(hand)
                handcopy[i]-=1
                handcopy[i+1]-=1
                handcopy[i+2]-=1
                if hu_nohead(handcopy):
                    return True
            return False
    return True

def hu_havehead(hand):
    for i in range(9):
        if hand[i]>0:
            if hand[i]>1:
                handcopy=copy.deepcopy(hand)
                handcopy[i]-=2
                if hu_nohead(handcopy):
                    return True
            if hand[i]>2:
                handcopy=copy.deepcopy(hand)
                handcopy[i]-=3
                if hu_havehead(handcopy):
                    return True
            if i<7 and hand[i+1]>0 and hand[i+2]>0:
                handcopy=copy.deepcopy(hand)
                handcopy[i]-=1
                handcopy[i+1]-=1
                handcopy[i+2]-=1
                if hu_havehead(handcopy):
                    return True
            return False
    return True


def findting(hand):
    res=[]
    for i in range(9):
        if hand[i]<4:
            handcopy=copy.deepcopy(hand)
            handcopy[i]+=1
            if hu_havehead(handcopy):
                res.append(i)
    return res
    

def findting_many(hands):
    res=[0]*512
    handps=[[]for i in range(512)]
    tings=[[]for i in range(512)]
    for hand in hands:
        if findting(hand)!=[]:
            it=0
            for i in findting(hand):
                it+=2**i
            res[it]+=1
            handps[it].append(hand)
            tings[it]=findting(hand)
    return res,handps,tings

def findunique(list_1,list_2):
    res=copy.deepcopy(list_2)
    for i in range(len(list_2)):
        if list_2[i] in list_1:
            res[i]=[]
    return res

def countavail(list):
    res=0
    for i in list:
        if i!=[]:
            res+=1
    return res

def confirmpat(result,ting):
    return result[1][result[2].index(ting)]

def findgood(list,a,b):
    res=[]
    for i in range(512):
        if list[2][i]!= []:
            flag=1
            for j in list[1][i]:
                if j[a]==0 or j[b]==0:
                    flag=0
                    break
            if flag==1:
                res.append(list[2][i])
    return res

def findgood_2(list,a):
    res=[]
    for i in range(512):
        if list[2][i]!= []:
            flag=1
            for j in list[1][i]:
                if j[a]<2:
                    flag=0
                    break
            if flag==1:
                res.append(list[2][i])
    return res

def findgood_3(list,a):
    res=[]
    for i in range(512):
        if list[2][i]!= []:
            flag=1
            for j in list[1][i]:
                if j[a]<3:
                    flag=0
                    break
            if flag==1:
                res.append(list[2][i])
    return res


def findgood_12(list,a,b):
    res=[]
    for i in range(512):
        if list[2][i]!= []:
            flag=1
            for j in list[1][i]:
                if j[a]==0 or j[b]<2:
                    flag=0
                    break
            if flag==1:
                res.append(list[2][i])
    return res

def findgood_123(list,a,b,c):
    res=[]
    for i in range(512):
        if list[2][i]!= []:
            flag=1
            for j in list[1][i]:
                if j[a]==0 or j[b]==0 or j[c]==0:
                    flag=0
                    break
            if flag==1:
                res.append(list[2][i])
    return res

def code_to_num(code):
    return (code[0]+9*code[1]+81*code[2])

def pat_to_num(pat):
    res=0
    if pat !=[]:
        for i in pat:
           res+=2**i
    return res    

def code_to_tile(code):
    base=[0]*9
    for i in code:
        base[i]+=1
    return base

def setcode(code_to_pat,pat_to_code,codes,pat):
    pat_to_code[pat_to_num(pat)]=codes
    for code in codes:
        code_to_pat[code_to_num(code)]=pat
    return code_to_pat,pat_to_code

def contain(pat,code):
    for i in range(9):
        if code[i]>pat[i]:
            return False
    return True        

def validate(codes,pat,list):
    s=confirmpat(list,pat)
    ref=[]
    for i in codes:
        ref.append(code_to_tile(i))
    for j in s:
        flag=0
        for k in ref:
            if contain(j,k):
                flag=1
        if flag==0:
            print (j,pat,codes)
            return False
    return True

a_7=findpattern(9,7)
c_7=findting_many(a_7)
a_10=findpattern(9,10)
c_10=findting_many(a_10)
a_13=findpattern(9,13)
c_13=findting_many(a_13)
#data=open("D:\data.txt",'w+') 
#print('miaomiaomiao',file=data)
#data.close()
ctp=[[]]*729
ptc=[[]]*512

