
from purchase_exceptions import InvalidPurchaseException
from ticket_type_request import TicketTypeRequest
from seatbooking.seat_reservation_service import SeatReservationService
from paymentgateway.ticket_payment_service import TicketPaymentService


class TicketService:

    """

      purchase_tickets should be the only public method

    """

    def purchase_tickets(account_id=None, ticket_type_requests=[]):

        #set series of inputs to determine customer requirements
        account_id = int(input("Please enter your account id:"))

        #check at least one adult is travelling, wrapped inside TicketTypeRequest to take advantage of its error checking
        valid = False
        while not valid:
            no_of_adults = TicketTypeRequest("ADULT",int(input("Please enter number of adults travelling:"))).get_tickets_number()
            if no_of_adults >= 1:
              valid = True
            else:
                print("There must be at least one adult travelling")
                continue
            
        #check number of dependents, wrapped inside TicketTypeRequest to take advantage of its error checking          
        no_of_children = TicketTypeRequest("CHILD",int(input("Please enter number of children travelling:"))).get_tickets_number()
        no_of_infants = TicketTypeRequest("INFANT",int(input("Please enter number of infants travelling:"))).get_tickets_number()

        #use this information to determine number of seats required

        no_of_seats = no_of_adults + no_of_children

        #use this information to determine number of tickets required

        no_of_tickets = no_of_adults + no_of_children + no_of_infants

        #use inputs to determine cost of tickets required

        cost = 20*no_of_adults + 10*no_of_children

        SeatReservationService.reserve_seat(SeatReservationService,account_id, no_of_seats)
        TicketPaymentService.make_payment(TicketPaymentService,account_id, cost)


        
    
