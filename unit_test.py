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
        number_of_tickets = 0
        for ticket_request in self.my_tickets:
            number_of_tickets = number_of_tickets + ticket_request.get_tickets_number()

        self.assertGreater(number_of_tickets, 0)
        

    def test_max_tickets(self):
        #tests that the number of tickets does not exceed 20
        number_of_tickets = 0
        for ticket_request in self.my_tickets:
            number_of_tickets = number_of_tickets + ticket_request.get_tickets_number()
        self.assertLessEqual(number_of_tickets, 20)
        pass

    def test_no_of_adults(self):
        no_of_adults = 0
        for ticket_request in self.my_tickets:
            if ticket_request.get_ticket_type() == "ADULT":
              no_of_adults = no_of_adults + ticket_request.get_tickets_number()
        
        self.assertGreater(no_of_adults,0)

    def test_unnaccompanied_minors(self):
        #tests that there aren't more infants than adults
        no_of_adults = 0
        no_of_infants = 0
        for ticket_request in self.my_tickets:
            if ticket_request.get_ticket_type() == "ADULT":
              no_of_adults = no_of_adults + ticket_request.get_tickets_number()
            if ticket_request.get_ticket_type() == "INFANT":
              no_of_infants = no_of_infants + ticket_request.get_tickets_number()
        
        self.assertGreater(no_of_adults,no_of_infants)

if __name__ == "__main__":
    unittest.main()