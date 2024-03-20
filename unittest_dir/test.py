newList = []
def generator(k):
    if k > 0:
      result = generator(k - 1) + k
      newList.append(result)
    else:
      result = 0
    return result

generator(5)
[print(x) for x in list(reversed(newList))]
