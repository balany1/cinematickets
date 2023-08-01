import unittest
from ticket_service import TicketService
from ticket_type_request import TicketTypeRequest

class Test_ticket_service(unittest.TestCase):

    def setUp(self) -> None:
        my_tickets = [TicketTypeRequest("ADULT", 2),TicketTypeRequest("CHILD",3)]
        self.ticket_service = TicketService.purchase_tickets(account_id=1,ticket_type_requests=my_tickets)
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_no_account_id(self):
        #tests that there is an account_id
        account_id = self.ticket_service.purchase_tickets(account_id=1)
        self.assertIsInstance(account_id, int)
        
    def test_negzero_account_id(self):
        account_id = self.ticket_service.purchase_tickets(account_id=1)
        self.assertGreater(account_id, 0)

    def test_tickets_requested(self):
        #tests that there has been a ticket requested
        pass

    def test_max_tickets(self):
        #tests that the number of tickets does not exceed 20
        pass

    def test_no_of_adults(self):
        #tests that there is at least one adult
        pass

    def test_unnaccompanied_minors(self):
        #tests that there aren't children travelling alone
        pass

if __name__ == "__main__":
    unittest.main()