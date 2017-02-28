inp=raw_input("Dwse mou mia akolouthia parenthesewn: \t")
length=len(inp)
flag=False


if (length>=2) and ((length % 2) == 0):

    if inp[0]=="(" and inp[-1]==")":
        position=0
        count=0

        while (position<length) and (count>=0):
#if adding 1 when a "(" appears and subtract by 1 when a ")"
#apears, in a valid mathematical sequece, the counter in the end must be 0.
            if inp[position]=="(":
                count+=1
            else:
                count-=1
            position+=1

        if (count==0):
            flag=True

print flag
