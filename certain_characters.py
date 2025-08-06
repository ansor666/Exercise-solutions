#The function returns a (possibly empty) string, which contains only those characters from "text" (first parameter) that are present in "chars".


def valid(text,chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    lst = [char for char in text if char in chars]
    return "".join(lst)


#####################################################
if __name__ == "__main__":
    print(valid("Barking"))
    print(valid("KL754", "0123456789"))   
    print(valid("BEAN", "abcdefghijklmnopqrstuvwxyz"))