# 1)Distinguish between variable, constant and literals with examle.

#ANS:-

PYTHON VARIABLES:-

  **A variable is a named location used to store data in the memory.
    It is helpful to think of variables as a container that holds data that can be changed later in the program.
    For example:-  **name = value**
                     number = 10
    
Here,
    we have created a variable named number. We have assigned the value 10 to the variable.

OR,
  You can think of variables as a bag to store books in it and that book can be replaced at any time.
OR,
  Variables are like boxes that store data.
number = 10
number = 1.1
Initially, the value of number was 10. Later, it was changed to 1.1.

     **a) Assigning values to Variables in Python
     
          we can use the assignment operator "=" to assign a value to a variable.
     Example 1:
             Declaring and assigning value to a variable
             website = "apple.com"
             print(website)
    Output:-
             apple.com

    Example 2:
            Changing the value of a variable
            website = "apple.com"
            print(website)
         # assigning a new variable to website
            website = "sona.com"
            print(website)
    Output:-
            apple.com
            sona.com
   Example 3:
            Assigning multiple values to multiple variables
            a, b, c = 5, 3.2, "Hello"
            print (a)
            print (b)
            print (c)
       #If we want to assign the same value to multiple variables at once, we can do this as:
            x = y = z = "sona"

            print (x)
            print (y)
            print (z)
    Output:-
            5
            3.2
            'Hello'
            'sona'
            'sona'
            'sona'


CONSTANT :-

    **A constant is a type of variable whose value cannot be changed.
      It is helpful to think of constants as containers that hold information which cannot be changed later.
  #Assigning value to constant.
       constants are usually declared and assigned in a module.
       Here,
           the module is a new file containing variables, functions, etc
           which is imported to the main file.
           Inside the module, constants are written in all capital letters and underscores separating the words.

    Example:-
           Declaring and assigning value to a constant
  #Create a constant.py:

             PI = 3.14
             GRAVITY = 9.8
  #Create a main.py:

             import constant

             print(constant.PI)
             print(constant.GRAVITY)
    Output:-
             3.14
             9.8
      I create a constant.py module file. Then, I assign the constant value to PI and GRAVITY.
      After that, I create a main.py file and import the constant module. Finally, I print the constant value.

   #Rules and Naming Convention for Variables and constants:-
    
      A) Constant and variable names should have a combination of letters in lowercase (a to z)
         or uppercase (A to Z) or digits (0 to 9) or an underscore (_).

    Example:-
           snake_case
           MACRO_CASE
           camelCase
           CapWords

       B) If I want to create a variable name having two words, use underscore to separate them.

    Example:-
           my_name
           current_salary

      C) Use capital letters possible to declare a constant.

    Example:-
            PI
            G
            MASS
            SPEED_OF_LIGHT
            TEMP
      D) Never use special symbols like !, @, #, $, %, etc.
      E) Don't start a variable name with a digit.



LITERAL:-

      **Literal is a raw data given in a variable or constant.
        there are various types of literals.

      **they are as follows:-

         A)Numeric Literals:-
                      Numeric Literals are immutable (unchangeable).
                      Numeric literals can belong to 3 different numerical types: Integer, Float, and Complex.

            Example:-
                    How to use Numeric literals in Python?
                     a = 0b1010 #Binary Literals
                     b = 100 #Decimal Literal 
                     c = 0o310 #Octal Literal
                     d = 0x12c #Hexadecimal Literal

               #Float Literal:-
                  float_1 = 10.5 
                  float_2 = 1.5e2

              #Complex Literal:-
                  x = 3.14j

                  print(a, b, c, d)
                  print(float_1, float_2)
                  print(x, x.imag, x.real)

         Output:-

                10 100 200 300
                10.5 150.0
                3.14j 3.14 0.0
