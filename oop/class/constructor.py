class Constructor_example:
    def __init__(self):
        # self.variable_name is a instance variable. Can be called via any object 
        # self is not a keyword, can be used any variable
        self.value_of_pi = "3.142" # instance variable instead of value_of_pi = "3.142" # Local variable

obj = Constructor_example()
print(obj.value_of_pi)

        