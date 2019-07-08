def percent(total_amt,discount_amt):
    p=0
    if not(type(total_amt) == int and type(discount_amt) == int):
        return("Invalid Arguments")
    
    if total_amt<=0:
        return("total amt cannot be zero")
    
    p=(discount_amt/total_amt)*100
    return p

#total_amt=int(input("Enter total amt : "))
#discount_amt=int(input("discount amt : "))
#p=percent(total_amt,discount_amt)
#print(p)