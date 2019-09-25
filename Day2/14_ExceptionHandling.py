i, j = 10, "2"
div = 0

def exceptTest(p, q):
    try:
        div = p / q
        print("Result: ", div)
    except ZeroDivisionError:
        print("Denominator is zero.")
    except Exception as e:
        print("Generic exception", e.args)

    finally:
        q = 1

    return p, q

i, j = exceptTest(i, j)

print(j)


# Raising exceptions
capacity = int(input("Enter vehicle capacity "))
if (capacity <= 0):
    raise ValueError('Capacity error!')


class VehicleCapacityError(ValueError):
    def __init__(self, msg, min_cap):
        super().__init__(msg)
        self.minimum = min_cap


# some functionality updates the value
# Raising exceptions if value not acceptable
def setVehicleCapacity(cap):
    if (capacity <= 0):
        raise VehicleCapacityError('Capacity error!', 0)
    else:
        print("Capacity updated")


capacity = int(input("Enter vehicle capacity "))
try:
    setVehicleCapacity(capacity)
except VehicleCapacityError as err:
    print(str(err), "Minimum required: ", err.minimum)
