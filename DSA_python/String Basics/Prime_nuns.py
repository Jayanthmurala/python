class Primes:
    def is_Prime(self , num :int):
        if num <= 1:
            return False
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                return False
        return True
    def list_primes(self , start ,end): 
        for i in range(start,end+1):
            if(self.is_Prime(i)):
                print(i,end=" ")
        return "\nDONE"
        
print(Primes().list_primes(50,100))