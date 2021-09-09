from LinkedList import Linked_List as L

MY_LISTS = [
    [ 1, 2, 3 ],
    [ 'a', 'b', 'c' ],
]

def create_linked_list ( current_list ):
    
    new_list = L.Linked_List()

    print ( 'current list', new_list.get_list() )
    for item in current_list:

        if ( type(item) is list ):
            new_list.append( create_linked_list(item) )
        else:
            new_list.append( item )

    return new_list

MY_LINKED_LISTS = create_linked_list ( MY_LISTS )

print ( '\t' )
print ( MY_LINKED_LISTS )
print ( '\t' )