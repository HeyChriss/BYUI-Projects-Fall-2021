import math
Items = int(input('Enter the number of items: '))
Box = int(input('Enter the number of items per box: '))
Boxes = Items / Box
Total = math.ceil(Boxes)

print (f'For {Items} items, packing {Box} items in each box, you will need {Total} boxes.')
