
"""

implemet a child-class of dict called RangeDict that takes pairs of ints; (int, int) which
signifies a range. eg. (1,10), (30,34).
Given an int will return the value of the range the int is inside

so if out dict contain the keys (1,10), (30,34), and we run:

>> my_range_dict[7]
>> (1,10)

furthermore;

when you try to add a range that overlaps with an existing range, for example
trying to add (5,11) when we have (1,10), overwrite the overlapping span.

>> my_range_dict
>> {(1,10):1, (30,34): 2}
>> my_range_dict[(5,11)] = 3
>> my_range_dict
>> {(30,34): 2, (5,11):3}

"""

class RangeDict():
    ranges = [(1,10),(30,34)]
    keys = [1, 2]
    dict = {}
    for i in range(len(ranges)):
        dict[ranges[i]] = keys[i]

class My_range_dict(RangeDict):

    def __getitem__(self, key):
        self.key = key
        for eachRange in self.ranges:
            if self.key in range(eachRange[0],eachRange[1]+1):
                print(eachRange)

    def __setitem__(self, key, value):
        new_range = set(range(key[0],key[1]+1))
        for each_range in self.ranges:
            old_range = set(range(each_range[0],each_range[1]+1))
            if new_range.intersection(old_range):
                del self.dict[each_range]
                self.dict[key] = value
                return self.dict
            else:
                self.dict[key] = value
                return self.dict

    def __call__(self):
        print(self.dict)

my_range_dict = My_range_dict()
my_range_dict()
my_range_dict[7]
my_range_dict[(20,24)] = 3
my_range_dict()
