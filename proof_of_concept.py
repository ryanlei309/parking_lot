import easyocr
import cv2
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timezone
from datetime import timedelta


reader = easyocr.Reader(["en"], gpu=False)
parked_vehicles = dict()
# img_path = "data/car_plate_1.jpg"
# results = reader.readtext(img_path)

"""
x_points = []
y_points = []
for xi, yi in results[0][0]:
    x_points.append(int(xi))
    y_points.append(int(yi))
left_top = (min(x_points), min(y_points))
right_bottom = (max(x_points), max(y_points))
img = cv2.imread(img_path)
cv2.rectangle(img, left_top, right_bottom, (0, 255, 0), 5)
plt.imshow(img)
plt.show()


results = reader.readtext("data/car_plate_1.jpg", detail=0)
print(results)

# 紀錄進場時間
entry_time = datetime.now(timezone.utc) + timedelta(hours=8)
print(entry_time)

# 紀錄出場時間與計算停留時間
leaving_time = datetime.now(timezone.utc) + timedelta(hours=8)
time_elapsed = leaving_time - entry_time
print(leaving_time)
print(time_elapsed)
print(int(time_elapsed.total_seconds()))
"""

def parking_lot_ocr(img_path: str, ntd_per_sec: int=1):
    results = reader.readtext(img_path, detail=0)
    entry_time = datetime.now(timezone.utc) + timedelta(hours=8)
    entry_time_str = entry_time.strftime("%Y-%m-%d %H:%M:%S")
    car_plate = results[0]

    # 記錄進場時間
    if car_plate not in parked_vehicles.keys():
        parked_vehicles[car_plate] = entry_time
        print(f"Welcome to the parking lot {car_plate}!")
        print(f"Your entry time is: {entry_time_str}.")
        print(f"Parking fee is NT${ntd_per_sec} per second.")
    
    # 記錄出場時間
    else:
        leaving_time = datetime.now(timezone.utc) + timedelta(hours=8)
        time_elapsed = leaving_time - parked_vehicles[car_plate]
        seconds_elapsed = int(time_elapsed.total_seconds())
        charge_amount = seconds_elapsed * ntd_per_sec
        print(f"Bye bye bye {car_plate}!")
        print(f"Your vehicle stayed {seconds_elapsed} seconds.")
        print(f"You will be charged NT${charge_amount:,}.")
        parked_vehicles.pop(car_plate, None)

parking_lot_ocr("data/car_plate_1.jpg")
print(parked_vehicles)

parking_lot_ocr("data/car_plate_1.jpg")
print(parked_vehicles)