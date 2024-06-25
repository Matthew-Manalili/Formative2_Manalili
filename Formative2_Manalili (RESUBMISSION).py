#!/usr/bin/env python
# coding: utf-8

# In[24]:


def shift_letter(letter, shift):
    if letter==" ":
        return" "
    else:
        if shift>26:
            shift=shift%26
        letter=letter.upper()
        letters="ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
        letter=letters[letters.find(letter)+shift]
        return letter
def caesar_cipher(message,shift):
    number_letters=len(message)
    added_letter=""
    if shift>26:
        shift=shift%26
    while number_letters!=0:
        capitalize=message.upper()
        letters="ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if capitalize[len(capitalize)-number_letters]!=" ":
            add=letters[letters.find(capitalize[len(capitalize)-number_letters])+shift]
        else:
            add=" "
        added_letter=added_letter+add
        number_letters-=1
    shifted_message=added_letter
    return shifted_message
def shift_by_letter(letter, shift):
    letter=letter.upper()
    shift=shift.upper()
    if letter!=" ":
        letters="ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
        letter=letters[letters.find(letter)+letters.find(shift)]
        return letter
    else:
        return " "
def vigenere_cipher(message,shift):
    number_letters=len(message)
    number_shift=len(shift)
    added_letter=""
    while number_letters!=0:
        capitalized_message=message.upper()
        capitalized_shift=shift.upper()
        letters="ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if number_shift!=0:
            if shift[len(capitalized_shift)-number_shift]!=" ":
                shift_amount=letters.find(capitalized_shift[len(capitalized_shift)-number_shift])
            else:
                shift_amount=0
        else:
            number_shift=len(shift)
            shift_amount=letters.find(capitalized_shift[len(capitalized_shift)-number_shift])
        
        if capitalized_message[len(capitalized_message)-number_letters]!=" ":
            add=letters[letters.find(capitalized_message[len(capitalized_message)-number_letters])+shift_amount]
        else:
            add=" "
        added_letter=added_letter+add
        number_letters-=1
        number_shift-=1
    shifted_message=added_letter
    return shifted_message
    
def scytale_cipher(message,shift):
    number_letters=len(message)
    encrypted_message=""
    i=0
    j=0
    
    if number_letters%shift!=0:
        while number_letters%shift!=0:
            message=message+"_"
            number_letters=len(message)
    while i!=number_letters/shift:
        while j!=shift:
            encrypted_message+=message[int(i+(j*(number_letters/shift)))]
            j+=1
        i+=1
        j=0
       
    return encrypted_message
def scytale_decipher(message,shift):
    number_letters=len(message)
    decrypted_message=""
    i=0
    j=0
    while i!=shift:
        while j!=number_letters/shift:
            decrypted_message+=message[int(i+(j*shift))]
            j+=1
        i+=1
        j=0
    return decrypted_message

vigenere_cipher("ABCDEFG","B")


# In[ ]:




