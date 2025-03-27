# This month is equivalent to which quarter?
#

def get_quarter(mo):
    if 1<=mo<=3:
        r="Quarter 1"
    elif 4<=mo<=6:
        r="Quarter 2"
    elif 7<=mo<=9:
        r="Quarter 3"
    elif 10<=mo<=12:
        r="Quarter 4"
    return r
# Insert month

mo=int(input("Insert a month(1-12):"))
print(f"Thang {mo} thuoc {get_quarter(mo)}")
