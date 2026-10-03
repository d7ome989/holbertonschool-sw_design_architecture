#!/usr/bin/env python3


class Bus:
    def mode(self):
        return "road"


class Train:
    def mode(self):
        return "rails"


class Bike:
    def mode(self):
        return "lane"


class Scooter:
    def mode(self):
        return "scooter_lane"


class VehicleFactory:
    def __init__(self):
        self._registry = {}

    def register_kind(self, name, cls):
        self._registry[name] = cls

    def create(self, kind):
        return self._registry[kind]()


def main():
    factory = VehicleFactory()
    factory.register_kind("bus", Bus)
    factory.register_kind("train", Train)
    factory.register_kind("bike", Bike)

    print(factory.create("bus").mode())
    print(factory.create("train").mode())
    print(factory.create("bike").mode())

    factory.register_kind("scooter", Scooter)
    print(factory.create("scooter").mode())


main()
