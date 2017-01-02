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

def frogJmp(x, y, d):
	count = 0
	while True:
		count += 1
		x += d
		if x>=y: 
			return count

def frogJmpBis(x,y,d):
	acc = 0
	dist = y-x
	if dist%d:
		acc = 1
	acc += dist//d
	return acc

print (frogJmp(10, 85, 30))
print (frogJmp(10, 70, 30))
print (frogJmpBis(10, 85, 30))
print (frogJmpBis(10, 70, 30))

def tapeEquilibrium(A):
	left_add = A[0]
	
	right_add = 0
	for i in xrange(1,len(A)):
		right_add += A[i]
	
	print 'intial with', (left_add, right_add) 
	min_diff = abs(left_add - right_add)
	print 'so far we get:', min_diff

	for i in xrange(1,len(A)-1):
		left_add += A[i]
		right_add -= A[i]
		
		print 'trying with', (i, A[i], left_add, right_add)
		min_diff = min(min_diff, abs(left_add - right_add))
		print 'so far we get:', min_diff

	return min_diff

def tapeEquilibriumBis(A):
	addition = 0
	for i in xrange(len(A)):
		addition += -1*A[i]
	res = abs(addition)
	for i in xrange(len(A)-1):
		addition += 2*A[i]
		res = min (res, abs(addition))
	return res


print (tapeEquilibrium([3,1,2,4,3]))
print (tapeEquilibriumBis([3,1,2,4,3]))

def swapToEqualSum(m, A, B):
	def countElems(A):
		numberOfElems = [0]*m
		sum_res = 0
		for i in xrange(len(A)):
			numberOfElems[A[i]] += 1
			sum_res += A[i]
		return numberOfElems, sum_res
	numElemsA, sumA =  (countElems(A))
	numElemsB, sumB =  (countElems(B))

	numNonCommonElems = [0]*m
	for i in xrange(m):
		numNonCommonElems[i] = abs(numElemsA[i] - numElemsB[i])

	return (numElemsA, sumA, numElemsB, sumB, numNonCommonElems)

print swapToEqualSum(4, [1,2,3,0,0,2,3,0], [1,2,3,1,0,2,3,0])
print swapToEqualSum(4, [1,2,3,1,1,2,3,0], [1,2,3,0,0,2,3,0])






















