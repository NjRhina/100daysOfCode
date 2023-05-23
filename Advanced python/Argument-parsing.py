import sys
import getopt

def myfunction(*args, **kwargs):
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])
    print(kwargs['KEYONE'])
    print(kwargs['KEYTWO'])

myfunction('hey', True, 19,'wow', KEYONE ="TEST", KEYTWO = 7 )

print(sys.argv[0])
print(sys.argv)

# usage: Argument-parsingss.py FILENAME
filename = sys.argv[1]
message = sys.argv[2]

with open(filename, 'w+') as f:
    f.write("my first message")


filename = "test1.txt"
message = "Hey kids, spelling is fun!"

opts, args = getopt.getopt(sys.argv[1:], "f:m:", ['filename','message'])
# print(opts)
# print(args)

for opt, arg in opts:
    if opt == '-f':
        filename = arg
    if opt == "-m":
        message = arg

with open(filename, 'w+') as f:
    f.write(message)



