#nhap vao mot chuoi, dem xem co bao nhieu tu

#ham dem tu
def so_tu(text):
    words=text.split()
    print(words) #tach chuoi thanh array cho cac tu ['a', 'b']
    return len(words)

#main
text=input("Nhap vao chuoi:")
print("So tu trong chuoi:",so_tu(text))