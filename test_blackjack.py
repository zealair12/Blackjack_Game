from unittest import TestCase, main
from unittest.mock import patch
from test_helper import run_test

class TestBlackjack(TestCase):

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_example(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The dealer wins by having a higher hand than the user.

        This does not count as one of your tests.
        '''
        output = run_test([3, 5, 8], ['y', 'n'], [3, 5, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "You have 16. Hit (y/n)? n\n" \
                   "Final hand: 16.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 10\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    # Make sure all your test functions start with test_ 
    # Follow indentation of test_example
    # WRITE ALL YOUR TESTS BELOW. Do not delete this line.

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_wins_by_blackjack(self, input_mock, randint_mock):
        """
        Test case where the user wins by hitting Blackjack.
        The dealer does not bust or hit Blackjack.
        """
        output = run_test([10, 1], [], [10, 8], randint_mock, input_mock)
        expected = (
            "-----------\n"
            "YOUR TURN\n"
            "-----------\n"
            "Drew a 10\n"
            "Drew an Ace\n"
            "Final hand: 21.\n"
            "BLACKJACK!\n"
            "-----------\n"
            "DEALER TURN\n"
            "-----------\n"
            "Drew a 10\n"
            "Drew an 8\n"
            "Final hand: 18.\n"
            "-----------\n"
            "GAME RESULT\n"
            "-----------\n"
            "You win!\n"
        )
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_wins_by_dealer_bust(self, input_mock, randint_mock):
        """
        Test case where the user wins because the dealer busts.
        The user does not bust (User's Final hand < 21).
        """
        output = run_test([3, 5], ['n'], [10, 6, 8], randint_mock, input_mock)
        expected = (
            "-----------\n"
            "YOUR TURN\n"
            "-----------\n"
            "Drew a 3\n"
            "Drew a 5\n"
            "You have 8. Hit (y/n)? n\n"
            "Final hand: 8.\n"
            "-----------\n"
            "DEALER TURN\n"
            "-----------\n"
            "Drew a 10\n"
            "Drew a 6\n"
            "Dealer has 16.\n"
            "Drew an 8\n"
            "Final hand: 24.\n"
            "BUST.\n"
            "-----------\n"
            "GAME RESULT\n"
            "-----------\n"
            "You win!\n"
        )
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_wins_by_higher_hand(self, input_mock, randint_mock):
        """
        Test case where the user wins with a hand less than 21 but higher than the dealer's hand.
        """
        output = run_test([7, 8, 3], ['y', 'n'], [5, 7, 5], randint_mock, input_mock)
        expected = (
            "-----------\n"
            "YOUR TURN\n"
            "-----------\n"
            "Drew a 7\n"
            "Drew an 8\n"
            "You have 15. Hit (y/n)? y\n"
            "Drew a 3\n"
            "You have 18. Hit (y/n)? n\n"
            "Final hand: 18.\n"
            "-----------\n"
            "DEALER TURN\n"
            "-----------\n"
            "Drew a 5\n"
            "Drew a 7\n"
            "Dealer has 12.\n"
            "Drew a 5\n"
            "Final hand: 17.\n"
            "-----------\n"
            "GAME RESULT\n"
            "-----------\n"
            "You win!\n"
        )
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_busts(self, input_mock, randint_mock):
        """
        Test case where the user busts and loses (17 <= Final hand of Dealer < 21).
        """
        output = run_test([7, 6, 10], ['y', 'n'], [5, 7, 2, 4], randint_mock, input_mock)
        expected = (
            "-----------\n"
            "YOUR TURN\n"
            "-----------\n"
            "Drew a 7\n"
            "Drew a 6\n"
            "You have 13. Hit (y/n)? y\n"
            "Drew a 10\n"
            "Final hand: 23.\n"
            "BUST.\n"
            "-----------\n"
            "DEALER TURN\n"
            "-----------\n"
            "Drew a 5\n"
            "Drew a 7\n"
            "Dealer has 12.\n"
            "Drew a 2\n"
            "Dealer has 14.\n"
            "Drew a 4\n"
            "Final hand: 18.\n"
            "-----------\n"
            "GAME RESULT\n"
            "-----------\n"
            "Dealer wins!\n"
        )
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_blackjack(self, input_mock, randint_mock):
        """
        Test case where the dealer wins by hitting Blackjack.
        The user does not bust.
        """
        output = run_test([10, 7], ['n'], [1, 10], randint_mock, input_mock)
        expected = (
            "-----------\n"
            "YOUR TURN\n"
            "-----------\n"
            "Drew a 10\n"
            "Drew a 7\n"
            "You have 17. Hit (y/n)? n\n"
            "Final hand: 17.\n"
            "-----------\n"
            "DEALER TURN\n"
            "-----------\n"
            "Drew an Ace\n"
            "Drew a 10\n"
            "Final hand: 21.\n"
            "BLACKJACK!\n"
            "-----------\n"
            "GAME RESULT\n"
            "-----------\n"
            "Dealer wins!\n"
        )
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_push_same_hand(self, input_mock, randint_mock):
        """
        Test case where the game ends in a push because both the user and dealer
        have the same hand (under 21).
        """
        output = run_test([5, 6, 9], ['y','n'], [7, 4, 5, 4], randint_mock, input_mock)
        expected = (
            "-----------\n"
            "YOUR TURN\n"
            "-----------\n"
            "Drew a 5\n"
            "Drew a 6\n"
            "You have 11. Hit (y/n)? y\n"
            "Drew a 9\n"
            "You have 20. Hit (y/n)? n\n"
            "Final hand: 20.\n"
            "-----------\n"
            "DEALER TURN\n"
            "-----------\n"
            "Drew a 7\n"
            "Drew a 4\n"
            "Dealer has 11.\n"
            "Drew a 5\n"
            "Dealer has 16.\n"
            "Drew a 4\n"
            "Final hand: 20.\n"
            "-----------\n"
            "GAME RESULT\n"
            "-----------\n"
            "Push.\n"
        )
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_tie_blackjack(self, input_mock, randint_mock):
        """
        Test case where the game ends in a tie because both the user and dealer get Blackjack.
        """
        output = run_test([1, 10], ['n'], [1, 10], randint_mock, input_mock)
        expected = (
            "-----------\n"
            "YOUR TURN\n"
            "-----------\n"
            "Drew an Ace\n"
            "Drew a 10\n"
            "Final hand: 21.\n"
            "BLACKJACK!\n"
            "-----------\n"
            "DEALER TURN\n"
            "-----------\n"
            "Drew an Ace\n"
            "Drew a 10\n"
            "Final hand: 21.\n"
            "BLACKJACK!\n"
            "-----------\n"
            "GAME RESULT\n"
            "-----------\n"
            "Push.\n"
        )
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_bust_dealer_blackjack(self, input_mock, randint_mock):
        """
        Test case where the user busts and the dealer hits Blackjack.
        """
        output = run_test([7, 8, 10], ['y'], [1, 10], randint_mock, input_mock)
        expected = (
            "-----------\n"
            "YOUR TURN\n"
            "-----------\n"
            "Drew a 7\n"
            "Drew an 8\n"
            "You have 15. Hit (y/n)? y\n"
            "Drew a 10\n"
            "Final hand: 25.\n"
            "BUST.\n"
            "-----------\n"
            "DEALER TURN\n"
            "-----------\n"
            "Drew an Ace\n"
            "Drew a 10\n"
            "Final hand: 21.\n"
            "BLACKJACK!\n"
            "-----------\n"
            "GAME RESULT\n"
            "-----------\n"
            "Dealer wins!\n"
        )
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_both_bust(self, input_mock, randint_mock):
        """
        Test case where both the user and dealer bust, resulting in a win for Dealer.
        """
        output = run_test([7, 9, 6], ['y'], [10, 6, 7], randint_mock, input_mock)
        expected = (
            "-----------\n"
            "YOUR TURN\n"
            "-----------\n"
            "Drew a 7\n"
            "Drew a 9\n"
            "You have 16. Hit (y/n)? y\n"
            "Drew a 6\n"
            "Final hand: 22.\n"
            "BUST.\n"
            "-----------\n"
            "DEALER TURN\n"
            "-----------\n"
            "Drew a 10\n"
            "Drew a 6\n"
            "Dealer has 16.\n"
            "Drew a 7\n"
            "Final hand: 23.\n"
            "BUST.\n"
            "-----------\n"
            "GAME RESULT\n"
            "-----------\n"
            "Dealer wins!\n"
        )
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_wins_higher_hand(self, input_mock, randint_mock):
        """
        Test case where the dealer wins with a higher hand under 21.
        """
        output = run_test([5, 6], ['n'], [9, 8], randint_mock, input_mock)
        expected = (
            "-----------\n"
            "YOUR TURN\n"
            "-----------\n"
            "Drew a 5\n"
            "Drew a 6\n"
            "You have 11. Hit (y/n)? n\n"
            "Final hand: 11.\n"
            "-----------\n"
            "DEALER TURN\n"
            "-----------\n"
            "Drew a 9\n"
            "Drew an 8\n"
            "Final hand: 17.\n"
            "-----------\n"
            "GAME RESULT\n"
            "-----------\n"
            "Dealer wins!\n"
        )
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_wins_higher_hand(self, input_mock, randint_mock):
        """
        Test case where the user wins with a Blackjack and the Dealer Busts.
        """
        output = run_test([8, 1, 2], ['y','y'], [1, 1], randint_mock, input_mock)
        expected = (
            "-----------\n"
            "YOUR TURN\n"
            "-----------\n"
            "Drew an 8\n"
            "Drew an Ace\n"
            "You have 19. Hit (y/n)? y\n"
            "Drew a 2\n"
            "Final hand: 21.\n"
            "BLACKJACK!\n"            
            "-----------\n"
            "DEALER TURN\n"
            "-----------\n"
            "Drew an Ace\n"
            "Drew an Ace\n"
            "Final hand: 22.\n"
            "BUST.\n"
            "-----------\n"
            "GAME RESULT\n"
            "-----------\n"
            "You win!\n"
        )
        self.assertEqual(output, expected)
    # Write all your tests above this. Do not delete this line.

if __name__ == '__main__':
    main()
