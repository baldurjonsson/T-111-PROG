# Á meðan input er stærra eða jafnt og núll.
# berið það saman við max_int. Ef input er stærra en max_int, yfirskrifð sem max_int og endurtakið.
# Ef input er neikvætt, ljúkið keyrslu.

max_int = 0

while (num_int := int(input("Input a number: "))) >= 0:
    if num_int > max_int:
        max_int = num_int

print("The maximum is", max_int)  # Do not change this line
