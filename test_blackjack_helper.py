from blackjack_helper import *
from test_helper import *
import unittest

class TestBlackjackHelper(unittest.TestCase):
  """
  Class for testing blackjack helper functions.
  """

  def test_print_card_name_example(self):
    """
    Example of a test to compare printed statements with expected

    This does not count as one of your tests
    """
    self.assertEqual(get_print(print_card_name, 2), "Drew a 2\n")

  def test_mock_randint_example(self):
    """
    Example of a test to compare output for a function that calls randint

    This does not count as one of your tests
    """
    self.assertEqual(mock_random([3], draw_card), 3)
    self.assertEqual(mock_random([3, 5], draw_starting_hand, "DEALER"), 8)

  # MAKE SURE ALL YOUR FUNCTION NAMES BEGIN WITH test_
  # WRITE YOUR TESTS BELOW.

  def test_print_card_name(self):
    # Test with a valid card rank (Ace)
    self.assertEqual(get_print(print_card_name, 1), "Drew an Ace\n")
    # Test with a valid card rank (Jack)
    self.assertEqual(get_print(print_card_name, 11), "Drew a Jack\n")
    # Test with an invalid card(0)
    self.assertEqual(get_print(print_card_name, 0), "BAD CARD\n")
    # Test with an invalid card rank (14)
    self.assertEqual(get_print(print_card_name, 14), "BAD CARD\n")
    # Test with a middle card rank (7)
    self.assertEqual(get_print(print_card_name,7), "Drew a 7\n")


  def test_draw_card(self):
    # Test with a mocked randint returning Ace (11)
    self.assertEqual(mock_random([1], draw_card), 11)
    # Test with a mocked randint returning King (10)
    self.assertEqual(mock_random([13], draw_card), 10)
    # Test with a mocked randint returning a middle card (7)
    self.assertEqual(mock_random([7], draw_card), 7)

  def test_print_header(self):
    # Test header with a simple message
    output = "-----------\nGAME START\n-----------\n"
    self.assertEqual(get_print(print_header, "GAME START"), output)
    # Test header with a different message
    output = "-----------\nDEALER TURN\n-----------\n"
    self.assertEqual(get_print(print_header, "DEALER TURN"), output)
    # Test header with an empty message
    output = "-----------\n\n-----------\n"
    self.assertEqual(get_print(print_header, ""), output)

  def test_draw_starting_hand(self):
    # Test drawing a hand with mocked randint returning 3 and 5
    self.assertEqual(mock_random([3, 5], draw_starting_hand, "YOUR"), 8)
    # Test drawing a hand with mocked randint returning 10 and Ace
    self.assertEqual(mock_random([10, 1], draw_starting_hand, "DEALER"), 21)
    # Test drawing a hand with mocked randint returning two Aces
    self.assertEqual(mock_random([1, 1], draw_starting_hand, "PLAYER"), 22)
    # Test drawing a hand with mocked randint returning two facecards
    self.assertEqual(mock_random([10,10], draw_starting_hand, ""), 20)

  def test_print_end_turn_status(self):
    # Test for a final hand value less than 21 (Normal case)
    self.assertEqual(get_print(print_end_turn_status, 20), "Final hand: 20.\n")
    # Test for a final hand value of 21 (Blackjack)
    self.assertEqual(get_print(print_end_turn_status, 21), "Final hand: 21.\nBLACKJACK!\n")
    # Test for a final hand value over 21 (Bust)
    self.assertEqual(get_print(print_end_turn_status, 22), "Final hand: 22.\nBUST.\n")


  def test_print_end_game_status(self):
    # Test where the user wins
    output = "-----------\nGAME RESULT\n-----------\nYou win!\n"
    self.assertEqual(get_print(print_end_game_status, 19, 18), output)
    # Test where the user wins when dealer busts
    output = "-----------\nGAME RESULT\n-----------\nYou win!\n"
    self.assertEqual(get_print(print_end_game_status, 18, 23), output)    
    # Test where the dealer wins
    output = "-----------\nGAME RESULT\n-----------\nDealer wins!\n"
    self.assertEqual(get_print(print_end_game_status, 18, 19), output)
    # Test where the dealer wins if they both bust
    output = "-----------\nGAME RESULT\n-----------\nDealer wins!\n"
    self.assertEqual(get_print(print_end_game_status, 25, 22), output)
    # Test for a push (tie)
    output = "-----------\nGAME RESULT\n-----------\nPush.\n"
    self.assertEqual(get_print(print_end_game_status, 21, 21), output)

if __name__ == '__main__':
    unittest.main()
