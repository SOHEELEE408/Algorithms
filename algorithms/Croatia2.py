class Main:
    str = input()
    croatia = ["c=","c-","dz=","d-","lj","nj","s=","z="]

    for i in croatia:
        str = str.replace(i,"*")
        print(str)
    print(len(str))