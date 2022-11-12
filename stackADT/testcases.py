from stackADT import Stack

##
## TEST CASE 1
##
def test_1():
    s = Stack()
    s.push("Apple")
    s.push("Widows")
    try: 
        assert s.stack == ['Apple', 'Widows']
        return"PASS"
    except:
        return "FAILED"

##
## TEST CASE 2
##
def test_2():
    global s1
    s1 = Stack()
    s1.push(1)
    s1.push(2)
    s1.push(3)
    s1.push(4)

    try:
        assert s1.binarySearch(2) == True
        #assert s1.binarySearch(5) == False
        return "PASS"
        
    except:
        return "Failed"


##
## TEST CASE 3
##
def test_3():
    s1.remove(2)
    try:
        assert s1.binarySearch(2) == False
        return "PASS"
        
    except:
        return "FAILED"


if __name__ == "__main__":
    print(test_1(),"\n",test_2(),"\n",test_3())