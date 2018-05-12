string1 = "Cat"
string2 = "Bat"

for i in range(len(string1)):
    for j in range(len(string2)):

        print("i: ",i, " <-----> ","j: ", j)
        print(string1[i],"  <---->  ",string2[j])

        if string1[i] == string2[j]:
            print("index: {0} of string1 matches with index: {1} of string2".format(i,j))
            print(i,j)

        print("\n #############")
