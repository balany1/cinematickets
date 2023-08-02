import unittest
import builtins
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
        account_id = self.ticket_service.purchase_tickets(account_id=1)
        print(account_id)
        self.assertGreater(account_id, 0)

    def test_tickets_requested(self):
        #tests that there has been a ticket requested
        number_of_tickets = self.ticket_service.purchase_tickets(account_id=1, ticket_type_requests=self.my_tickets)
        self.assertGreater(number_of_tickets, 0)
        pass

    def test_max_tickets(self):
        #tests that the number of tickets does not exceed 20
        number_of_tickets = self.ticket_service.purchase_tickets(account_id=1, ticket_type_requests=self.my_tickets)
        self.assertLessEqual(number_of_tickets, 20)
        pass

    def test_no_of_adults(self):
        #tests that there is at least one adult
        pass

    def test_unnaccompanied_minors(self):
        #tests that there aren't children travelling alone
        pass

if __name__ == "__main__":
    unittest.main()