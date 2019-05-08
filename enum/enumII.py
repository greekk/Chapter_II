import enum

#@enum.unique
class Status(enum.IntEnum):
    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1

    by_design = 4
    closed = 1

for status in Status:
    print("{:13} = {}".format(status.name, status.value))
print(Status.by_design)

print("\nSame: by_design is wont_fix: ", Status.by_design is Status.wont_fix)
print("Same: closed is fix_released: ", Status.closed is Status.fix_released)

