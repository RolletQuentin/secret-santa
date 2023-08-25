from Person import Person
from emailSender import sendEmail
from secretSanta import draw

if __name__ == "__main__":

    # Create people :
    # Example :
    # alice = Person("Alice", "Group 1", "firegame1506@gmail.com")
    # bob = Person("Bob", "Group 2", "firegame1506@gmail.com")

    # Add people to the mailing list
    # Example
    # mailing_list = [alice, bob]
    mailing_list = []

    # Add some people into blacklist
    # Example :
    # alice.addPersonToBlackList(bob)

    # Set up the max iterations
    max_iterations = 50

    # Make the draw for the Secret Santa
    try:
        correspondance_dict = draw(mailing_list, max_iterations)
    except ValueError as err:
        print(err)
        exit()

    # Send emails
    for sender, receiver in correspondance_dict.items():
        message = f"""Hey {sender} !
        
        This year, you have to offer a gift to {receiver} !
        """
        print(sender.email)
        sendEmail(to_email=sender.email, message=message)
