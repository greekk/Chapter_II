class Human:

    def __init__(self, height = 0, weight=0, skin_color=""):
        self.height = height
        self.weight = weight
        self.skin_color = skin_color

    def walk(self):
        print("I'm walking!")

    def sleep(self):
        print("I'm sleeping!")


class Worker(Human):

    def __init__(self, age = 0, skill_level=0):
        self.age = age
        self.skill_level = skill_level

    def work(self):
        if self.age < 18:
            raise Exception("No working in this age!")

    def work_ending(self):
        print("Work is done!")

    def break_up(self):
        print("Work is breaking up!")


class BrickLayer(Worker):

    def work(self):
        try:
            super().work()
            print("I have laying the bricks!")
        except Exception as ex:
            print(ex)


