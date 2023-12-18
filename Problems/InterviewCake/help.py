with open("./nums.txt", "r") as f:
    with open("./out.txt", "w") as o:
        n = ""
        l = f.readline()
        while l:
            n += l[:6] + "\n"
            l = f.readline()
        o.writelines(n)
