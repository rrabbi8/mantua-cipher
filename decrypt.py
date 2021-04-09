""" 
/*
 * THE FUNCTION DECRYPTS A CIPHERTEXT FOR A GIVEN CODE TABLE AND RETURNS A STRING OF THE PLAINTEXT
 *
 * © Md Reaj Uddin Rabbi, September 2018
*/
    
"""

def decrypt(ciphertext, code_table):
   
    
    # A dictionary of alphabets with their index values from the code_table
    my_dict = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8,
               'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 
               'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 
               'z':25}
    
    # Iterate over ciphertext and code table
    # Check in which list from code_table each element 
    #     from the ciphertext is present
    # Add the index of the corresponding code_table list to my_list
   
    my_list = []
    for text in ciphertext:
        for item in code_table:
            if text in item:
                my_list.append(code_table.index(item))
    
    # Iterate over my_list and the items in the dictionary 
    # Checks if elements from my_list is equal to the value of a key
    #     in the dictionary 
    # Finally add the keys of the corresponding values to an empty string and 
    #     concatenate them
    
    plain_txt = ''
    for num in my_list:
        for key,value in my_dict.items():
            if num == value:
                plain_txt += key
    
    return plain_txt