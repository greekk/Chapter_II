from collections import ChainMap

car_parts = {'hood':500, 'enfine': 5000, 'front door': 750}
car_options = {'A/C': 1000, 'Turbo': 2500, 'rollbar': 300}
car_accessories = {'cover':100, 'hood ornament': 150, 'seat cover': 99}

car_pricing = ChainMap(car_accessories, car_options, car_parts)
# print(car_pricing['hood'])
# print(car_pricing['A/C'])
# print(car_pricing.keys())
# print(car_pricing.values)

for key, value in car_pricing.items():
    print(f"{key:15} - {value}")


