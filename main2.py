name = input("Enter driver name: ")
destination = input("Enter destination: ")
distance = float(input("Enter distance (km): "))
consumption = float(input("Enter fuel consumption (L/100km): "))
price = float(input("Enter fuel price (KZT/L): "))

litres_needed = distance * consumption / 100
cost = litres_needed * price

if distance < 100:
    category = "Short trip"
elif distance < 500:
    category = "Medium trip"
else:
    category = "Long trip"

print("=" * 30)
print(f"Driver : {name}")
print(f"Destination : {destination.upper()}")
print(f"Distance : {distance} km")
print(f"Fuel cost : {cost} KZT")
print(f"Category : {category}")
print("=" * 30)

print("\nCost breakdown:")

cost_per_km = cost / distance

for km in range(100, int(distance) + 1, 100):
    cum_cost = cost_per_km * km
    print(f"{km} km → {cum_cost} KZT")

print(f"\nDestination uppercase : {destination.upper()}")
print(f"Destination lowercase : {destination.lower()}")
print(f"Length : {len(destination)}")
print(f"Letter 'a' count : {destination.lower().count('a')}")