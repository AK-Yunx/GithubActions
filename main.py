import os

if __name__ == '__main__':
    with open('newFile.txt', 'w') as f:
        f.write("Hello")
        print(f.name)
    print("文件呢？")
    print(os.path.abspath(__file__))
