
import datetime

class Card:

    def __init__ ( Card, name, content ):

        Card.date_created = datetime.datetime.now()
        Card.name = name
        Card.content = content
        Card.date_updated_at = datetime.datetime.now()

    def set_date_updated_at ( Card ):
        Card.date_updated_at = datetime.datetime.now()


MY_CARD = Card( 'My new card', 'A cool card')
print( MY_CARD.date_updated_at )
