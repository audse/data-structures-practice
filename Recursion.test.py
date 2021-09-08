from LinkedList import Linked_List

MY_LISTS = [
    [ 1, 2, 3 ],
    [ 'a', 'b', 'c' ],
]

MY_LINKED_LISTS = []

def create_linked_list ( current_list ):

    linked_list = Linked_List.Linked_List()

    for item in current_list:

        if ( type(item) is list ):
            linked_list.append( create_linked_list(item) )
        else:
            linked_list.append( item )
    
    return linked_list

for each_list in MY_LISTS:
    MY_LINKED_LISTS.append( create_linked_list( MY_LISTS ) )

print ( '\t' )
print ( MY_LINKED_LISTS )
print ( '\t' )