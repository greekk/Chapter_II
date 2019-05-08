import enum

class MyEnumeration(enum.Enum):
    new = 6
    incomplete = 5
    invalid = 5
    wont_fix= 4
    in_progress = 3
    fix_commited = 2
    fix_released = 1

print('\nMember name: {}'.format(MyEnumeration.wont_fix.name))
print('Member value: {}'.format(MyEnumeration.wont_fix.value))

for member in MyEnumeration:
    print("{:12} = {}".format(member.name, member.value))

actual_state = MyEnumeration.fix_commited.value
desired_state = MyEnumeration.fix_released.value

print(actual_state)
print(desired_state)

print("Equality:", actual_state == desired_state, actual_state == MyEnumeration.wont_fix)
print("Identity:", actual_state is desired_state, actual_state is MyEnumeration.wont_fix)

print("Ordered by value: ")
try:
    print("\n".join(" " + s.name for s in sorted(MyEnumeration)))
except TypeError as err:
    print(" Cannot sort: {}".format(err))
