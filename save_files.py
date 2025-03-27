def luuFile():
    file=open('csdlSV.txt','w', encoding='utf-8')
    file.writelines("sv01;Tran Ngoc Hai;9.5\n")
    file.writelines("sv01;Tran Ngoc Hai;9.5\n")
    file.writelines("sv01;Tran Ngoc Hai;9.5\n")
    file.writelines("sv01;Tran Ngoc Hai;9.5\n")
    file.close()

def docFile():
    file=open('csdlSV.txt','r',encoding='utf-8')
    for line in file:
        print(line.strip())
    file.close()

docFile()