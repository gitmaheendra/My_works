
def get_input():
    input =int(raw_input("Enter the limit"))
    return input

def fizz_bizz(n):
    for i in range(1,n):
        if (i%15==0):
            print "fizzbizz"
        elif(i%5==0):
            print "bizz"
        elif(i%3==0):
            print "fizz"
        else:
            print i


token = get_input()
fizz_bizz(token)


    