In the above program,
         I assigned integer literals into different variables.
         Here,
            a is binary literal,
            b is a decimal literal,
            c is an octal literal and
            d is a hexadecimal literal.
         When I print the variables, all the literals are converted into decimal values.
         10.5 and 1.5e2 are floating-point literals.
         1.5e2 is expressed with exponential and is equivalent to 1.5 * 102.
         I assigned a complex literal i.e 3.14j in variable x.
         Then I use imaginary literal (x.imag) and real literal (x.real) to create imaginary and real parts of complex numbers.
         To learn more about Numeric Literals, refer to Python Numbers.

     B)String literals:-
                 A string literal is a sequence of characters surrounded by quotes.
                 We can use both single, double, or triple quotes for a string.
                 And, a character literal is a single character surrounded by single or double quotes.

         Example:-
               How to use string literals in Python?
               strings = "This is Python"
               char = "C"
               multiline_str = """This is a multiline string with more than one line code."""
               unicode = u"\u00dcnic\u00f6de"
               raw_str = r"raw \n string"

              print(strings)
              print(char)
              print(multiline_str)
              print(unicode)
              print(raw_str)
       Output:-

             This is Python
             C
             This is a multiline string with more than one line code.
             Ünicöde
             raw \n string
   In the above program, This is Python is a string literal and C is a character literal.


      C) Boolean literals:-
                   A Boolean literal can have any of the two values: True or False.

           Example:-
                 How to use boolean literals in Python?

                 x = (1 == True)
                 y = (1 == False)
                 a = True + 4
                 b = False + 10

                 print("x is", x)
                 print("y is", y)
                 print("a:", a)
                 print("b:", b)
          Output:-

                 x is True
                 y is False
                 a: 5
                 b: 10
    In the above program, we use boolean literal True and False.
    In Python, True represents the value as 1 and False as 0.
    The value of x is True because 1 is equal to True.
    And, the value of y is False because 1 is not equal to False.

  Similarly,
       I can use the True and False in numeric expressions as the value.
       The value of a is 5 because we add True which has a value of 1 with 4.
  Similarly,
       b is 10 because we add the False having value of 0 with 10.

     D)Special literals:-
                 Python contains one special literal i.e. None.
                 We use it to specify that the field has not been created.

        Example:-
               How to use special literals in Python?

              drink = "Available"
              food = None

             def menu(x):
                if x == drink:
                    print(drink)
                else:
                    print(food)

            menu(drink)
            menu(food)
      Output:-
             Available
             None
   In the above program, I define a menu function. Inside menu, when we set the argument as drink then, it displays Available.
   And, when the argument is food, it displays None.

    E) Literal Collections:-
                    There are four different literal collections List literals, Tuple literals, Dict literals, and Set literals.

        Example:-
              How to use literals collections in Python?

             fruits = ["apple", "mango", "orange"] #list
             numbers = (1, 2, 3) #tuple
             alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} #dictionary
             vowels = {'a', 'e', 'i' , 'o', 'u'} #set

             print(fruits)
             print(numbers)
             print(alphabets)
             print(vowels)
      Output:-

            ['apple', 'mango', 'orange']
            (1, 2, 3)
            {'a': 'apple', 'b': 'ball', 'c': 'cat'}
            {'e', 'a', 'o', 'i', 'u'}
  In the above program, we created a list of fruits, a tuple of numbers, a dictionary dict having values with keys designated to each value and a set of vowels.





# 2) Define identifiers and datatype.
      
#ANS:-

IDENTIFIER:-
           An identifier is a name given to entities like class, functions, variables, etc.
           It helps to differentiate one entity from another.

  #Rules for writing identifiers:-

     1) Identifiers can be a combination of letters in lowercase (a to z) or uppercase (A to Z) or digits (0 to 9) or an underscore _.
        Names like myClass, var_1 and print_this_to_screen, all are valid example.
     2) An identifier cannot start with a digit. 1variable is invalid, but variable1 is a valid name.
     3) Keywords cannot be used as identifiers.
           global = 1
      Output:-
           File "<interactive input>", line 1
           global = 1
                  ^
      SyntaxError: invalid syntax
               We cannot use special symbols like !, @, #, $, % etc. in our identifier.
               a@ = 0

     Output:-
            File "<interactive input>", line 1
            a@ = 0
             ^
     SyntaxError: invalid syntax
    4) An identifier can be of any length.
  Things to Remember:-
              Python is a case-sensitive language. This means, Variable and variable are not the same.
              Always give the identifiers a name that makes sense. While c = 10 is a valid name,
              writing count = 10 would make more sense, and it would be easier to figure out
              what it represents when you look at your code after a long gap.



