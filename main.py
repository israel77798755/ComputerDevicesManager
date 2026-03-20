from computer import Computer

# Create an instance
my_computer = Computer()

# Add devices with categories
devices = {
    "Input": ["Keyboard", "Mouse", "Scanner", "Microphone"],
    "Output": ["Monitor", "Speaker", "Printer", "Headphones"],
    "Storage": ["SSD", "HDD", "Memory Card", "USB Flash Drive"],
    "Network": ["Router", "Ethernet Cable", "Modem"]
}

for category, items in devices.items():
    for item in items:
        my_computer.add(item, category)

# List all devices
print("All devices:", ', '.join(my_computer.list_items()))

# List devices by category
print("Input devices:", ', '.join(my_computer.list_by_category("Input")))

# Search for a device
device = "Router"
category = my_computer.search(device)
if category:
    print(f"{device} is in {category} category.")
else:
    print(f"{device} not found.")

# Remove a device
my_computer.remove("Router")
print("Devices after removing Router:", ', '.join(my_computer.list_items()))

# Save and load from file
my_computer.save_to_file("computer.json")
new_computer = Computer()
new_computer.load_from_file("computer.json")
print("Devices after loading from file:", ', '.join(new_computer.list_items()))