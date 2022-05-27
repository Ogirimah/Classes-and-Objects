from array import array


class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = ['General'] + tracks
        self.score = int(round(score))

    def __repr__(self) -> str:
        return (f'Student({self.name!r}, '
        f'{self.age!r}, '
        f'{self.tracks!r}, '
        f'{self.score!r})')

    def change_name(self, new_name):
        self.name = new_name

    def change_age(self, new_age):
        self.age = new_age

    def add_track(self, new_track):
        new_track = new_track.split()
        self.tracks = self.tracks + new_track

    def get_score(self):
        return self.score
        



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

print(Bob)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

print(Bob)