def reverseArray(A):
	n = len(A)
	def loop(A, n, l, r):
		if n>1:
			temp = A[l]
			A[l] = A[r]
			A[r] = temp
		if n>2:
			loop(A, n-2, l+1, r-1)
		return A
	loop(A, n, 0, n-1)
	return A

def reverseArrayLinear(A):
	n = len(A)
	for i in xrange(0, n//2):
		temp = A[i]
		A[i] = A[n-1-i]
		A[n-1-i] = temp
	return A


print (reverseArray([1,2,3,4,5,6,7,8,9]))
print (reverseArray([1,2,3]))
print (reverseArray([1,2]))
print (reverseArray([1]))

print (reverseArrayLinear([1,2,3,4,5,6,7,8,9]))
print (reverseArrayLinear([1,2,3]))
print (reverseArrayLinear([1,2]))
print (reverseArrayLinear([1]))

def cyclicRotation(A, s):
	for i in xrange(s):
		A.append(A.pop(0))
	return A

print (cyclicRotation([1,2,3,4,5,6,7,8,9], 3))
print (cyclicRotation([1,2,3,4,5,6,7,8,9], 5))
print (cyclicRotation([1,2,3,4,5,6,7,8,9], 1))
print (cyclicRotation([1,2,3,4,5,6,7,8,9], 0))

def oddOccurrencesInArray(A):
	acc = 0
	for i in xrange(len(A)):
		acc = acc^A[i]
	return acc

print oddOccurrencesInArray([9,3,9,3,9,7,9]) 
print oddOccurrencesInArray([9,3,9]) 
print oddOccurrencesInArray([9,3,9,3]) 

def perfMissingElem(A, n):
	acc = 0
	for i in xrange(1, n+2):
		acc = acc^i
	for i in xrange(n):
		acc = acc^A[i]

	return acc

print 'perfMissingElem'
print perfMissingElem([2,3,1,5],4)
print perfMissingElem([2,3,1,5,6],5)
print perfMissingElem([4,3,1,5],4)
print perfMissingElem([2,3,4,5],4)

def perfMissingElemBis(A, n):
	acc, expected = 0, (n+1)*(n+2)/2 # triangle area!
	for i in xrange(n):
		acc += A[i]
	return expected-acc 

print 'perfMissingElem'
print perfMissingElemBis([2,3,1,5],4)
print perfMissingElemBis([2,3,1,5,6],5)
print perfMissingElemBis([4,3,1,5],4)
print perfMissingElemBis([2,3,4,5],4)

def perfMissingElemBBis(A, n):


