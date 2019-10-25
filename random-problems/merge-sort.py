array = [1,5,2,7,5,4,2,1]

def mergesort(array):
  if len(array) > 1:

    middle = len(array)//2

    leftArray = array[:middle]
    rightArray = array[middle:]

    mergesort(leftArray)
    mergesort(rightArray)

    mergeHalves(array, leftArray, rightArray)




def mergeHalves(array, leftArray, rightArray):

  combinedIndex = 0
  leftArrayIndex = 0
  rightArrayIndex = 0


  while (leftArrayIndex < len(leftArray) and rightArrayIndex < len(rightArray)):
      if (leftArray[leftArrayIndex] < rightArray[rightArrayIndex]):
        array[combinedIndex] = leftArray[leftArrayIndex]
        leftArrayIndex += 1
      else:
        array[combinedIndex] = rightArray[rightArrayIndex]
        rightArrayIndex += 1

      combinedIndex += 1

  while leftArrayIndex < len(leftArray):
    array[combinedIndex] = leftArray[leftArrayIndex]
    leftArrayIndex += 1
    combinedIndex += 1

  while rightArrayIndex < len(rightArray):
    array[combinedIndex] = rightArray[rightArrayIndex]
    rightArrayIndex += 1
    combinedIndex += 1
