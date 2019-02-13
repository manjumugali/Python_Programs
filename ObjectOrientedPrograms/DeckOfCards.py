"""
******************************************************************************
* Purpose:  Program To Demonstration Deck Of Cards
*
* @author:  Manjunath Mugali
* @version: 3.7
* @since:   28-01-2019
*
******************************************************************************
"""
from OOPS_Utility.Test_Oops_Utility import DeckOfCard


class DeckOfCards:
    try:
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]  # list stores the suits
        rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King",
                "Ace"]  # list stores rank of cards
        deck = DeckOfCard(rank, suits)  # creating object DeckOfCard class and passing parameters
        list_cards = deck.shuffleCards()  # on deck object invoking shuffleCards() function
        deck.dealCard(list_cards)  # on deck object invoking dealCard() function takes array as parameter
    except RuntimeError:
        print("oops Something Went Wrong......... Please Provide Only Integer Values.......")


if __name__ == "__main__":
    DeckOfCards()
