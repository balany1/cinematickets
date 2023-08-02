import builtins
import unittest
from unittest.mock import patch
from ticket_service import TicketService
from ticket_type_request import TicketTypeRequest
from purchase_exceptions import InvalidPurchaseException

class Test_ticket_service(unittest.TestCase):

    def setUp(self) -> None:
        self.ticket_service = TicketService()
        self.my_tickets = [TicketTypeRequest("ADULT", 2),TicketTypeRequest("CHILD",3)]
        
    def test_no_account_id(self):
        #tests that there is an account_id
        with self.assertRaises(InvalidPurchaseException):
            self.ticket_service.purchase_tickets(account_id=None)
        
    def test_negzero_account_id(self):
        my_tickets = [TicketTypeRequest("ADULT", 3),TicketTypeRequest("CHILD",5)]
        with self.assertRaises(InvalidPurchaseException):
            self.ticket_service.purchase_tickets(account_id=-2, ticket_type_requests=my_tickets)

    def test_tickets_requested_null(self):
        #tests that there has been a ticket requested
        my_tickets = []
        with self.assertRaises(InvalidPurchaseException):
            self.ticket_service.purchase_tickets(account_id=3, ticket_type_requests=my_tickets)

    def test_tickets_requested_notnull(self):
        #tests that there has been a ticket requested
        my_tickets = [TicketTypeRequest("ADULT", 0),TicketTypeRequest("CHILD",0)]
        with self.assertRaises(InvalidPurchaseException):
            self.ticket_service.purchase_tickets(account_id=3, ticket_type_requests=my_tickets)    

    def test_max_tickets(self):
        #tests that the number of tickets does not exceed 20
        my_tickets = [TicketTypeRequest("ADULT", 3),TicketTypeRequest("CHILD",19)]
        with self.assertRaises(InvalidPurchaseException):
            self.ticket_service.purchase_tickets(account_id=3, ticket_type_requests=my_tickets)

    def test_no_of_adults(self):
        my_tickets = [TicketTypeRequest("ADULT", 0),TicketTypeRequest("CHILD",19)]
        with self.assertRaises(InvalidPurchaseException):
            self.ticket_service.purchase_tickets(account_id=3, ticket_type_requests=my_tickets)

    def test_unnaccompanied_minors(self):
        my_tickets = [TicketTypeRequest("ADULT", 1),TicketTypeRequest("CHILD",2),TicketTypeRequest("INFANT",2)]
        with self.assertRaises(InvalidPurchaseException):
            self.ticket_service.purchase_tickets(account_id=3, ticket_type_requests=my_tickets)

    def test_valid_purchase(self):
        my_tickets = [TicketTypeRequest("ADULT", 2),TicketTypeRequest("CHILD",4),TicketTypeRequest("INFANT",2)]
        self.ticket_service.purchase_tickets(account_id=3, ticket_type_requests=my_tickets)
        
if __name__ == "__main__":
    unittest.main()