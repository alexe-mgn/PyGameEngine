import pymunk
from Engine.geometry import Vec2d
from Engine.loading import load_model, cast_model
from Engine.physics import BaseProjectile

NAME = __name__.split('.')[1]
MODEL = load_model('Projectiles\\Models\\%s' % (NAME,))

CS = Vec2d(0, 0)


class Projectile(BaseProjectile):
    size_inc = 1
    lifetime = 1000
    damage = 10

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.body = pymunk.Body()
        self.shape = pymunk.Poly(self.body, self.RADIUS)
        self.shape.density = 1

    @classmethod
    def init_class(cls):
        cls._frames, cls.IMAGE_SHIFT = cast_model(MODEL, CS, cls.size_inc)
        cls.precalculate_shape()
        cls.calculate_poly_shape()

    @classmethod
    def precalculate_shape(cls):
        radius = 10

        cls.RADIUS = radius * cls.size_inc

    @classmethod
    def calculate_poly_shape(cls):
        img_poly_left = []
        poly_left = [tuple(e[n] - CS[n] for n in range(2)) for e in img_poly_left]
        poly_right = [(e[0], -e[1]) for e in poly_left[::-1]]
        cls.POLY_SHAPE = [(e[0] * cls.size_inc, e[1] * cls.size_inc) for e in poly_left + poly_right]


Projectile.init_class()