DATATYPES:-
        Every value in Python has a datatype. Since everything is an object in Python programming,
        data types are actually classes and variables are instance (object) of these classes.

        There are various data types in Python. Some of the important types are listed below.

  1) Python Numbers:-
              Integers, floating point numbers and complex numbers fall under Python numbers category.
              They are defined as int, float and complex classes in Python.

              I can use the type() function to know which class a variable or a value belongs to.
              Similarly, the isinstance() function is used to check if an object belongs to a particular class.

                a = 5
                print(a, "is of type", type(a))

                a = 2.0
                print(a, "is of type", type(a))

                a = 1+2j
                print(a, "is complex number?", isinstance(1+2j,complex))
        Output:-

                5 is of type <class 'int'>
                2.0 is of type <class 'float'>
                (1+2j) is complex number? True
            Integers can be of any length, it is only limited by the memory available.

            A floating-point number is accurate up to 15 decimal places.
            Integer and floating points are separated by decimal points.
            1 is an integer, 1.0 is a floating-point number.

            Complex numbers are written in the form, x + yj, where x is the real part and y is the imaginary part.
        Examples:-

            >>> a = 1234567890123456789
            >>> a
                1234567890123456789
            >>> b = 0.1234567890123456789
            >>> b
                0.12345678901234568
            >>> c = 1+2j
            >>> c
               (1+2j)


   2) Python List:-
               List is an ordered sequence of items. It is one of the most used datatype in Python and is very flexible.
               All the items in a list do not need to be of the same type.

              Declaring a list is pretty straight forward.
              Items separated by commas are enclosed within brackets [ ].

              a = [1, 2.2, 'python']
              I can use the slicing operator [ ] to extract an item or a range of items from a list.
              The index starts from 0 in Python.

              a = [5,10,15,20,25,30,35,40]

              # a[2] = 15
              print("a[2] = ", a[2])

              # a[0:3] = [5, 10, 15]
              print("a[0:3] = ", a[0:3])

             # a[5:] = [30, 35, 40]
             print("a[5:] = ", a[5:])
       Output:-

             a[2] =  15
             a[0:3] =  [5, 10, 15]
             a[5:] =  [30, 35, 40]
             
          EG:-
             Lists are mutable, meaning, the value of elements of a list can be altered.

             a = [1, 2, 3]
             a[2] = 4
             print(a)

     Output:-

            [1, 2, 4]
            
  3) Python Tuple:-
  
               Tuple is an ordered sequence of items same as a list.
               The only difference is that tuples are immutable.
               Tuples once created cannot be modified.

              Tuples are used to write-protect data and are usually faster than lists as they cannot change dynamically.

              It is defined within parentheses () where items are separated by commas.

              t = (5,'program', 1+3j)
              I can use the slicing operator [] to extract items but we cannot change its value.

              t = (5,'program', 1+3j)

        # t[1] = 'program'
             print("t[1] = ", t[1])

        # t[0:3] = (5, 'program', (1+3j))
             print("t[0:3] = ", t[0:3])

        # Generates error
        # Tuples are immutable
             t[0] = 10
     Output:-

         t[1] =  program
         t[0:3] =  (5, 'program', (1+3j))
        Traceback (most recent call last):
       File "test.py", line 11, in <module>
         t[0] = 10
     TypeError: 'tuple' object does not support item assignment

     
  4) Python Strings:-
  
               String is sequence of Unicode characters.
               I can use single quotes or double quotes to represent strings.
               Multi-line strings can be denoted using triple quotes,*'' OR ""*
     EG:-
         s = "This is a string"
         print(s)
         s = '''A multiline
         string'''
         print(s)
    Output:-
        This is a string
        A multiline
        string
        
         Just like a list and tuple, the slicing
         operator [ ] can be used with strings.
         Strings, however, are immutable.

     EG:-
            s = 'Hello world!'

            # s[4] = 'o'
            print("s[4] = ", s[4])

            # s[6:11] = 'world'
            print("s[6:11] = ", s[6:11])

            # Generates error
            # Strings are immutable in Python
            s[5] ='d'
    Output:-

            s[4] =  o
            s[6:11] =  world
            Traceback (most recent call last):
              File "<string>", line 11, in <module>
            TypeError: 'str' object does not support item assignment


    5) Python Set:-
                Set is an unordered collection of unique items.
                Set is defined by values separated by comma inside braces { }.
                Items in a set are not ordered.
            EG:-
                a = {5,2,3,1,4}

                # printing set variable
                print("a = ", a)

                # data type of variable a
                print(type(a))
            Output:-

                a =  {1, 2, 3, 4, 5}
                <class 'set'>
                
         I can perform set operations like union, intersection on two sets.
         Sets have unique values. They eliminate duplicates.
    EG:-
            a = {1,2,2,3,3,3}
            print(a)
    Output:-

            {1, 2, 3}
            
        Since, set are unordered collection, indexing has no meaning. Hence, the slicing operator [] does not work.

        >>> a = {1,2,3}
        >>> a[1]
        Traceback (most recent call last):
          File "<string>", line 301, in runcode
          File "<interactive input>", line 1, in <module>
        TypeError: 'set' object does not support indexing

    6) Python Dictionary:-
                    Dictionary is an unordered collection of key-value pairs.

                    It is generally used when we have a huge amount of data.
                    Dictionaries are optimized for retrieving data.
                    We must know the key to retrieve the value.

                    In Python, dictionaries are defined within braces {} with each item being a pair in the form key:value.
                    Key and value can be of any type.

                    >>> d = {1:'value','key':2}
                    >>> type(d)
                    <class 'dict'>
                    I use key to retrieve the respective value. But not the other way around.
            EG:-
                    d = {1:'value','key':2}
                    print(type(d))

                    print("d[1] = ", d[1]);

                    print("d['key'] = ", d['key']);

                    # Generates error
                    print("d[2] = ", d[2]);
          Output:-

                <class 'dict'>
                d[1] =  value
                d['key'] =  2
                Traceback (most recent call last):
                      File "<string>", line 9, in <module>
                KeyError: 2

                


# 3) Write a program to declare two variable , take one of them from
     user and determine one by self then compare and print them.


#ANS:-

     name1=sona
     name2=input("Enter the word:-")
     print(name1==nam2)
     print(name1)

 Output:-
         Enter the word:-babyqueen
         False
         sona

























      
