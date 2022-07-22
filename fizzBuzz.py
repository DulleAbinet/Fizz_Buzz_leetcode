class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        list_str = [0]*n
        i = 1
        while  i <= n :
            if i % 3 == 0 and i % 5 == 0:
                list_str[i-1] = "FizzBuzz"
            elif i % 3 == 0:
                list_str[i-1] = "Fizz"
            elif i % 5 == 0 :
                list_str[i-1] = "Buzz"
            else:
                list_str[i-1] = str(i)
                
            i +=1
                
        return list_str
