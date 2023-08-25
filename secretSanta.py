import random
from Person import Person


def draw_sender(mailing_list: list[Person], already_sender_list: list[Person]) -> Person:
    """Draw random sender who doesn't send a gift.
    """

    available_senders = [
        sender for sender in mailing_list if sender not in already_sender_list]

    if available_senders:
        return random.choice(available_senders)
    else:
        raise ValueError("No available senders.")


def draw_receiver(mailing_list: list[Person], already_receiver_list: list[Person], sender: Person) -> Person:
    """Draw random receiver who doesn't receive a gift. 

    Args:
        mailing_list (list): The mailing list.
        already_receiver_list (list): The list of people who already receive a gift.
        sender (dict): The sender of the gift.
    """

    available_receivers = [
        receiver for receiver in mailing_list if ((receiver not in already_receiver_list) and (receiver not in sender.blacklist) and (receiver.group != sender.group) and (sender != receiver))
    ]

    if available_receivers:
        return random.choice(available_receivers)
    else:
        raise ValueError("No available receivers.")


def draw(mailing_list, max_iteration=50):
    """Make the secret santa drawing.
    """

    already_sender_list = []  # people who already offers a gift
    already_receiver_list = []  # people who already receives a gift
    correspondence_dict = {}  # dict which represent the sender and the receiver

    i = 0  # iteration variable
    success = False

    while (not (success) and i < max_iteration):
        j = 0
        impossible = False
        already_receiver_list = []
        already_sender_list = []
        while (j < len(mailing_list) and not (impossible)):
            try:
                sender = draw_sender(mailing_list, already_sender_list)
                receiver = draw_receiver(
                    mailing_list, already_receiver_list, sender)
            except ValueError as err:
                print(err)
                impossible = True

            if not (impossible):
                already_sender_list.append(sender)
                already_receiver_list.append(receiver)
                correspondence_dict[sender] = receiver
                j += 1

        if j == len(mailing_list):
            success = True
        else:
            i += 1

    if success:
        return correspondence_dict
    else:
        raise ValueError("This draw seems to be impossible.")


if __name__ == "__main__":
    # Crete people
    alice = Person("Alice", "Group 1", "alice@example.com")
    bob = Person("Bob", "Group 1", "bob@example.com")
    charlie = Person("Charlie", "Group 1", "charlie@example.com")
    david = Person("David", "Group 2", "david@example.com")
    eve = Person("Eve", "Group 2", "eve@example.com")
    frank = Person("Frank", "Group 2", "frank@example.com")
    grace = Person("Grace", "Group 2", "grace@example.com")
    hannah = Person("Hannah", "Group 3", "hannah@example.com")
    isaac = Person("Isaac", "Group 3", "isaac@example.com")
    jane = Person("Jane", "Group 3", "jane@example.com")

    # # Add people to blacklist
    alice.addPersonToBlackList(bob)
    charlie.addPersonToBlackList(david)
    frank.addPersonToBlackList(grace)
    hannah.addPersonToBlackList(isaac)

    mailing_list = [
        alice, bob, charlie, david, eve, frank, grace, hannah, isaac, jane
    ]

    # draw sender tests
    # print(draw_sender(mailing_list, mailing_list[2:]))

    # draw receiver tests
    # print(draw_receiver(mailing_list, [
    #     charlie, eve, hannah, frank, jane, alice, bob, david, grace], jane))

    result = draw(mailing_list, 50)
    for key, value in result.items():
        print(f'${key} --> ${value}')
