
#cheking for prime without using modulus operator
def chekPrime(number):
    var=2
    f=0

    while(var <= number/2):
        if ((number/var)*var == number):
            f=1
            break;
        var+=1
    
    if(f==1):
        print "it is not prime"
    else:
        print "it is a prime number"

    
input = int(raw_input("Enter the number\t"))
chekPrime(input)
    
