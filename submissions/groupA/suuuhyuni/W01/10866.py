num = int(input())


deque = []
output = []

for _ in range(num):

    input_func = input().split()

    if input_func[0] == "push_front" :
        deque.insert(0, input_func[1])
    
    elif input_func[0] == "push_back" :
        deque.append(input_func[1])
    
    elif input_func[0] == "pop_front" :
        if len(deque) == 0 :
            output.append("-1")
        else : 
            output.append(deque.pop(0))
    
    elif input_func[0] == "pop_back" :
        if len(deque) == 0 :
            output.append("-1")
        else : 
            output.append(deque.pop())
    
    elif input_func[0] == "size" :
        output.append(str(len(deque)))
    
    elif input_func[0] == "empty" :
        output.append("1" if len(deque) == 0 else '0')
    
    elif input_func[0] == "front" :
        output.append("-1" if len(deque) == 0 else deque[0])
    
    elif input_func[0] == "back" :
        output.append("-1" if len(deque) == 0 else deque[-1])

print("\n".join(output))