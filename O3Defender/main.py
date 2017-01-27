from direct.showbase.ShowBase import ShowBase
from direct.task import Task


class Game(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        #self.disableMouse()

        self.sky = self.loader.loadModel("models/sky/blue-sky-sphere.egg")
        self.sky.reparentTo(self.render)

        self.environ_x = 0
        self.environ_y = 0
        self.environ_z = -3

        self.acceleration = 0.01

        self.environ_tilt_x = 0
        self.environ_tilt_y = 0
        self.environ_tilt_z = 0

        self.env = self.loader.loadModel("models/env/course2.egg")
        self.env.reparentTo(self.render)
        self.env.setPos(self.environ_x, self.environ_y, self.environ_z)
        self.env.setHpr(self.environ_tilt_x, self.environ_tilt_y, self.environ_tilt_z)

        self.actor = self.loader.loadModel("models/actor/sonic.egg")
        self.actor.reparentTo(self.render)
        self.actor.setPos(0, 5, -1)
        self.actor.setHpr(230, 0, 0)
        self.actor.setScale(0.05, 0.05, 0.05)

        #self.accept("space-repeat", self.move_ahead)
        self.accept("a-repeat", self.turn_left)
        self.accept("d-repeat", self.turn_right)
        self.accept("w-repeat", self.turn_up)
        self.accept("s-repeat", self.turn_down)
        self.accept("shift", self.boost_toggle)

        self.taskMgr.add(self.move_ahead, "move_ahead")

    def move_ahead(self, task):
        self.environ_y -= self.acceleration
        self.env.setPos(self.environ_x, self.environ_y, self.environ_z)
        return Task.cont

    def turn_left(self):
        pivot_node = self.render.attachNewNode("environ-pivot")
        pivot_node.setPos(0, 5, -1)
        self.env.wrtReparentTo(pivot_node)
        self.environ_tilt_x = 0
        self.environ_tilt_x -= 0.5
        pivot_node.setHpr(self.environ_tilt_x, self.environ_tilt_y, self.environ_tilt_z)

    def turn_right(self):
        pivot_node = self.render.attachNewNode("environ-pivot")
        pivot_node.setPos(0, 5, -1)
        self.env.wrtReparentTo(pivot_node)
        self.environ_tilt_x = 0
        self.environ_tilt_x += 0.5
        pivot_node.setHpr(self.environ_tilt_x, self.environ_tilt_y, self.environ_tilt_z)

    def turn_up(self):
        self.environ_z -= 0.1
        self.env.setPos(self.environ_x, self.environ_y, self.environ_z)

    def turn_down(self):
        self.environ_z += 0.1
        self.env.setPos(self.environ_x, self.environ_y, self.environ_z)

    def boost_toggle(self):
        if self.acceleration > 0.01:
            self.acceleration = 0.01
        else:
            self.acceleration = 0.1

game = Game()
game.run()