
from ticket_service import TicketService
from purchase_exceptions import InvalidPurchaseException
from ticket_type_request import TicketTypeRequest
from seatbooking.seat_reservation_service import SeatReservationService
from paymentgateway.ticket_payment_service import TicketPaymentService


if __name__ == '__main__':

    #instantiate TicketService and list of tickets
    ticket_service = TicketService()
    my_tickets = [TicketTypeRequest("ADULT", 2),TicketTypeRequest("CHILD",3),TicketTypeRequest("ADULT", 2)]
    ticket_service.purchase_tickets(account_id = 1,ticket_type_requests=my_tickets)
