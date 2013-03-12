#!/usr/bin/env python

from binary_operator_tests_v4 import SingleSide


'''
Tests all the binary operators in the system.
'''

def run_test():
    # for single side tests, these values do not really matter.
    host_uuid = 10
    conn_obj = None
    single_side = SingleSide(host_uuid,conn_obj)


    if not test_comparisons(single_side):
        return False

    if not test_math(single_side):
        return False

    if not test_other_plusses(single_side):
        return False

    if not test_in(single_side):
        return False
    
    return True


def test_in(single_side):
    init_map = {
        1: 2,
        3: 4
        }
    if not single_side.in_map(init_map,1):
        print '\nErr on in '
        return False

    if single_side.in_map(init_map,4):
        print '\nErr on in '
        return False

    
    return True
 
def test_other_plusses(single_side):

    if single_side.plus_text('a','b') != 'ab':
        print '\nErr on plus text'
        return False

    # disallowed by type system
    # if single_side.plus_list([1],[2]) != [1,2]:
    #     print '\nErr on plus list'
    #     return False

    return True
    

def test_math(single_side):

    # +
    if single_side.plus_num(3,5.5) != 8.5:
        print '\nErr on plus num'
        return False

    # -
    if single_side.minus(3,5.5) != - 2.5:
        print '\nErr on minus'
        return False

    # *
    if single_side.mult(3,2.5) != 7.5:
        print '\nErr on mul'
        return False

    # /
    if single_side.div(6,3) != 2:
        print '\nErr on div'
        return False

    return True
    

def test_comparisons(single_side):
    '''
    @returns {bool} --- True if all comparsions produced correct result.  False
    if error.
    '''

    # <
    if not single_side.less_than(1,3):
        print '\nErr with less than'
        return False

    if single_side.less_than(3,3):
        print '\nErr with less than'
        return False

    if single_side.less_than(5,3):
        print '\nErr with less than'
        return False

    # <=
    if not single_side.less_than_eq(1,3):
        print '\nErr with less than eq'
        return False

    if not single_side.less_than_eq(3,3):
        print '\nErr with less than eq'
        return False

    if single_side.less_than_eq(5,3):
        print '\nErr with less than eq'
        return False


    # >
    if not single_side.greater_than(5,3):
        print '\nErr with greater than'
        return False

    if single_side.greater_than(3,3):
        print '\nErr with greater than'
        return False

    if single_side.greater_than(1,3):
        print '\nErr with greater than'
        return False

    # >=
    if not single_side.greater_than_eq(5,3):
        print '\nErr with greater than eq'
        return False

    if not single_side.greater_than_eq(3,3):
        print '\nErr with greater than eq'
        return False

    if single_side.greater_than_eq(1,3):
        print '\nErr with greater than eq'
        return False


    # !=
    if not single_side.not_equal('a','b'):
        print '\nErr with !='
        return False

    if single_side.not_equal('a','a'):
        print '\nErr with !='
        return False


    # ==
    if not single_side.equal('a','a'):
        print '\nErr with =='
        return False

    if single_side.equal('a','b'):
        print '\nErr with =='
        return False


    # or
    if not single_side.or_(False,True):
        print '\nErr with or'
        return False

    if not single_side.or_(True,True):
        print '\nErr with or'
        return False

    if single_side.or_(False,False):
        print '\nErr with or'
        return False

    # and
    if not single_side.and_(True,True):
        print '\nErr with and'
        return False

    if single_side.and_(True,False):
        print '\nErr with and'
        return False

    if single_side.and_(False,False):
        print '\nErr with and'
        return False
    
    
    return True




if __name__ == '__main__':
    run_test()
