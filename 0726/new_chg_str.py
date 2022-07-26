s='@#~!I NeVEr DrEamEd AbouT SuCCeSs, i woRkEd foR iT.!>!'

def chg_str(x):
    X=''
    for i in x:
        if i.isalpha() or i==' ' or i=='.':
            X+=i
    return "'"+X.lower().capitalize()+"'"

print(chg_str(s))