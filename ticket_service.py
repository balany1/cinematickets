
from purchase_exceptions import InvalidPurchaseException
from ticket_type_request import TicketTypeRequest
from seatbooking.seat_reservation_service import SeatReservationService
from paymentgateway.ticket_payment_service import TicketPaymentService


class TicketService:

    """

      purchase_tickets should be the only public method

    """

    def __init__(self) -> None:
        self.seat_reservation_service = SeatReservationService()
        self.ticket_type_request = TicketTypeRequest()
        self.ticket_payment_service = TicketPaymentService()
        
        

    def purchase_tickets(account_id=None, ticket_type_requests=[]):

        
        #raise InvalidPurchaseException
    
        #self.seat_reservation_service.reserve_seat(account_id, no_of_seats)
        #self.ticket_payment_service.make_payment(account_id, cost)
            
        

       


        
    
