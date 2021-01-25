def list_comp1(input_data):
    """
    make this into a list comprehension

    example:
    >> list_comp1([1,0,90,40])
    >> [0,0,1,1]
    """

    transformed_data = []
    transformed_data = [0 if i < 10 else 1 for i in [i for i in input_data if i >= 0]]
    return transformed_data

transformed_data = list_comp1([1,0,90,40])
print(transformed_data)