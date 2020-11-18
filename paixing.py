import copy
def combine(num, list_of_list):
    res=[]
    for i in list_of_list:
         res.append([num] + i)
    return res

def findpattern(nums, tiles):#遍历所有13牌牌型
    if tiles == 0:
        return [[0] * nums]
    if tiles > (nums * 4):
        return []
    if nums == 1:
        return [[tiles]]
    res=[]
    for i in range(5):
        if (tiles - i) >= 0:
            res += combine(i, findpattern(nums - 1 , tiles - i))
    return res

def hu_nohead(hand):
    for i in range(9):
        if hand[i] > 0:
            if hand[i] > 2:
                handcopy = copy.deepcopy(hand)
                handcopy[i] -= 3
                if hu_nohead(handcopy):
                    return True
            elif i < 7 and hand[i + 1]>0 and hand[i + 2] > 0:
                handcopy = copy.deepcopy(hand)
                handcopy[i] -= 1
                handcopy[i + 1] -= 1
                handcopy[i + 2] -= 1
                if hu_nohead(handcopy):
                    return True
            return False
    return True

def hu_havehead(hand):#验证和牌
    for i in range(9):
        if hand[i] > 0:
            if hand[i] > 1:
                handcopy = copy.deepcopy(hand)
                handcopy[i] -= 2
                if hu_nohead(handcopy):
                    return True
            if hand[i] > 2:
                handcopy = copy.deepcopy(hand)
                handcopy[i] -= 3
                if hu_havehead(handcopy):
                    return True
            if i < 7 and hand[i + 1]>0 and hand[i + 2]>0:
                handcopy=copy.deepcopy(hand)
                handcopy[i] -= 1
                handcopy[i + 1] -= 1
                handcopy[i + 2] -= 1
                if hu_havehead(handcopy):
                    return True
            return False
    return True

def findting(hand):#找到一副手牌的听牌种类
    res=[]
    for i in range(9):
        handcopy = copy.deepcopy(hand)
        handcopy[i] += 1
        if hu_havehead(handcopy):
            res.append(i)
    return res

def findting_many(hands):
    res=[0] * 512
    handps=[[]for i in range(512)]
    tings=[[]for i in range(512)]
    for hand in hands:
        if findting(hand) != []:
            it = 0
            for i in findting(hand):
                it += 2 ** i
            res[it] += 1
            handps[it].append(hand)
            tings[it] = findting(hand)
    return res,handps,tings
    

def fingtingqh(hand):#不计空听的情况
    res = []
    for i in range(9):
        if hand[i] < 4:
            handcopy = copy.deepcopy(hand)
            handcopy[i] += 1
            if hu_havehead(handcopy):
                res.append(i)
    return res
    

def findunique(list_1, list_2):
    res = copy.deepcopy(list_2)
    for i in range(len(list_2)):
        if list_2[i] in list_1:
            res[i] = []
    return res

def countavail(list):
    res = 0
    for i in list:
        if i != []:
            res += 1
    return res

def confirmpat(result, ting):#找到一种听牌类型对应的所有牌型
    return result[1][result[2].index(ting)]

def findgood(list,a,b):#这些都用不上
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

def findgood_123(list,a,b,c):#这些都用不上
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
    return (code[0] + 9 * code[1] + 81 * code[2])

def pat_to_num(pat):
    res = 0
    if pat != []:
        for i in pat:
           res += 2 ** i
    return res    

def code_to_tile(code):
    base=[0] *9
    for i in code:
        base[i] += 1
    return base

def setcode(code_to_pat, pat_to_code, codes,pat):#这个没用
    pat_to_code[pat_to_num(pat)] = codes
    for code in codes:
        code_to_pat[code_to_num(code)]=pat
    return code_to_pat,pat_to_code

def contain(pat, code):#判断手牌是否包含编码用到的三张牌
    for i in range(9):
        if code[i] > pat[i]:
            return False
    return True        

def validate(codes, pat, list):#判断一些编码能否覆盖某种听牌型包括的所有牌型
    s = confirmpat(list, pat)
    ref = []
    for i in codes:
        ref.append(code_to_tile(i))
    for j in s:
        flag = 0
        for k in ref:
            if contain(j, k):
                flag = 1
        if flag == 0:
            print (j, pat, codes)
            return False
    return True

def validate_s(codes, pat, list):#用不着了
    s = confirmpat(list, pat)
    ref = []
    for i in codes:
        ref.append(code_to_tile(i))
    for j in s:
        flag = 0
        for k in ref:
            if contain(j, k):
                flag = 1
        if flag == 0:
            #print (j, pat, codes)
            return False
    return True

def availcount(code, ref):
    return ref[1][ref[0].index(code)]

def choosecode(ref, pat, list):
    res = []
    lis = find_onecode(pat, list)
    for code in lis:
        res.append(availcount(code, ref))
    if max(res) == 0:
        return False
    pos = res.index(max(res))
    cod = lis[pos]
    ref[1][ref[0].index(cod)] -= 1
    ref[2][ref[0].index(cod)].append(pat)
    return ref

