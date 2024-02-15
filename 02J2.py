while True:
    inp = input()
    if inp == "quit!":
        break
    
    l = len(inp)
    if l > 4 and inp[-1] == 'r' and inp[-2] == 'o' and inp[-3] not in ['a', 'e', 'i', 'o', 'u', 'y']:
        print(inp[:-2] + "our")
    else:
        print(inp)
