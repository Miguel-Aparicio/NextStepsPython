def principal():
    cadena = input("Introduce una cadena ==> ")

    for i in range(len(cadena)):
        print(f"{cadena[i]}\n")
        
if __name__=="__main__":
   principal()