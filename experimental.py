test1=[('(', ')', '(', '(', ')', ')'), (')', '(', '(', '(', ')', ')'), (')', ')', '(', '(', '(', ')'), (')', '(', 
'(', ')', ')', '('), ('(', ')', '(', ')', '(', ')'), ('(', '(', ')', ')', ')', '('), (')', ')', '(', ')', '(', '('), (')', '(', ')', '(', ')', '('), ('(', '(', ')', '(', ')', ')'), ('(', ')', ')', '(', ')', '('), (')', '(', '(', ')', '(', ')'), (')', ')', '(', '(', ')', '('), (')', ')', ')', '(', '(', '('), (')', '(', ')', ')', '(', '('), ('(', ')', ')', ')', '(', '('), ('(', ')', '(', ')', ')', '('), ('(', '(', ')', ')', '(', ')'), (')', '(', ')', '(', '(', ')'), ('(', ')', ')', '(', '(', ')'), ('(', '(', '(', ')', ')', ')')]  
test=list(set(test1))
result=[]
index=[]
for i in range(len(test)):
    stack=[]
    for j in test[i]:
        if j ==')':
            try:
                stack.pop()
            except:
                index.append(i)
                break
        else:
            stack.append(j)

    if i not in index:
        result.append(''.join(test[i]))
    
print(result)