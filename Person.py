class Person:

    def __init__(self, name: str, group: str, email: str) -> None:
        self.name = name
        self.group = group
        self.email = email
        self.blacklist = []

    def __repr__(self):
        return f"Person(name={self.name}, group={self.group})"

    def addPersonToBlackList(self, person):
        self.blacklist.append(person)