def choosecode_many(ref, manypats, list):#自动指定一部分牌型（即能用单个编码覆盖）的编码
    for i in manypats:
        if not choosecode(ref, i, list):
            return 'error!', i, find_onecode(i, list)
    return ref    

def choosecode_manual(ref, codes, pat):#手动把codes中包含的编码指定给某听牌型pat
    for cod in codes:
        if ref[1][ref[0].index(cod)] > 0:
            ref[1][ref[0].index(cod)] -= 1
        else:
            return 'too many!' 
        ref[2][ref[0].index(cod)].append(pat)
    return ref

def remove_code(ref, pat):#把某听牌型的信息移除
    for i in range(len(ref[2])):
        if pat in ref[2][i]:
            ref[2][i].remove(pat)
            ref[1][i] += 1
    return ref

def remove_codes(ref, pats):
    for pat in pats:
        ref = remove_code(ref,pat)
    return ref

def change_code(ref, codes, pat):#移除再换成新的
    ref = remove_code(ref, pat)
    ref = choosecode_manual(ref, codes, pat)
    return ref

def code_to_str(code):
    res = ''
    for i in code:
        res += str(i)
    return str

def is_onecode(pat, list):#判断一个听牌型包含的牌型能不能被（至少）一个编码覆盖
    s = confirmpat(list, pat)
    res = []
    for i in refpats[0]:
        flag = 0
        for j in s:
            if not contain(j, code_to_tile(i)):
                flag = 1
        if flag == 0:
            return True
    return False

def find_onecode(pat, list):#找到所有被一个编码覆盖的听牌型（以便进行自动指定
    s = confirmpat(list, pat)
    res = []
    for i in refpats[0]:
        flag = 0
        for j in s:
            if not contain(j, code_to_tile(i)):
                flag = 1
        if flag == 0:
            res.append(i)
    return res

def find_single(pats, list):#找到所有能且只能被一个编码覆盖的听牌型（本来是打算优先给这部分听牌型分配编码，结果后来发现没必要
    res = []
    for pat in pats:
        if len(find_onecode(pat,list)) == 1:
            res.append(pat)
    return res

def are_one_code(list):
    res = []
    for i in list[2]:
        if is_onecode(i, list):
            res.append(i)
    return res

def show_pats(code, ref):
    return ref[2][ref[0].index(code)]

def show_codes(pat, ref):
    res = []
    for i in range(len(ref[2])):
        if pat in ref[2][i]:
            res.append(ref[0][i])
    return res

def pickavail(list):
    res = []
    for i in list:
        if i != []:
            res.append(i)
    return res

def findbug():
    res = []
    for i in len(refpats[1]):
        if refpats[1][i] + refpatss[1][i]>6:
            res.append(refpats[0][i])
    return res

def code_of_pat(ref, list):
    res = [[], []]
    for pat in list[2]:
        if pat != []:
            res[0].append(pat)
            res[1].append(show_codes(pat, ref))
    return res

def check(ref, list):#验证一个解答是否满足题目条件
    for i in range(len(ref[1])):
        if not validate_s(ref[1][i], ref[0][i], list):
            return ref[1][i], ref[0][i]
    return True


def check_s(ref, list):
    res = []
    for i in range(len(ref[1])):
        if ref[0][i] in list[2]:
            if not validate_s(ref[1][i], ref[0][i],list):
                res.append(ref[0][i])
    return res

def code_to_digits(code):
    return code[0] * 100 + code[1] * 10 + code[2]

def pat_to_digits(pat):
    res = 0
    for i in range(len(pat)):
        res += (pat[i] * (10 ** i))
    return res

a_4=findpattern(9, 4)
c_4=findting_many(a_4)
a_7=findpattern(9, 7)
c_7=findting_many(a_7)
a_10=findpattern(9, 10)
c_10=findting_many(a_10)
a_13=findpattern(9, 13)
c_13=findting_many(a_13)
#data=open("D:\data.txt",'w+') 
#print('miaomiaomiao',file=data)
#data.close()
#ctp=[[]]*729
#ptc=[[]]*512
refpatss=[[],[],[]]#第一个list是编码，第二个是这个编码还能使用的次数，第三个是使用这个编码的听牌型
for i in range(9):#初始化编码空间
    for j in range(i, 9):
        for k in range(j, 9):
            refpatss[0].append([i, j, k])
            if i == k:
                refpatss[1].append(1)
            elif i == j or j == k:
                refpatss[1].append(3)
            else:
                refpatss[1].append(6)
            refpatss[2].append([])


import xlwt
workbook = xlwt.Workbook(encoding = 'utf-8')
ws = workbook.add_sheet('My Worksheet')
for i in range(len(cop[0])):
    ws.write(i,0,pat_to_digits(cop[0][i]),style0)
    for j in range(len(cop[1][i])):
        ws.write(i,j+1,code_to_digits(cop[1][i][j]),style0)

