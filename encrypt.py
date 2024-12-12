Secret_Message="Lxwp{j}~uj}rxw|*)bx~)l{jltnm)}qn)lxmn7)]qn)ox{ln)r|)\][XWP)r}q)x~*"

for i in range(-20, 20):
    word = ""
    for char in Secret_Message:
        num = ord(char)
        num += i
        word += chr(num)
    if i == -9:
        print(word)
        break