#測試程式
import sys 

def test(fun):
    if(fun=="inp"):#def inp()開關
        return 0
    elif(fun=="swee"):#def swee()開關
        return 0
def inp():
    sinp=sys.stdin.readline()
    sinp=sinp.replace("\n","")
    fiect=1
    #測資讀入
    while(sinp!="0 0"):
        hei,wei=map(int,sinp.split())#地圖高跟寬
        if(test("inp")):print(hei,wei)
        #地圖讀入
        swmap=[]
        for i in range(hei):
            sinp=sys.stdin.readline()
            sinp=sinp.replace("\n","").replace(".","0") 
            swmap.append(list(sinp))
            if(test("inp")):print(sinp)
        if(test("inp")):print(swmap)
        print("Field #%d:"%fiect)
        fiect+=1
        swee(swmap,hei,wei)
        sinp=sys.stdin.readline()
        sinp=sinp.replace("\n","")
	#主程式
def swee(st,h,w):
#這邊做預處理，如果地雷的鄰居也是地雷，鄰居不變。("*":"*")
#如果鄰居是數字，那麼加一處理
    swst={"*":"*","0":"1","1":"2","2":"3","3":"4","4":"5","5":"6","6":"7","7":"8","8":"8"}
    for j in range(h):
        for i in range(w):
            if(st[j][i]=="*"):
                for sti in range(-1,2,1):
                    for stj in range(-1,2,1):
                        if(((sti+j)in range(h))&((stj+i)in range(w))):
                            st[sti+j][stj+i]=swst.get(st[sti+j][stj+i])
#答案輸出                            
    for sth in range(h):
        for stw in range(w):
            print("%s"%st[sth][stw],end="")
        print("")
    print("")
        
inp()    
