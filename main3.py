car_info = ("Toyota", "Camry", 2020)
print("=" * 30)
print(f"{car_info[0]} {car_info[1]} ({car_info[2]})")
print("=" * 30)

cities = []
distances = []
fuel_costs = []

consumption = float(input("Enter fuel consumption (L/100km): "))
fuel_price = float(input("Enter fuel price (KZT/L): "))

while True:
    city = input("Enter city (or 'done' to finish): ")
    if city.lower() == 'done':
        break
    distance = float(input("Enter distance (km): "))

    fuel_cost = distance * consumption / 100 * fuel_price

    cities.append(city)
    distances.append(distance)
    fuel_costs.append(fuel_cost)

print("-" * 30)
print(f"Your route ({len(cities)} stops):")
print("-" * 30)

for i in range(len(cities)):
    print(f"{cities[i]} {distances[i]} km {fuel_costs[i]} KZT")

print("-" * 30)

visited = set()

while True:
    city = input("Enter city (or 'done' to finish): ")
    if city.lower() == 'done':
        break
    visited.add(city)

print(f"Unique cities visited: {len(visited)}")
print(visited)

driver_name = input("Enter driver name: ")

total_distance = sum(distances)
total_cost = sum(fuel_costs)

if total_distance < 100:
    category = "Short trip"
elif total_distance < 500:
    category = "Medium trip"
else:
    category = "Long trip"

summary = {
    "driver": driver_name,
    "stops": len(cities),
    "total_distance": total_distance,
    "total_cost": total_cost,
    "category": category
}

print("=" * 30)
print(f"TRIP SUMMARY - {car_info[0]} {car_info[1]} ({car_info[2]})")
print("=" * 30)
print(f"Driver : {summary['driver']}")
print(f"Stops : {summary['stops']}")
print("-" * 30)

for i in range(len(cities)):
    print(f"{cities[i]} {distances[i]} km {fuel_costs[i]} KZT")

print("-" * 30)
print(f"Total distance : {summary['total_distance']} km")
print(f"Total fuel cost : {summary['total_cost']} KZT")
print(f"Category : {summary['category']}")
print("=" * 30)