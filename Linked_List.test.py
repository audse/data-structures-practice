
class Node:

    next = None

    def __init__ ( Node, data ):
        Node.data = data

    def set_next ( Node, data ):
        Node.next = data

class Linked_List:

    head = None

    # Returns a non-linked list of all the items in the linked list
    def get_list ( Linked_List ):
        
        if ( Linked_List.head == None ):
            return []

        current = Linked_List.head
        new_list = [ current.data ]

        while ( current.next != None ):
            new_list.append( current.next.data )
            current = current.next

        return new_list

    def append ( Linked_List, data ):

        # If the linked list has no head,
        # create it
        if ( Linked_List.head == None ):
            Linked_List.head = Node(data)
            return

        # Cycle through the linked list to find
        # the final item
        current = Linked_List.head
        while ( current.next != None ):
            current = current.next
        
        # Add the data as the final item's next value
        current.set_next( Node(data) )
        return
    
    def delete_value ( Linked_List, data ):

        # If the linked list has no head,
        # we don't need to cycle through it
        if ( Linked_List.head == None ):
            return
        
        # Cycle through all items to find
        # the FIRST value that matches the param data
        current = Linked_List.head
        while ( current.next != None ):

            # If the next value is the data we want to delete,
            # change it to the value after that
            if ( current.next.data == data ):
                current.set_next( current.next.next )
                return
            
            current = current.next

my_list = Linked_List()
my_list.append( 0 )
my_list.append( 1 )
my_list.append( 2 )
my_list.delete_value( 1 )

print ( '\t' )
print( my_list.get_list() )
print ( '\t' )