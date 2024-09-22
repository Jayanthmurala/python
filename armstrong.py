def  arms(start,end):
    lestOfNum=[]
    for i in range(start,end+1):
        length=len(str(i))
        sum=0
        
        temp=i
        while(temp>0):
            sum+=(temp%10)**length
            temp//=10
        if(sum==i):
            lestOfNum.append(sum)
    return lestOfNum

def main():
    Start=int(input("Enter start: "))
    end=int(input("Enter end: "))
    print(arms(Start,end))
if __name__=="__main__":
    main()
