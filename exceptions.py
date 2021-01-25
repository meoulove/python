

"""
fill in the fucntions so that the catch the appropriate errors and return "caught".

example:
>> test_list = []
>> catch_all_exceptions(test_list[10])
>> "caught"

"""

def catch_all_exceptions(object):
    catch_index_error(object)
    catch_value_error(object)

def catch_index_error(object):
    try:
        print(object[10])
    except IndexError:
        print('caught')

def catch_value_error(object):
    try:
        object = str(object)
        print(int(object))
    except ValueError:
        print('caught')


test_list = []
catch_all_exceptions(test_list)

