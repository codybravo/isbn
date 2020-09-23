class Isbn:
    def __init__(self,isbn):
        self.isbn = isbn
        self.isbn = list(self.isbn)
    
        
    
    def isbn_check(self):
        if (len(self.isbn) == 10) or (len(self.isbn) == 13):
            check = self.isbn[len(self.isbn)-1]
            del self.isbn[len(self.isbn)-1]
        elif (len(self.isbn) == 9) or (len(self.isbn) == 11) or (len(self.isbn) == 12):
            check = 'x'
        else:
            print("length of ISBN/UPC is incorrect!")
        self.isbn = [ int(i) for i in self.isbn ]
        return self.isbn, check
    
    def isbn_valid(self):
        for i in range(len(self.isbn)):
            if self.isbn[i] == 'x' or self.isbn[i] == 'X':
                self.isbn[i] = 10
        self.isbn = [ int(item) for item in self.isbn ]
        return self.isbn
    
    def isbn_missing(self):
        newlist = []
        for item in self.isbn:
            if item.isdigit() == True :
                newlist.append(int(item))
            else:
                check = item
                newlist.append('x')
        self.isbn = newlist[:] 
        return self.isbn, check
    
    


class IsbnValidation:
    def __init__(self,isbn):
        self.isbn = isbn
        self.isbn = isbn_out
        self.temp = self.isbn[:]
        if option != 1 and option != 5:
            self.check = check_out
        if option == 6 or option == 5 or option == 4 or option == 3 or option == 6:
            self.cond = False
        else:
            self.cond = True
        self.total = 0
        

    def print2(self,listing,v1,v2,v3):
        print("\n=> ",end="")
        print(*listing,sep="+",end="") 
        print(f'{v1} = {v2}(mod{v3})\n')
        
        
    def print1(self,value1,value2, value3):
        f1st = []
        [ f1st.append(f'({self.temp[i]}*{i+1})') for i in range(len(self.temp)) ]
        if self.cond == True:
            print(f'\n=> ',end="")
            print(*f1st,sep='+',end="")
            print(value1,end=" = ")
            print(f'{value2}(mod{value3})',end="\n\n")
        else:
            pass
        print(f'=> ',end="")
        print(*self.isbn,sep='+',end="")
        print(value1,end=" = ")
        print(f'{value2}(mod{value3})',end="\n\n")
        print(f'=> {self.total}{value1} = {value2}(mod{value3})',end="\n\n")

    
    def oper_valid(self):
        print("\nIf the above ISBN is correct it must hold the following congruence.")
        for i in range(len(self.isbn)):
            self.isbn[i] = self.isbn[i] * (i+1)
            self.total = self.isbn[i] + self.total
        self.print1(value1="",value2=0, value3=11)
        mod = self.total % 11
        if mod == 0:
            print("Hence the given ISBN is valid")
        else:
            print("Hence the given ISBN is not valid")
        
    
    def check_10(self):
        for i in range(len(self.isbn)):
            self.isbn[i] = self.isbn[i] * (i+1)
            self.total = self.total + self.isbn[i]
        self.print1(value1="",value2=self.check, value3=11)
        mod = self.total % 11
        print(f'=> {self.total} = {mod}(mod11)\n')
        print(f"Hence the check digit '{self.check}' = {mod}")

        
    def check_13(self):
        list2 = []
        for i in range(len(self.isbn)):
            j = i+1
            if (j%2) == 0:
                mul_var = 3
            else:
                mul_var = 1
            list2.append(f'({self.isbn[i]}*{mul_var})')
            self.isbn[i] = self.isbn[i] * mul_var
            self.total = self.isbn[i] + self.total
            mod = self.total % 10
            mod = 10 - mod
            if mod == 10 :
                mod = 10 - mod
        self.print2(listing=list2,v1=self.check,v2=0,v3=10)
        self.print1(value1="+"+self.check,value2="0",value3=10)
        print(f"Hence the check digit '{self.check}' = {mod}")
            
    
    def missing_digit(self):
        list2 = []
        for i in range(len(self.isbn)):
            list2.append(f'({self.isbn[i]}*{i+1})')
            if self.isbn[i] == 'x' :
                index1 = i+1
                self.check = 'x'
                self.isbn[i] = 'x'
            else:
                self.isbn[i] = self.isbn[i] * (i+1) 
                self.total = self.total + self.isbn[i]
        del self.isbn[index1-1]
        print("\nLet x be the missing digit then")
        self.print2(listing=list2,v1="",v2=0,v3=11)
        self.print1(value1=f'+{index1}x',value2=0,value3=11)
        mod = self.total % 11
        print(f'=> {mod}+{index1}{self.check} = 0(mod11)',f'=> {index1}{self.check} = {-mod}(mod11)',sep="\n\n",end="\n")
        result = 0
        for i in range(10):
            for j in range(10):
                temp = i * 11
                if (temp-(j*index1)) == mod:
                    result = j
        print(f'\nHence missing digit {self.check} = {result}')
    
    def upc_validation(self):
        list2 = []
        print("\nGiven UPC will be correct if it satisfies the congruences.")
        for i in range(len(self.isbn)):
            j = (i+1) % 2
            if j == 0:
                mul_var = 3
            else:
                mul_var = 1
            list2.append(f'({self.isbn[i]}*{mul_var})')
            self.isbn[i] = self.isbn[i] * mul_var
            self.total = self.total + self.isbn[i]
        self.print2(listing=list2,v1="",v2=0,v3=10)
        self.print1(value1="",value2=0,value3=10)
        mod = self.total % 10
        print(f'=> {self.total} = {mod}(mod10)\n')
        if mod == 0:
            print("Hence the given code is a correct UPC")
        else:
            print("Hence the given code is not correct UPC")
                
    def upc_check(self):
        list2 = []
        for i in range(len(self.isbn)):
            j = (i+1)%2
            if j == 0:
                var1 = 3
            else:
                var1 = 1
            list2.append(f'({self.isbn[i]}*{var1})')
            self.isbn[i] = self.isbn[i] * var1
            self.total = self.total + self.isbn[i]
        if len(self.isbn) == 12 :
            var2 = 1
        else:
            var2 = 3
        mod = self.total % 10
        print("\nLet x be the check digit then from the congruence.")
        self.print2(listing=list2,v1=f'+{var2}{self.check}',v2=0,v3=10)
        self.print1(value1=f'+{var2}{self.check}',value2=0,value3=10)
        for i in range(10):
            for j in range(10):
                temp = i *10
                if (temp-(j*var2)) == mod:
                    result = j
        print(f'=> {var2}{self.check} = -{mod}(mod10)',end="\n\n")
        print(f"So the Check digit '{self.check}' = {result}")
                
        


