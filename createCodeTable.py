"""
/*
 * THE FUNCTION RETURNS A CODE TABLE FOR A GIVEN SYMBOL COUNT TABLE AND AN OFFSET/KEY
 *
 * © Md Reaj Uddin Rabbi, September 2018
*/
"""

def gen_code_table(symb_cnt_table,offset):
    """ 
    
    """
    # To make the code easier 'symb_cnt_table' is replaced 'S_C_T'
    S_C_T = symb_cnt_table
    
    # A list of numbers 0-99 is made using this function 
    lst_N = []
    for num in range(100):
        lst_N.append(num)
    
    # Generates code table in a list when offset is 0
    # Iterate over S_C_T and add the numbers- 
    #     from lst_N with index 0 - j as asublist
    # Finally deletes the added list from the original
    
    lst_C_T = []
    if offset == 0:
        for item in S_C_T:
            lst_C_T.append(lst_N[:item])
            del lst_N[:item]
   
    # Generates code table in a list when offset in not 0
    # Firstly, iterating over S_C_T from the index 'offset'
    # Secondly, iterating over S_C_T till the index 'offset'
    # Finally replaces the of  postion sublists from 
    #     index '-offset' to the last to index 0 to 'offset
    # The 'zip' function was taken from the website 'stackoverflow.com':
    # https://stackoverflow.com/questions/31683959/the-zip-function-in-python-3
  
    
    else:
        
        for item in S_C_T[offset:]:
            lst_C_T.append(lst_N[:item])
            del lst_N[:item]
        for k in S_C_T[:offset]:
            lst_C_T.append(lst_N[:k])
            del lst_N[:k]
        for m,n in zip(range(-offset,0), range(offset)):
            lst_C_T.insert(n, lst_C_T[m])
        del lst_C_T[-offset:]
 
    return lst_C_T

   
    
    
