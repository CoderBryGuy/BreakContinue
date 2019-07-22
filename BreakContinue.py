_author_ = 'dev'

# Modify this loop to stop when i is exactly divisible by 11
# for i in range(0, 100, 7):
#     print(i)
#     if i != 0 and i % 11 ==0:
#         break
#

for i in range(1,20):
    if i % 3 == 0 or i % 5 == 0:
        continue
    else:
        print(i)


