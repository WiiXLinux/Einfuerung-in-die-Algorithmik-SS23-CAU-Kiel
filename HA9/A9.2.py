'''
A9.2 ADT for optinal values

laws:
1. nothing().is_filled() == False
2. filled(v).from_filled() == v
3. nothing().change_content(v).from_filled() == None
4. filled(x).change_content(v).from_filled() == v
5. filled(v).optional_map(f).from_filled() == f(v)
6. nothing().optional_map(f).is_filled() == False
'''

class Optional():
    '''
    A class that implements the concept of Optional Values
    as an ADT
    One instance of Optional() can either contain a value
    or contain no value, in which case its value is None
    The default constructor corresponds to a nothing()
    constructor, which generates an empty instance of Optional().
    '''
    def __init__(self):
        '''
        constructor that acts as the nothing() constructor
        generates an empty optional-value
        isfilled contains information about whether the OV contains
        a value or not
        value contains its value, if no value is contained in this OV
        value contains None
        '''
        #parameter used for checking if instance of
        #Optional() contains a value
        self.isfilled = False
        self.value = None
    
    def filled(v):
        '''
        constructor that generates a filled value by creating
        a new instance of Optional() and filling its values
        '''
        optional = Optional()
        optional.isfilled = True
        optional.value = v
        return optional
    
    def is_filled(ov):
        '''
        selector, that returns the isfilled value of an OV
        >>> o.is_filled() #for an empty OV
        False
        >>> o.is_filled() #for a non-empty OV
        True
        '''
        return ov.isfilled
    
    def from_filled(ov):
        '''
        selector that returns the value of an OV
        >>> o.from_filled() #for an empty OV
        None
        o.from_filled() #for a non-empty OV
        value
        '''
        return ov.value
    
    def change_content(ov,v):
        '''
        operation that returns a new value, if the OV
        was previously filled
        if OV was empty, it remains empty
        '''
        if ov.isfilled:
            return Optional.filled(v)
        else:
            return Optional()
    
    def optional_map(ov, f):
        '''
        operation that applies a function f to the value of
        OV, if the OV is not empty
        >>> ov.optional_map(lambda x : x + 31) #for an OV with value v
        v + 31
        generates a new OV, if the OV was empty
        '''
        if ov.is_filled():
            return Optional.filled(f(ov.value))
        else:
            return Optional()

#test cases from assignment
o = Optional()
print(o.is_filled())        # False
o = Optional.filled(42)
print(o.is_filled())        # True
print(o.from_filled())      # 42
o1 = o.change_content(73)
print(o.from_filled())      # 42
print(o1.from_filled())     # 73
o2 = o.optional_map(lambda x : x + 31)
print(o.from_filled())        # 42
print(o2.from_filled())       # 73

#testprogram

class OptionalTest:
    '''
    test class that checks if our implementation of Optional()
    corresponds with the laws of OV ADT
    '''
    @staticmethod
    def test_laws():
        # 1. nothing().is_filled() == False
        assert Optional().is_filled() == False

        # 2. filled(v).from_filled() == v
        assert Optional.filled(42).from_filled() == 42

        # 3. nothing().change_content(v).from_filled() == None
        assert Optional().change_content(42).from_filled() == None

        # 4. filled(x).change_content(v).from_filled() == v
        assert Optional.filled(10).change_content(42).from_filled() == 42

        # 5. filled(v).optional_map(f).from_filled() == f(v)
        assert Optional.filled(42).optional_map(lambda x : x + 31).from_filled() == 73

        # 6. nothing().optional_map(f).is_filled() == False
        assert Optional().optional_map(lambda x : x + 31).is_filled() == False

OptionalTest.test_laws()
