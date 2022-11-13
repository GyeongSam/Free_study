
input()
print('go!')
for i in range(1234567,12345678):
    for j in range(7654321,76543210):
        if (((i%1000000007)*(j%1000000007))%1000000007!=(i*j)%1000000007):
            print('발견!!!',i,j)
            break
    else:continue
else: print('end')

