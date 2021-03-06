from test.test_MimeWriter import OUTPUT
__author__ = 'mdarmadi@ucsd.edu, A11410141, hdharmaw@ucsd.edu, A91413023, vcchandr@ucsd.edu, A12496582'
import sys
from Queue  import LifoQueue
import time
closedList = {} # closedList is going to be a dictionary showing the parent of number

def isPrime(n):
    if n == 0 or n == 1:
         return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

def getPossibleActions(currentPrime):
    listOfPrimes = []

    currentStr = str(currentPrime)
    currentList = list(currentStr)
    length = len(currentList)   # this is the digit of the number

    # check every possible combination
    for i in range(0, length):
        curChar = currentList[i]
        for j in range(0,10): # possible digit replacement
            j = str(j)

            if(j == curChar): # to avoid repetition
                continue

            if (j == '0' and i == 0):    # to avoid producing leading 0
                continue

            currentList[i] = j          # replace the digit
            newStr = ''.join(currentList)
            newInt = int(newStr)            # might not need to convert to int if dictionary uses str for key

            # check if new integer is prime and not in closedList already
            if (isPrime(newInt)):
                if (not str(newInt) in closedList):
                    listOfPrimes.append(newInt)

            currentList[i] = curChar # return currentList to original char

    return listOfPrimes

def getPath(startingPrime, finalPrime):
    # print(type(startingPrime))
    # print("starting Prime: " + str(startingPrime))
    # print(type(finalPrime))
    # print("final Prime: " + str(finalPrime))

	# your code here
	#depth limit is 5	
	#declare stack
    closedList.clear()
    stack = LifoQueue()
	
	#push <startingPrime (currentPrime), 0 (depth)> into the stack
    stack.put((startingPrime , 0))

    outputString = ""
	
	#while stack is not empty 
    while(not stack.empty()):
		#pop a from stack
        a = stack.get()

		#if a.currentPrime == finalPrime
        if(a[0] == finalPrime):
            break

		#else if a.depth >= 5
        elif(a[1] >= 5):
            continue
		
		#find all neighbor of currentPrime
        neighbor = getPossibleActions(a[0])
		
        for i in range(0,len(neighbor)):
			#set the parent of the neighbor to currentPrime
            closedList[str(neighbor[i])] = a[0]
			#push all neighbor as <neighbor,a.depth + 1> into the stack
            stack.put((neighbor[i],a[1] + 1))
	
    #if(currentPRime != finalPrime)
    if(a[0] != finalPrime):
        #unsolvable
        outputString = 'UNSOLVABLE'

    else:
        current = a[0]
        outputString = ""
        outputString = str(current) + " " + outputString
        while(current != startingPrime):
            current = closedList[str(current)]
            outputString = str(current) + " " + outputString
# 		outputString = startingPrime + " " + outputString

#     file = open('output.txt','w')
#     print >> file,outputString
#     file.close()
    sys.stdout.write(outputString + "\n")
    return 

def main():
    for line in sys.stdin.readlines():
    #line = sys.stdin.readline()
        primes = str(line).split()
        first = list(primes[0])
        second = list(primes[1])

        t0 = time.time()
        getPath(int(primes[0]), int(primes[1]))

        t1 = time.time()
        #print t1 - t0
if __name__ == '__main__':
	main()