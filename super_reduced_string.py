def super_reduced_string(string_s):
    i = 0
    while i < len(string_s)-1:
        if string_s[i]==string_s[i+1]:
            string_s = string_s[:i] + string_s [i+2:]
            i = 0
        else:
            i += 1

    if string_s == "":
        return "Empty string"
    else:
        return string_s

string_s = input("Ingrese una cadena de texto: ")
string = super_reduced_string(string_s)

print(string)