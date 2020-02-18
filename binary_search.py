def BinarySearch(numberList, targetValue):
	startIndex = 0
	endIndex = len(numberList)
	
	while endIndex > startIndex:
		intervalLength = endIndex - startIndex
		midIndex = startIndex + (intervalLength // 2)
		
		if numberList[midIndex] == targetValue:
			return midIndex
		else:
			if numberList[midIndex] > targetValue:
				endIndex = midIndex
			else:
				startIndex = midIndex + 1

	return -1


List1 = [3, 6, 12, 14, 25, 37, 59, 123, 280, 950]
position = BinarySearch(List1, 6)

if position != -1:
	print("6 is in position", position)
else:
	print("6 is not in the list")

List2 = [1, 15, 29, 44, 91, 197, 657, 1260, 12873, 12884]
position = BinarySearch(List2, 109)

if position != -1:
	print("109 is in position", position)
else:
	print("109 is not in the list")
