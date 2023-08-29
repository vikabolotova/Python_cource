def compare_list(A,B):
    if len(A) > len (B):
        print(len(A))
    elif len(A)==len(B):
        print('Длина списков одинакова и равна', len(A))

    else:
        print(len(B))

compare_list([1,5,6,7,'a',4,7],[5,8,9,0,'b','bhfdc'])