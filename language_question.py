import copy

increment_by_i=[lambda x: x+i for i in range(10)]


def create_increment_function(x):
    return lambda y: y+x

increment_by_i_v2=[create_increment_function(i) for i in range(10)]




if __name__ == "__main__":
    a=increment_by_i[3](4)
    a_prim=increment_by_i_v2[5](8)

    l_empty=[]
    for i in range(10):
        temp=increment_by_i_v2[5](i) #nie widze sensu za bardzo tego
        l_empty.append(temp)

    ################################----#copy vs deepcopy----######################################################
    l_a=[3,5,7,8]
    l_b=l_a
    l_b.append(7)
    print(l_a)

    l_c=[3,5,7,8]
    l_d=copy.deepcopy(l_c)
    l_d.append(9)
    print(l_d)
    print(l_c)

    ################################----#copy vs deepcopy----######################################################



    print('end')
