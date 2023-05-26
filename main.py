def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def main():
    print("{} と {} を足すと {}".format(1,2,add(1,2)))
    print("{} から {} を引くと {}".format(2,2,sub(1,2)))

if __name__ == '__main__':
    main()
