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
        self.ticket_payment_service = TicketPaymentService()
        
    def __check_adult_ticket(self,number_of_tickets):
        if number_of_tickets == 0:
            raise InvalidPurchaseException("No adults present")

    def __check_max_tickets(self,number_of_tickets):
        if number_of_tickets >= 20:
            raise InvalidPurchaseException("Maximum number of tickets exceeded")

    def __check_unaccompanied_infant(self,number_of_adults,number_of_infants):
        if number_of_infants > number_of_adults:
            raise InvalidPurchaseException("Too many infants for the number of adults selected")

    def __check_account_id_pos(self, account_id):
        if account_id <=0:
            raise InvalidPurchaseException("Account ID needs to be positive")
    
    def __check_account_id_int(self, account_id):
        if type(account_id) != int:
            raise InvalidPurchaseException("Account ID needs to be an integer")

    def purchase_tickets(self, account_id=None, ticket_type_requests=[]):

        #loop through my tickets and get data
      no_of_adults = 0
      no_of_children = 0
      no_of_infants = 0

      for ticket_request in ticket_type_requests:
          if ticket_request.get_ticket_type() == "ADULT":
              no_of_adults = no_of_adults + ticket_request.get_tickets_number()
          elif ticket_request.get_ticket_type() == "CHILD":
              no_of_children = no_of_children + ticket_request.get_tickets_number()
          elif ticket_request.get_ticket_type() == "INFANT":
              no_of_infants = no_of_infants + ticket_request.get_tickets_number()
        
      #use this information to determine number of seats required

      no_of_seats = no_of_adults + no_of_children

      #use this information to determine number of tickets required

      no_of_tickets = no_of_adults + no_of_children + no_of_infants

      #perform checks on constraints

      self.__check_adult_ticket(no_of_adults)
      self.__check_max_tickets(no_of_tickets)
      self.__check_unaccompanied_infant(no_of_adults, no_of_infants)
      self.__check_account_id_int(account_id)
      self.__check_account_id_pos(account_id)
      
      #use inputs to determine cost of tickets required

      cost = 20*no_of_adults + 10*no_of_children

      self.seat_reservation_service.reserve_seat(account_id, no_of_seats)
      self.ticket_payment_service.make_payment(account_id, cost)
            
        

       


        
    
