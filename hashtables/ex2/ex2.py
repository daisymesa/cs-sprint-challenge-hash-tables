#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # making empty dict for itinerary
    itinerary = {}
    # creating empty result variable to store output
    route = []

    # loop through each ticket to add to dict
    for ticket in tickets:
        # dict will have key + values as "source" : destination
        itinerary[ticket.source] = ticket.destination

    # initialize w/destination of 'NONE'
    curr_destination = itinerary['NONE']
    print(curr_destination)

    # if dest is not NONE, append curr_dest to final itinerary
    while curr_destination is not 'NONE':
        route.append(curr_destination)
        # after updating route, reassign curr_dest
        curr_destination = itinerary[curr_destination]
    route.append('NONE')

    print(itinerary)

    return route


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

print(reconstruct_trip(tickets, 3))  # PDX, DCA
