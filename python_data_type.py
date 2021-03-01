while True:
      print("\n")
      print("𝖈𝖍𝖎𝖓𝖒𝖆𝖞29𝖍𝖚𝖇 : https://github.com/chinmay29hub/python-data-types")
      print("\n===================Main Menu==================\n")
      print("1. Strings")
      print("2. Lists")
      print("3. Tuples")
      print("4. Dictionaries")
      print("5. Exit\n")
      choice_1 = int(input("Enter Your Choice : "))
      
      if choice_1 == 1:
         while True:
               print("\n================String Operations==============\n")
               print("1. Slicing")
               print("2. Modifying")
               print("3. Concatenate")
               print("4. Formatting")
               print("5. Escaping Characters")
               print("6. Exit\n")
               choice_2 = int(input("Choose one of the operation : "))
               
               if choice_2 == 1:
                  while True:
                        print("\n===================Slicing Operation=================\n")
                        print("1. Slice from Both Sides ")
                        print("2. Slice from the Start")
                        print("3. Slice To the End")
                        print("4. Negative Slicing")
                        print("5. Exit\n")
                        choice_3 = int(input("\nEnter your Slicing Operation\n"))
                  
                        if choice_3 == 1:
                           print("Assuming String : Hello, World!\n")
                           print("Performing Operation : b[2:5]\n")
                           b = "Hello, World!"
                           print("Answer is : ",b[2:5])
                        elif choice_3 == 2:
                             print("Assuming String : Hello, World!\n")
                             print("Performing Operation : b[:5]\n")
                             b = "Hello, World!"
                             print("Answer is : ",b[:5])
                        elif choice_3 == 3:
                             print("Assuming String : Hello, World!\n")
                             print("Performing Operation : b[2:]\n")
                             b = "Hello, World!"
                             print("Answer is : ",b[2:])
                        elif choice_3 == 4:
                             print("Assuming String : Hello, World!\n")
                             print("Performing Operation : b[-5:-2]\n")
                             b = "Hello, World!"
                             print("Answer is : ",b[-5:-2])
                        elif choice_3 == 5:
                             break
                        else:
                            print("\nInvalid Choice\n")
               if choice_2 == 2:
                  while True:
                        print("\n=================Modifying Operations==================\n")
                        print("1. Upper Case")
                        print("2. Lower Case")
                        print("3. Remove Whitespace")
                        print("4. Replace String")
                        print("5. Split String")
                        print("6. Exit")
                        choice_4 = int(input("\nEnter Which Operation you want to Perform\n"))
                  
                        if choice_4 == 1:
                           a = "Hello, World!"
                           print("Assuming String: Hello, World!\n ")
                           print("Performing Operation : a.upper()\n")
                           print("Answer is : ",a.upper())
                        elif choice_4 == 2:
                             a = "Hello, World!"
                             print("Assuming String: Hello, World!\n ")
                             print("Performing Operation : a.lower()\n")
                             print("Answer is : ",a.lower())
                        elif choice_4 == 3:
                             a = "Hello, World!"
                             print("Assuming String: Hello, World!\n ")
                             print("Performing Operation : a.strip()\n")
                             print("Answer is : ",a.strip())
                        elif choice_4 == 4:
                             a = "Hello, World!"
                             print("Assuming String: Hello, World!\n ")
                             print("Performing Operation : a.replace(\"H\", \"J\")\n")
                             print("Answer is : ",a.replace("H", "J"))
                        elif choice_4 == 5:
                             a = "Hello, World!"
                             print("Assuming String: Hello, World!\n ")
                             print("Performing Operation : a.split(\",\")\n")
                             print("Answer is : ",a.split(","))
                        elif choice_4 == 6:
                             break
                        else:
                            print("\ninvalid Choice\n")
                  
               elif choice_2 == 3:
                    print("\n===================Concatenate Operation======================\n")
                    print("Asumming strings: a = \"Hello\"\",\" b = \"World!\"")
                    print("Performing Operation : c = a + b")
                    a = "Hello"
                    b = "World"
                    c = a + b
                    print("Answer is : ",c)
               elif choice_2 == 4:
                    print("\n======================Formatting Operations=====================\n")
                    print("we cannot combine strings and numbers\n")
                    print("But with the help of \"format()\" we can combine\n")
                    age = 36
                    print("------->Example<-------")
                    print("age = 36")
                    txt = "My name is John, and I am {}"
                    print("txt = My name is John, and I am \"{}\"")
                    print("Answer is : ",txt.format(age))
               elif choice_2 == 5:
                    print("\n====================Escaping Characters Operations=================\n")
                    print("We can use \"backward slash\"(\)\"\" for escaping the systax error\n")
                    print("In many places I have used this method in the code, You can browse the code\n")
                    txt = "We are the so-called \"Vikings\" from the north."
                    print("Assuming String : txt = We are the so-called \"Vikings\" from the north.")
                    print("Answer is : ",txt)
               elif choice_2 == 6:
                    break
               else:
                   print("\nInvalid Choice\n")   
      if choice_1 == 2:
         while True:
               print("\n==========================List Operations=========================\n")
               print("1.  Access List Items")
               print("2.  Change List Items")
               print("3.  Add List Items")
               print("4.  Remove List Items")
               print("5.  Loop Lists")
               print("6.  List Comprehension")
               print("7.  Sort Lists")
               print("8.  Copy Lists")
               print("9.  Join Lists")
               print("10. Exit\n")
               choice_5 = int(input("Enter Your Choice: "))
         
               if choice_5 == 1:
                  while True:
                        print("\n=============Accessing List Items Operations=============\n")
                        print("1. Positive Indexing")
                        print("2. Negative Indexing")
                        print("3. Range Of Indexes")
                        print("4. Exit\n")
                        choice_6 = int(input("Enter Which operation You want: "))
                        
                        if choice_6 == 1:
                           print("List items are indexed and you can access them by referring to the index number\n")
                           print("Assuming List : thislist = [\"apple\", \"banana\", \"cherry\"]")
                           thislist = ["apple", "banana", "cherry"]
                           print("Performing Operation : thislist[1]")
                           print("Answer is : ",thislist[1])
                        elif choice_6 == 2:
                             print("Negative indexing means start from the end")
                             print("-1 refers to the last item, -2 refers to the second last item etc.\n")
                             print("Assuming String : thislist = [\"apple\", \"banana\", \"cherry\"]")
                             thislist = ["apple", "banana", "cherry"]
                             print("Performing Operation : thislist[-1]")
                             print("Answer is : ",thislist[-1])
                        elif choice_6 == 3:
                             print("You can specify a range of indexes by specifying where to start and where to end the range.")
                             print("For eg: Return the third, fourth, and fifth item\n")
                             print("Assuming String : thislist = [\"apple\", \"banana\", \"cherry\", \"orange\", \"kiwi\", \"melon\", \"mango\"]")
                        elif choice_6 == 4:
                             break
                        else:
                            print("\nInvalid Choice\n")     
               elif choice_5 == 2:
                    while True:
                          print("\n=================Change List items Operations================\n")
                          print("1. Change Item Value")
                          print("2. Change a Range Of Item Values")
                          print("3. Insert Items")
                          print("4. Exit\n")
                          choice_7 = int(input("Enter Your Choice : "))
                          
                          if choice_7 == 1:
                             print("To change the value of a specific item, refer to the index number")
                             print("Assuming List : thislist = [\"apple\", \"banana\", \"cherry\"]")
                             thislist = ["apple", "banana", "cherry"]
                             print("Performing Operation : thislist[1] = \"blackcurrant\"")
                             thislist[1] = "blackcurrant"
                             print("Answer is : ",thislist)
                          elif choice_7 == 2:
                               print("To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values")
                               print("For eg : Change the values \"banana\" and \"cherry\" with the values \"blackcurrant\" and \"watermelon\":")
                               print("Assuming String : thislist = [\"apple\", \"banana\", \"cherry\", \"orange\", \"kiwi\", \"mango\"]")
                               thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
                               print("Performing Operation : thislist[1:3] = [\"blackcurrant\", \"watermelon\"]")
                               thislist[1:3] = ["blackcurrant", "watermelon"]
                               print("Answer is ",thislist)
                          elif choice_7 == 3:
                               print("To insert a new list item, without replacing any of the existing values, we can use the insert() method")
                               print("Assuming String : thislist = [\"apple\", \"banana\", \"cherry\"]")
                               thislist = ["apple", "banana", "cherry"]
                               print("Performing Operation : thislist.insert(2, \"watermelon\")")
                               thislist.insert(2, "watermelon")
                               print("Answer Is : ",thislist)
                          elif choice_7 == 4:
                               break
                          else:
                              print("\nInvalid Choice\n")
               elif choice_5 == 3:
                    while True:
                          print("\n================Add List Items Operations================\n")
                          print("1. Append Items")
                          print("2. Extend List")
                          print("3. Add any Iterable")
                          print("4. Exit\n")
                          choice_8 = int(input("Enter Your Choice : "))
                    
                          if choice_8 == 1:
                             print("To add an item to the end of the list, use the append() method")
                             print("Assuming List : thislist = [\"apple\", \"banana\", \"cherry\"]")
                             thislist = ["apple", "banana", "cherry"]
                             print("Performing Operation : thislist.append(\"orange\")")
                             thislist.append("orange")
                             print("Answer Is ",thislist)
                          elif choice_8 == 2:
                               print("To append elements from another list to the current list, use the extend() method.")
                               print("Assuming First List : thislist = [\"apple\", \"banana\", \"cherry\"]")
                               thislist = ["apple", "banana", "cherry"]
                               print("Assuming Second List : tropical = [\"mango\", \"pineapple\", \"papaya\"]")
                               tropical = ["mango", "pineapple", "papaya"]
                               print("Performing Operation : thislist.extend(tropical)")
                               print("Answer Is : ",thislist)
                          elif choice_8 == 3:
                               print("The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.)")
                               print("Assuming List : thislist = [\"apple\", \"banana\", \"cherry\"]")
                               thislist = ["apple", "banana", "cherry"]
                               print("Assuming Tuple : thistuple = (\"kiwi\", \"orange\")")
                               thistuple = ("kiwi", "orange")
                               print("Performing Operation : thislist.extend(thistuple)")
                               print("Answer Is ",thislist)
                          elif choice_8 == 4:
                               break
                          else:
                             print("\nInvalid Choice\n")     
               elif choice_5 == 4:
                    while True:
                          print("\n==================Remove List Items Operations=================\n")
                          print("1. Remove Specified Item")
                          print("2. Remove Specified Index")
                          print("3. Clear the List")
                          print("4. Exit\n")
                          choice_9 = int(input("Enter Your Choice : "))
                          
                          if choice_9 == 1:
                             print("Assuming List : thislist = [\"apple\", \"banana\", \"cherry\"]")
                             thislist = ["apple", "banana", "cherry"]
                             print("Performing Operation : thislist.remove(\"banana\")")
                             thislist.remove("banana")
                             print("Answer Is : ",thislist)
                          elif choice_9 == 2:
                               print("Assuming List : thislist = [\"apple\", \"banana\", \"cherry\"]")
                               thislist = ["apple", "banana", "cherry"]
                               print("Performing Operation : thislist.pop(1)")
                               thislist.pop(1)
                               print("Answer Is : ",thislist.pop(1))
                          elif choice_9 == 3:
                               print("The clear() method empties the list.")
                               print("Assuming List : thislist = [\"apple\", \"banana\", \"cherry\"]")
                               thislist = ["apple", "banana", "cherry"]
                               print("Performing Operation : thislist.clear()")
                               thislist.clear()
                               print("Answer Is : ",thislist.clear())
                          elif choice_9 == 4:
                               break
                          else:
                              print("\nInvalid Choice\n")
               elif choice_5 == 5:
                    while True:
                          print("\n==================Loop Lists Operations===================\n")
                          print("1. Loop through a List")
                          print("2. Loop through the Index Numbers")
                          print("3. Loop using a While Loop")
                          print("4. Loop using List Comprehension")
                          print("5. Exit\n")
                          choice_10 = int(input("Enter Your Choice"))
                          
                          if choice_10 == 1:
                             print("Assuming List : thislist = [\"apple\", \"banana\", \"cherry\"]")
                             thislist = ["apple", "banana", "cherry"]
                             print("Performing Operation : for x in thislist:")
                             print("                           print(x)")
                             for x in thislist:
                                 print("Answer is : ",x)
                          elif choice_10 == 2:
                               print("Assuming List : thislist = [\"apple\", \"banana\", \"cherry\"]")
                               thislist = ["apple", "banana", "cherry"]
                               print("Performing Operation : for i in range(len(thislist)):")
                               print("                           print(thislist[i])")
                               for i in range(len(thislist)):
                                   print("Answer is : ",thislist[i])
                          elif choice_10 == 3:
                               print("Assuming List : thislist = [\"apple\", \"banana\", \"cherry\"]")
                               thislist = ["apple", "banana", "cherry"]
                               print("Performing Operation : i = 0")
                               print("                       while i < len(thislist):")
                               print("                             print(thislist[i])")
                               print("                             i = i + 1")
                               while i < len(thislist):
                                     print("Answer Is : ",thislist[i])
                                     i = i + 1
                          elif choice_10 == 4:
                               print("Assuming List : thislist = [\"apple\", \"banana\", \"cherry\"]")
                               thislist = ["apple", "banana", "cherry"]
                               print("Performing Operation : [print(x) for x in thislist]")
                               [print("Answer is : ",x) for x in thislist]
                          elif choice_10 == 5:
                               break
                          else:
                              print("\nInvalid Choice\n")     
               elif choice_5 == 6:
                    print("Assuming List : fruits = [\"apple\", \"banana\", \"cherry\", \"kiwi\", \"mango\"]")
                    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
                    print("Performing Operation : newlist = []")
                    print("                       for x in fruits:")
                    print("                           if \"a\" in x:")
                    print("                               newlist.append(x)")
                    print("                       print(\"Answer is : \",newlist)")
                    for x in fruits:
                        if "a" in x:
                           newlist.append(x)

                    print("Answer is : ",newlist)
               elif choice_5 == 7:
                    while True:
                          print("\n=======================Sort List Opeartions=====================\n")
                          print("1. Sort List Alphanumerically")
                          print("2. Sort Descending")
                          print("3. Case Insensitive Sort")
                          print("4. Reverse Order")
                          print("5. Exit\n")
                          choice_11 = int(input("Enter Your Choice : "))
                          
                          if choice_11 == 1:
                             print("Assuming List : thislist = [\"orange\", \"mango\", \"kiwi\", \"pineapple\", \"banana\"]")
                             thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
                             print("Performing Operation : thislist.sort()")
                             thislist.sort()
                             print("Answer is : ",thislist)
                          elif choice_11 == 2:
                               print("Assuming List : thislist = [\"orange\", \"mango\", \"kiwi\", \"pineapple\", \"banana\"]")
                               thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
                               print("Performing Operation : thislist.sort(reverse = True)")
                               thislist.sort(reverse = True)
                               print("Answer is : ",thislist)
                          elif choice_11 == 3:
                               print("Assuming List : thislist = [\"banana\", \"Orange\", \"Kiwi\", \"cherry\"]")
                               thislist = ["banana", "Orange", "Kiwi", "cherry"]
                               print("Performing Operation : thislist.sort()")
                               thislist.sort()
                               print("Answer is : ",thislist)
                          elif choice_11 == 4:
                               print("Assuming List : thislist = [\"banana\", \"Orange\", \"Kiwi\", \"cherry\"]")
                               thislist = ["banana", "Orange", "Kiwi", "cherry"]
                               print("Performing Operation : thislist.reverse()")
                               thislist.reverse()
                               print("Answer Is : ",thislist)
                          elif choice_11 == 5:
                               break
                          else:
                              print("\nInvalid Choice\n")
               elif choice_5 == 8:
                    print("\n===================Copy Lists Operations=================\n")
                    print("Assuming List : thislist = [\"apple\", \"banana\", \"cherry\"]")
                    thislist = ["apple", "banana", "cherry"]
                    print("Performing Operation : mylist = thislist.copy()")
                    print("                       print(mylist)")
                    mylist = thislist.copy()
                    print("Answer Is : ",mylist)
               elif choice_5 == 9:
                    print("\n====================Join List Operations==================\n")
                    print("Assuming First List : list1 = [\"a\", \"b\", \"c\"]")
                    list1 = ["a", "b", "c"]
                    print("Assuming Second List : list2 = [1, 2, 3]")
                    list2 = [1, 2, 3]
                    print("Performing Operation : list3 = list1 + list2")
                    list3 = list1 + list2
                    print("Answer Is : ",list3)
               elif choice_5 == 10:
                    break
               else:
                   print("\nInvalid Choice\n")     
      elif choice_1 == 3:
           while True:
                 print("\n=======================Tuple Operations======================\n")
                 print("1. Access Tuples")
                 print("2. Update Tuples")
                 print("3. Unpack Tuples")
                 print("4. Loop Tuples")
                 print("5. Join Tuples")
                 print("6. Exit\n")
                 choice_12 = int(input("Enter Your Choice : "))
                 
                 if choice_12 == 1:
                    while True:
                          print("\n==================Access Tuple Operations================\n")
                          print("1. Access Tuple Items")
                          print("2. Negative Indexing")
                          print("3. Range of Indexes")
                          print("4. Range of Negative Indexes")
                          print("5. Check if Item Exists")
                          print("6. Exit\n")
                          choice_13 = int(input("Enter Your Choice : "))
                          
                          if choice_13 == 1:
                             print("Assuming Tuple : thistuple = (\"apple\", \"banana\", \"cherry\")")
                             thistuple = ("apple", "banana", "cherry")
                             print("Performing Operation : thistuple[1]")
                             print("Answer Is : ",thistuple[1])
                          elif choice_13 == 2:
                               print("Assuming Tuple : thistuple = (\"apple\", \"banana\", \"cherry\")")
                               thistuple = ("apple", "banana", "cherry")
                               print("Performing Operation : thistuple[-1]")
                               print("Answer is : ",thistuple[-1])
                          elif choice_13 == 3:
                               print("Assuming Tuples : thistuple = (\"apple\", \"banana\", \"cherry\", \"orange\", \"kiwi\", \"melon\", \"mango\")")
                               thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
                               print("Performing Operation : thistuple[2:5]")
                               print("Answer Is ",thistuple[2:5])
                          elif choice_13 == 4:
                               print("Assuming Tuple : thistuple = (\"apple\", \"banana\", \"cherry\", \"orange\", \"kiwi\", \"melon\", \"mango\")")
                               thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
                               print("Performing Operation : thistuple[-4:-1]")
                               print("Answer Is ",thistuple[-4:-1])
                          elif choice_13 == 5:
                               print("Assuming Tuple : thistuple = (\"apple\", \"banana\", \"cherry\")")
                               thistuple = ("apple", "banana", "cherry")
                               print("Performing Operation : if \"apple\" in thistuple:")
                               print("                           print(\"Yes, 'apple' is in the fruits tuple\")")
                               if "apple" in thistuple:
                                  print("Yes, 'apple' is in the fruits tuple")
                          elif choice_13 == 6:
                               break
                          else:
                              print("\nInvalid Choice\n")
                 elif choice_12 == 2:
                      while True:
                            print("\n====================Update Tuples Operations==================\n")
                            print("1. Add Items")
                            print("2. Remove Items")
                            print("3. Exit\n")
                            choice_14 = int(input("Enter Your Choice : "))
                            
                            if choice_14 == 1:
                               print("Once a tuple is created, you cannot add items to it.")
                               print("Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.")
                               print("Assuming Tuple : thistuple = (\"apple\", \"banana\", \"cherry\")")
                               thistuple = ("apple", "banana", "cherry")
                               print("Peforming Operation : y = list(thistuple)")
                               print("                      y.append(\"orange\")")
                               print("                      thistuple = tuple(y)")
                               y = list(thistuple)
                               y.append("orange")
                               thistuple = tuple(y)
                               print("Answer Is : ",thistuple)
                            elif choice_14 == 2:
                                 print("Assuming Tuple : thistuple = (\"apple\", \"banana\", \"cherry\")")
                                 thistuple = ("apple", "banana", "cherry")
                                 print("Performing Operation : y = list(thistuple)")
                                 print("                       y.remove(\"apple\")")
                                 print("                       thistuple = tuple(y)")
                                 y = list(thistuple)
                                 y.remove("apple")
                                 thistuple = tuple(y)
                                 print("Answer Is : ",thistuple)
                            elif choice_14 == 3:
                                 break
                            else:
                                print("\nInvalid Choice\n")
                 elif choice_12 == 3:
                      print("Assuming Tuple : fruits = (\"apple\", \"mango\", \"papaya\", \"pineapple\", \"cherry\")")
                      fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
                      print("Performing Operation : (green, *tropic, red) = fruits")
                      print("                       print(green)")
                      print("                       print(tropic)")
                      print("                       print(red)")
                      (green, *tropic, red) = fruits
                      print("Answer Is : ")
                      print(green)
                      print(tropic)
                      print(red)
                      print("\n")
                 elif choice_12 == 4:
                      while True:
                            print("\n======================Loop Tuples Operations======================\n")
                            print("1. Loop Through a Tuple")
                            print("2. Loop Through the Index Numbers")
                            print("3. Using a While Loop")
                            print("4. Exit\n")
                            choice_15 = int(input("Enter Your Choice : "))
                            
                            if choice_15 == 1:
                               print("Assuming Tuple : thistuple = (\"apple\", \"banana\", \"cherry\")")
                               thistuple = ("apple", "banana", "cherry")
                               print("Performing Operation : for x in thistuple:")
                               print("                           print(\"Answer Is : \",x)")
                               for x in thistuple:
                                   print("Answer Is : ",x)
                            elif choice_15 == 2:
                                 print("Assuming Tuple : thistuple = (\"apple\", \"banana\", \"cherry\")")
                                 thistuple = ("apple", "banana", "cherry")
                                 print("Performing Operation : for i in range(len(thistuple)):")
                                 print("                           print(\"Answer Is : \",thistuple[i])")
                                 for i in range(len(thistuple)):
                                     print("Answer Is : ",thistuple[i])
                            elif choice_15 == 3:
                                 print("Assuming Tuple : thistuple = (\"apple\", \"banana\", \"cherry\")")
                                 thistuple = ("apple", "banana", "cherry")
                                 print("Performing operation : i = 0")
                                 print("                       while i < len(thistuple):")
                                 print("                             print(\"Answer Is : \",thistuple[i])")
                                 print("                             i = i + 1")
                                 i = 0
                                 while i < len(thistuple):
                                       print("Answer Is : ",thistuple[i])
                                       i = i + 1
                            elif choice_15 == 4:
                                 break
                            else:
                                print("\nInvalid Choice\n")
                 elif choice_12 == 5:
                      print("Assuming Tuple one : tuple1 = (\"a\", \"b\" , \"c\")")
                      tuple1 = ("a", "b" , "c")
                      print("Assuming Tuple two : tuple2 = (1, 2, 3)")
                      tuple2 = (1, 2, 3)
                      print("Performing Operation : tuple3 = tuple1 + tuple2")
                      tuple3 = tuple1 + tuple2
                      print("Answer is : ",tuple3)
                 elif choice_12 == 6:
                      break
                 else:
                     print("\nInvalid Choice\n")
      elif choice_1 == 4:
           while True:
                 print("\n=====================Dictionaries Operations===================\n")
                 print("1. Access Items")
                 print("2. Change Items")
                 print("3. Add Items")
                 print("4. Remove Items")
                 print("5. Loop Dictionaries")
                 print("6. Copy Dictionaries")
                 print("7. Nested Dictionaries")
                 print("8. Exit\n")
                 choice_16 = int(input("Enter Your Choice : "))
                 
                 if choice_16 == 1:
                    while True:
                          print("\n===================Access Items Operations====================\n")
                          print("1. Accessing Items")
                          print("2. Get Keys")
                          print("3. Get Values")
                          print("4. Get Items")
                          print("5. Check if Key Exists")
                          print("6. Exit\n")
                          choice_17 = int(input("Enter Your Choice : "))
                          
                          if choice_17 == 1:
                             print("Assuming Dictionary : thisdict = {\"brand\": \"Ford\",\"model\": \"Mustang\",\"year\": 1964}")
                             thisdict =	{
                               "brand": "Ford",
                               "model": "Mustang",
                               "year": 1964
                             }
                             print("Performing Operation : x = thisdict.get(\"model\")")
                             x = thisdict.get("model")
                             print("Answer Is : ",x)
                          elif choice_17 == 2:
                               print("Assuming Dictionary : thisdict = {\"brand\": \"Ford\",\"model\": \"Mustang\",\"year\": 1964}")
                               thisdict =	{
                                 "brand": "Ford",
                                 "model": "Mustang",
                                 "year": 1964
                               }
                               print("Performing Operation : x = thisdict.keys() ")
                               x = thisdict.keys() 
                               print("Answer Is : ",x)
                          elif choice_17 == 3:
                               print("Assuming Dictionary : thisdict = {\"brand\": \"Ford\",\"model\": \"Mustang\",\"year\": 1964}")
                               thisdict =	{
                                 "brand": "Ford",
                                 "model": "Mustang",
                                 "year": 1964
                               }
                               print("Performing Operation : x = thisdict.values()")
                               x = thisdict.values()
                               print("Answer Is : ",x)
                          elif choice_17 == 4:
                               print("Assuming Dictionary : thisdict = {\"brand\": \"Ford\",\"model\": \"Mustang\",\"year\": 1964}")
                               thisdict =	{
                                 "brand": "Ford",
                                 "model": "Mustang",
                                 "year": 1964
                               }
                               print("Performing Operation : x = thisdict.items()")
                               x = thisdict.items()
                               print("Answer Is : ",x)
                          elif choice_17 == 5:
                               print("Assuming Dictionary : thisdict = {\"brand\": \"Ford\",\"model\": \"Mustang\",\"year\": 1964}")
                               thisdict =	{
                                 "brand": "Ford",
                                 "model": "Mustang",
                                 "year": 1964
                               }
                               print("Performing Operation : if \"model\" in thisdict:")
                               print("                           print(\"Yes, 'model' is one of the keys in the thisdict dictionary\")")
                               if "model" in thisdict:
                                  print("Yes, 'model' is one of the keys in the thisdict dictionary")
                          elif choice_17 == 6:
                               break
                          else:
                              print("\nInvalid Choice\n")
                 elif choice_16 == 2:
                      while True:
                            print("\n==================Change Items Operations=================\n")
                            print("1. Change Values")
                            print("2. Update Values")
                            print("3. Exit\n")
                            choice_18 = int(input("Enter Your Choice : "))
                            
                            if choice_18 == 1: 
                               print("Assuming Dictionary : thisdict = {\"brand\": \"Ford\",\"model\": \"Mustang\",\"year\": 1964}")
                               thisdict =	{
                                 "brand": "Ford",
                                 "model": "Mustang",
                                 "year": 1964
                               }
                               print("Peforming Operation : thisdict[\"year\"] = 2018")
                               thisdict["year"] = 2018
                               print("Answer Is : ",thisdict)
                            elif choice_18 == 2:
                                 print("Assuming Dictionary : thisdict = {\"brand\": \"Ford\",\"model\": \"Mustang\",\"year\": 1964}")
                                 thisdict =	{
                                   "brand": "Ford",
                                   "model": "Mustang",
                                   "year": 1964
                                 }
                                 print("Performing Operation : thisdict.update({\"year\": 2020})")
                                 thisdict.update({"year": 2020})
                                 print("Answer Is : ",thisdict)
                            elif choice_18 == 3:
                                 break
                            else:
                                print("\nInvalid Choice\n")
                 elif choice_16 == 3:
                      print("Assuming Dictionary : thisdict = {\"brand\": \"Ford\",\"model\": \"Mustang\",\"year\": 1964}")
                      thisdict ={
                        "brand": "Ford",
                        "model": "Mustang",
                        "year": 1964
                      }
                      print("Performing Operation : thisdict[\"color\"] = \"red\"")
                      print("                       print(thisdict)")
                      thisdict["color"] = "red"
                      print("Answer Is : ",thisdict)
                 elif choice_16 == 4:
                      print("Assuming Dictionary : thisdict = {\"brand\": \"Ford\",\"model\": \"Mustang\",\"year\": 1964}")
                      thisdict ={
                        "brand": "Ford",
                        "model": "Mustang",
                        "year": 1964
                      }
                      print("Performing Operation : del thisdict[\"model\"]")
                      print("                       print(thisdict)")
                      del thisdict["model"]
                      print("Answer Is : ",thisdict)
                 elif choice_16 == 5:
                      while True:
                            print("================Loop Dictoinaries Operations==================")
                            print("1. Print all Key names")
                            print("2. Print all Values")
                            print("3. Exit\n")
                            choice_19 = int(input("Enter Your Choice : "))
                            
                            if choice_19 == 1:
                               print("Assuming Dictionary : thisdict = {\"brand\": \"Ford\",\"model\": \"Mustang\",\"year\": 1964}")
                               thisdict ={
                                 "brand": "Ford",
                                 "model": "Mustang",
                                 "year": 1964
                               }
                               print("Performing Operation : for x in thisdict:")
                               print("                           print(\"Answer Is : \",x)")
                               for x in thisdict:
                                   print("Answer Is: ",x)
                            elif choice_19 == 2:
                                 print("Assuming Dictionary : thisdict = {\"brand\": \"Ford\",\"model\": \"Mustang\",\"year\": 1964}")
                                 thisdict ={
                                   "brand": "Ford",
                                   "model": "Mustang",
                                   "year": 1964
                                 }
                                 print("Performing Operation : for x in thisdict:")
                                 print("                           print(\"Answer Is : \"thisdict[x])")
                                 for x in thisdict:
                                     print("Answer Is : ",thisdict[x])
                            elif choice_19 == 3:
                                 break
                            else:
                                print("\nInvalid Choice\n")
                 elif choice_16 == 6:
                      print("Assuming Dictionary : thisdict = {\"brand\": \"Ford\",\"model\": \"Mustang\",\"year\": 1964}")
                      thisdict ={
                        "brand": "Ford",
                        "model": "Mustang",
                        "year": 1964
                      }
                      print("Performing Operation : mydict = thisdict.copy()")
                      print("                       print(\"Answer Is : \",mydict)")
                      mydict = thisdict.copy()
                      print("Answer Is : ",mydict)
                 elif choice_16 == 7:
                      print("This is a Nested Dictionarie :::\n")
                      print("myfamily = {\"child1\" : {\"name\" : \"Emil\",\"year\" : 2004},\"child2\" : {\"name\" : \"Tobias\"\"year\" : 2007}, \"child3\" : {\"name\" : \"Linus\",\"year\" : 2011}}")
                 elif choice_16 == 8:
                      break
                 else:
                     print("\nInvalid Choice\n")
      elif choice_1 == 5:
           print("\n𝖈𝖍𝖎𝖓𝖒𝖆𝖞29𝖍𝖚𝖇 : https://github.com/chinmay29hub/python-data-types")
           print("\nReference : https://www.w3schools.com/\n")
           break
      else:
          print("\nInvalid Choice\n")     
         
