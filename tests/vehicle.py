class InstanceAttribute:
    _cls_attr = 1
    def __init__(self):
        self.inst_attr = 2


# ia = InstanceAttribute()
# ia._cls_attr = 2
# print(InstanceAttribute._cls_attr)
# InstanceAttribute._cls_attr = 2
# print(InstanceAttribute._cls_attr)


class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def __repr__(self):
        return f"Vehicle name: {self.name} Speed: {self.max_speed}  Milage: {self.mileage}"


class Bus(Vehicle):
    def __init__(self, *args, **kwargs):
        super(Bus, self).__init__(*args, **kwargs)

    def seating_capacity(self):
        return 50


b = Bus("School Volvo", 108, 12)
print(b)
print(b.seating_capacity())
