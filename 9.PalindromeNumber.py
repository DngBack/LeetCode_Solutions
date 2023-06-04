class Soluion: 
    def first_solution(self, x: int) -> bool : 
        if x < 0: 
            return False
        else: 
            return str(x) == str(x)[::-1]
        
    def second_solution(self, x: int) -> bool :
        if x<0 or (x > 0 and x % 10 == 0):
            return False 
        
        revX = 0 
        while x > revX:
            revX = revX * 10 + x % 10 
            x = x // 10 
        
        return True if (x == revX or x == revX // 10 ) else False 

