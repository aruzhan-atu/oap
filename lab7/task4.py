positive = negative = zeros = even = odd = 0
for value in numbers:
     if value > 0:
         positive += 1
     elif value < 0:
         negative += 1
     else:
         zeros += 1
     if value % 2 == 0:
         even += 1
     else:
          odd += 1 