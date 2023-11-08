import time
import sys

name = input(str('What Is Your First Name? '))
lastname = input(str('Last Name? '))
age = input(str('Age? '))
list = [{name}, {lastname}, {int(age)}]


#print('Cheking Your Datas ...')
#time.sleep(1)

#print('Connecting To Database ...')
#time.sleep(1)

#print('Hacking You ...')
#time.sleep(2)


def test():
    animation = [".","..","...","....",".....",":....","::...",":::..","::::.",":::::"]

    for i in range(5):
        for i in range(len(animation)):
            time.sleep(0.1)
            str = animation[i]
            sys.stdout.write("\r" + str)
            sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write("\r" + "     ")
        sys.stdout.flush()

test()

#print('XD')
print(f'\n<!> YOU BEEN HACKED <!> \n   > Name: {list[0]}, \n   > Last Name: {list[1]}, \n   > Age: {list[2]}')