###
print('''
                    ISBN
1. Validate ISBN
2. Find the check digit of 10-digit ISBN
3. Find the check digit of 13-digit ISBN
4. Find missing digit of a ISBN
5. Validation of UPC
6. Find the Check digit of UPC code
7. Help
''')

option = int(input('Enter option : '))
if option == 5 or option == 6:
    isbn = input("\nUPC : ")
else:
    isbn = input("\nISBN : ")
i = Isbn(isbn)

if option == 1:
    isbn_out = i.isbn_valid()
    k = IsbnValidation(isbn)
    print(k.oper_valid())
elif option == 2:
    isbn_out, check_out = i.isbn_check()
    k = IsbnValidation(isbn)
    print(k.check_10())
elif option == 3:
    isbn_out, check_out = i.isbn_check()
    k = IsbnValidation(isbn)
    print(k.check_13())
elif option == 4:
    isbn_out, check_out = i.isbn_missing()
    k = IsbnValidation(isbn)
    print(k.missing_digit())
elif option == 5:
    isbn_out = i.isbn_valid()
    k = IsbnValidation(isbn)
    print(k.upc_validation())
elif option == 6:
    isbn_out, check_out = i.isbn_check()
    k = IsbnValidation(isbn)
    print(k.upc_check())
else:
    exit()


    

        




