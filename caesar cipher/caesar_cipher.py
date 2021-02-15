def encription(plain_text):
    plain_text =  plain_text.upper()
    encripted_text = ""

    for i in range(len(plain_text)):
        c = plain_text[i]
        loc_of_c = alphabets.find(c)
        new_loc = (loc_of_c + shifting_key_value) % 26
        encripted_text = encripted_text + alphabets[new_loc]

    return encripted_text


alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

plain_text = input("Enter the message: ")
shifting_key_value = int(input("Enter the key value to shift: "))

print("The encripted text is : ")
print(encription(plain_text))