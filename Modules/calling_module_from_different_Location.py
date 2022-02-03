#accessing module file from cureent and other file
def main():
    print("This is main window executed!!!")

def optional():
    print("Module Executed form other File!!!")

if __name__=='__main__':
    main()
elif __name__=='calling_module_from_different_Location':
    optional()
print("This is an example ")