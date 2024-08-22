import time
print('O mundo vai acabar em...')
for c in range(5,0,-1):
    print(f'{c};')
    time.sleep(1)
    if (c == 1):
        print('O mundo acabou! :)')