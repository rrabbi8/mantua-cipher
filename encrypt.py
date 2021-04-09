""" 
/*
 * THE FUNCTION ENCRYPTS A STRING OF PLAINTEXT FOR A GIVEN CODE TABLE AND RETURNS A LIST OF SYMBOLS/CIPHERTEXT
 *
 * © Md Reaj Uddin Rabbi, September 2018
*/
    
"""
def encrypt(plaintext, code_table):
    
    # A dictionary of alphabets with their index values from the code_table
    my_dict = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8,
               'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 
               'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 
               'z':25}
    
    # Iterate over the plaintext and items in my_dict
    # If letter from plaintext = key in my_dict, add the corresponding value 
    #     to my_list
    my_list = []
    for letter in plaintext:
        for key, value in my_dict.items():
            if key == letter:
                my_list.append(value)
    
    # Iterate over my_list
    # From the code_table sublist with index of element from my_list add the 
    # first element to the list cipher_txt and remove the element from the
    #     sublist, add it to the back
    
    cipher_txt = []   
    for item in my_list:
        cipher_txt.append(code_table[item][0])
        code_table[item].append(code_table[item].pop(0))
        
                    
    return cipher_txt