"""
create a class that given a list of text files will at each iteration return
the first line of the text only if the file is not suppose to be ignored (see example files below)

example:

lets assume we have the following files and that the first line of each file is the name of the file

files = ["file1.txt", "file2.txt", "ingore_this_file1.txt", "file3.txt", "ingore_this_file1.txt", "file4.txt"]


following code should run:

>> my_generator =  DataGenerator(files)
>> for data in my_generator:
..      print(data)
..      if "3" in data:
..          break
>>"file1.txt"
>>"file2.txt"
>>"file3.txt"
>> next(my_generator)
>>"file4.txt"

"""

class DataGenerator():
    def __init__(self,files):
        self.data = files
        self.current_num = 0

    def __iter__(self):
        return self

    def __next__(self):
        for item in self.data:
            if 'ingore' in item:
                self.data.remove(item)
        if self.current_num < len(self.data):
            ret = self.data[self.current_num]
            self.current_num += 1
            return ret

files = ["file1.txt", "file2.txt", "ingore_this_file1.txt", "file3.txt", "ingore_this_file1.txt", "file4.txt"]

my_generator =  DataGenerator(files)
for data in my_generator:
    print(data)
    if "3" in data:
        break
print('================')
print(next(my_generator))
