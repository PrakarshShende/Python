'file handling'

'creating a file'
# file = open("exp5.txt",'x')
# file.close()


'with open'
# with open("exp5.txt",'r') as file:
#     data = file.read()
#     print(data)
#     file.close()

'write'
# file = open("exp5.txt",'w')
# file.write("Helllooo! Python")
# file.close()

'writelines'
# file = open("exp5.txt", "w")
# lines = ["Hello\n", "Python\n", "CSE\n"]
# file.writelines(lines)
# file.close()

'Read file'
# file = open("exp5.txt",'r')
# data = file.read()
# print(data)
# file.close()

'Read n charatcers'
# file = open("exp5.txt", "r")
# data = file.read(5)
# print(data)
# file.close()

'Readline'
# file = open("exp5.txt", "r")
# line = file.readline()
# print(line)
# file.close()

'Readlines'
# file = open("exp5.txt", "r")
# lines = file.readlines()
# print(lines)
# file.close()

'Seek'
# file = open("exp5.txt",'r')
# file.seek(3)
# print(file.read())
# file.close()

'tell'
# file = open("exp5.txt",'r')
# print(file.tell())
# file.read(5)
# print(file.tell())
# file.close()

'append'
# file = open("exp5.txt",'a')
# file.write("\n Hello programmers")
# file.close()

'append + read'
# file = open("exp5.txt",'+a')
# file.write("\nNew content")
# file.seek(0)
# print(file.read())
# file.close()

'read and write'
# file = open("exp5.txt",'r+')
# print(file.read())
# file.seek(0)
# file.write("Helllo coders")
# file.close()

'write and read'
# file = open("exp5.txt",'w+')
# file.write("Hello this is written using w+ mode")
# file.seek(0)
# print(file.read())
# file.close()

'append binary'
# f = open("exp5.bin", "ab")
# f.write(b"Hello")
# f.close()

'read binary'
# f = open("scene.jpeg", "rb")
# print(f.read())
# f.close()

'write binary'
# f = open("scene.jpeg", "wb")
# f.write(b"Hello world")
# f.close()

'read + write binary rb+'
# f = open("exp5.bin", "rb+")
# print(f.read())
# f.seek(0)
# f.write(b"Hello programmmers")
# f.close()

'read + write binary wb+'
# f = open("exp5.bin", "wb+")
# print(f.read())
# f.seek(0)
# f.write(b"Hello progammers and coders")
# print(f.read())
# f.close()

'read + append binary'
# f = open("exp5.bin", 'ab+')
# print(f.read())
# f.seek(0)
# f.write(b"\nHello progammers and coders")
# print(f.read())
# f.close()

'delete'
# import os
# file = open("exp6.txt",'x')
# os.remove("exp6.txt")

'unlink'
import os
# file = open("exp6.txt",'x')
# os.unlink("exp6.txt")


# ====================================================================================

'''Directory'''

'os.getcwd() — Get Current Directory'
# import os
# print(os.getcwd())


'os.chdir() — Change Directory'
# import os
# os.chdir("C:\\Users\\Prakarsh\\Desktop")
# print(os.getcwd())


'os.listdir() — List Directory'
# import os
# print(os.listdir())


'os.mkdir() — Make Directory'
# import os
# os.mkdir("Test")

'os.makedirs() — Make Multiple Directories'
# import os
# os.makedirs("College/Python/Programs")

'os.rmdir() — Remove Directory'
# import os
# os.rmdir("Test")

