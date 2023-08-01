
from ticket_service import TicketService
from purchase_exceptions import InvalidPurchaseException
from ticket_type_request import TicketTypeRequest
from seatbooking.seat_reservation_service import SeatReservationService
from paymentgateway.ticket_payment_service import TicketPaymentService


if __name__ == '__main__':

    my_tickets = [TicketTypeRequest("ADULT", 2),TicketTypeRequest("CHILD"),3]

    ticket_service = TicketService(account_id=1, t)
    ticket_type = TicketTypeRequest()
    ticket_type_requests = []

    #set series of inputs to determine customer requirements
    account_id = int(input("Please enter your account id:"))

    #check at least one adult is travelling
    valid = False
    while not valid:
        no_of_adults = int(input("Please enter number of adults travelling:")).get_tickets_number()
        if no_of_adults >= 1:
            valid = True
        else:
            print("There must be at least one adult travelling")
            continue
    
    
    #check number of dependents         
    no_of_children =int(input("Please enter number of children travelling:"))
    no_of_infants = int(input("Please enter number of infants travelling:"))

    #use this information to determine number of seats required

    no_of_seats = no_of_adults + no_of_children

    #use this information to determine number of tickets required

    no_of_tickets = no_of_adults + no_of_children + no_of_infants

    #use inputs to determine cost of tickets required

    cost = 20*no_of_adults + 10*no_of_children


    ticket_service.purchase_tickets(account_id,ticket_type_requests)
