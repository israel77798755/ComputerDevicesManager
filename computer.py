import json  # for saving and loading

class Computer:
    def __init__(self):
        # Items stored by category
        self.items = {
            "Input": [],
            "Output": [],
            "Storage": [],
            "Network": []
        }

    def add(self, device, category):
        if category not in self.items:
            print(f"Category '{category}' does not exist.")
            return
        self.items[category].append(device)

    def remove(self, device):
        found = False
        for category, devices in self.items.items():
            if device in devices:
                devices.remove(device)
                found = True
                print(f"Removed {device} from {category} category.")
                break
        if not found:
            print(f"{device} not found in any category.")

    def list_items(self):
        all_devices = []
        for devices in self.items.values():
            all_devices.extend(devices)
        return all_devices

    def list_by_category(self, category):
        if category in self.items:
            return self.items[category]
        else:
            print(f"Category '{category}' does not exist.")
            return []

    def search(self, device):
        for category, devices in self.items.items():
            if device in devices:
                return category
        return None

    def __len__(self):
        return len(self.list_items())

    def __getitem__(self, index):
        return self.list_items()[index]

    def __contains__(self, device):
        return device in self.list_items()

    def __iter__(self):
        return iter(self.list_items())

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            json.dump(self.items, f)
        print(f"Computer saved to {filename}")

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as f:
                self.items = json.load(f)
            print(f"Computer loaded from {filename}")
        except FileNotFoundError:
            print(f"File {filename} not found.")