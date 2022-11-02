operands = '+*-/'
def postfix_eval(chaine):
    L = chaine.strip().split(" ")
    res = 0
    stack = []
    
    while len(L) != 0 :
        
        if L[0] not in operands:
            
            try : 
                stack += [int(L.pop(0))] 
            except :
                return("error-syntax")              
        
        else :
            
            op = L.pop(0)
            
            if len(stack) == 1 or len(stack) == 0 :
                return('error-empty-stack')
            else :
                rnum = stack.pop()
                lnum = stack.pop()
            
            if op == '+': stack.append(lnum + rnum)
            elif op == '-' : stack.append(lnum - rnum)
            elif op == '/' : stack.append(lnum // rnum)
            else : stack.append(lnum * rnum)
            
    if len(stack) != 1 :
        return('error-unfinished')
     
    return(stack[0])