"""
******************************************************************************
* Purpose:  Program To Demonstration Deck Of Cards using Linked List Queue.
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   30-01-2019
*
******************************************************************************
"""
from OOPS_Utility.Test_Oops_Utility import DeckOfCard
from OOPS_Utility.Test_Oops_Utility import LinkedListQueueCards

class DeckOfCardQueue:
    try:
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]  # list stores the suits
        rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King",
                "Ace"]  # list stores rank of cards
        deck = DeckOfCard(rank, suits)  # creating object DeckOfCard class and passing parameters
        list_cards = deck.shuffleCards()  # on deck object invoking shuffleCards() function
        matrix = deck.dealCard(list_cards)  # on deck object invoking dealCard() function takes array as parameter

        l1 = LinkedListQueueCards(matrix)   # creating object LinkedListQueueCards class and passing parameters
        l1.enQueueCards()                   # on l1 object invoking enQueueCards() functionSSSS
    except RuntimeError:
        print("oops Something Went Wrong......... Please Provide Only Integer Values.......")


if __name__ == "__main__":
    DeckOfCardQueue()
