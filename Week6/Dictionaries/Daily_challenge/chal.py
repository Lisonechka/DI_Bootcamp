text = input('Write the message: ')
ask_action = input('Do yo want  encrypt or decrypt message? :')
shift = int(input('what a shift:'))
encrypt_text = ''
decrypt_text = ''
if ask_action == "encrypt":
    for letter in text:
        encrypt_text += chr(ord(letter) + shift)
print(encrypt_text.strip())
if ask_action == "decrypt":
    for letter in text:
        decrypt_text += chr(ord(letter) - shift)
print(decrypt_text.strip())




    
    





