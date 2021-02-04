import pytest
import requests

'''
Map the vehicle type to the numeric value:
compact: 0
sedan  : 1
van    : 2
truck  : 3
'''
def calculated_vehicle_size(length, width, height, weight):
    if (length > 120 or width > 60) and (length > 60 or width > 120) or height > 60 or weight > 70:
        return 3
    elif (length > 24 or width > 36) and (length > 36 or width > 24) or height > 48 or weight > 50:
        return 2
    elif length > 24 or width > 24 or height > 36 or weight > 50:
        return 1
    else:
        return 0
'''
@pytest.mark.parametrize(
    "length, width, height, weight, expected",
    [
        (20, 20, 30, 60, 2),
        (90, 50, 62, 60, 3),
        (60, 90, 50, 60, 2),
    ]
)
'''
def test_calculated_vehicle_size(expected):
    response = requests.get("api/vehicle_size")
    # response format: [{},{}]
    for i in range(len(response)):
        data = response[i]
        length, width, height, weight = data['length'], data['width'], data['height'], data['weight']    
        assert calculated_vehicle_size(length, width, height, weight) == expected[i] 