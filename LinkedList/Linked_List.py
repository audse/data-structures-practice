
class Node:

    next = None

    def __init__ ( self, data ):
        Node.data = data

    def set_next ( self, data ):
        Node.next = data

class Linked_List:

    head = None

    # Returns a non-linked list of all the items in the linked list
    def get_list ( self ):
        
        if ( self.head == None ):
            return []

        current = self.head
        new_list = [ current.data ]

        while ( current.next != None ):
            new_list.append( current.next.data )
            current = current.next

        return new_list

    def append ( self, data ):

        # If the linked list has no head,
        # create it
        if ( self.head == None ):
            self.head = Node(data)
            return

        # Cycle through the linked list to find
        # the final item
        current = self.head
        while ( current.next != None ):
            current = current.next
        
        # Add the data as the final item's next value
        current.set_next( Node(data) )
        return
    
    def delete_value ( self, data ):

        # If the linked list has no head,
        # we don't need to cycle through it
        if ( self.head == None ):
            return
        
        # Cycle through all items to find
        # the FIRST value that matches the param data
        current = self.head
        while ( current.next != None ):

            # If the next value is the data we want to delete,
            # change it to the value after that
            if ( current.next.data == data ):
                current.set_next( current.next.next )
                return
            
            current = current.next