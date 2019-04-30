import random
from typing import List

<<<<<<< HEAD
from magic_methods.lifetime import Programmer
=======
from lection.magic_methods.lifetime import Programmer
>>>>>>> df016b159cd1c734d557d2b92ea75377bf916c2b


class ITCompany:
    members: List[Programmer]

    def __init__(self, name, years, members=None):
        self.name = name
        self.years = years
        self.members = members if members is not None else []
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.current < len(self.members):
            res = self.members[self.current]
            self.current += 1
            return res
        else:
            self.current = 0
            raise StopIteration

    def __contains__(self, item):
        return item in self.members


if __name__ == "__main__":
    names = ["Den", "Illya", "Alex", "Oksana", "Peter", "Vasya"]
    languages = ["Python", "PHP", "C++", "C#", "Java", "1C", "Go", "Ruby", "Rust", "R"]
    positions = ["trainee", "junior", "middle", "senior", "tech lead"]

    programmers = []
<<<<<<< HEAD
    for _ in range(2):
=======
    for _ in range(5):
>>>>>>> df016b159cd1c734d557d2b92ea75377bf916c2b
        programmer = Programmer(
            name=random.choice(names),
            language=random.choice(languages),
            position=random.choice(positions)
        )
        programmers.append(programmer)

    company = ITCompany(name="Ralabs", members=programmers, years=6)
<<<<<<< HEAD
=======
    
    default_list = [1, 2, 3, 4, 5, 6]
    for i in default_list:
        print(i)
    # Lets see what we have in our company now
    for member in company:
        print(member)
>>>>>>> df016b159cd1c734d557d2b92ea75377bf916c2b

    # Lets see what we have in our company now
    for p in company:
        print(p)

<<<<<<< HEAD
=======

>>>>>>> df016b159cd1c734d557d2b92ea75377bf916c2b
    # We should find this programmer in our company
    programmer = random.choice(programmers)
    print(f"Do we have this programmer {programmer} in company {company}? -{programmer in company}")

    # And this not
    batman = Programmer(name="Batman", position=["Team Lead"], language="Fists")
    print(f"Do we have this programmer {batman} in company {company}? -{batman in company}")
<<<<<<< HEAD

=======
>>>>>>> df016b159cd1c734d557d2b92ea75377bf916c2b
