#!/user/python

class Printer(str):
    def __init__(self, hellostring):
        if not hellostring:
            hellostring = ""
        
        self.__setstr(hellostring)

    def __setstr(self, string_to_set):
        self.__string = string_to_set
    
    def do_print(self):
        print(self.__string)

def main():
    s = "Hello, World!"
    p = Printer(s)
    p.do_print()

if __name__ == '__main__':
    main()
