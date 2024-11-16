import time
import random

class Junction:
    def __init__(self, name, capacities):
        self.name = name
        self.lines = {f"Line {i+1}": {'vehicles': 0, 'emergency': 0} for i in range(4)}
        self.capacities = capacities

    def update_vehicles(self, line, emergency, vehicle_count=None):
        if vehicle_count is None:
            vehicle_count = random.randint(0, self.capacities[line])  # Randomly generate vehicle count if not provided
        self.lines[line]['vehicles'] = vehicle_count
        self.lines[line]['emergency'] = emergency

    def get_traffic_distribution(self):
        return {line: data['vehicles'] for line, data in self.lines.items()}

    def get_emergency_status(self):
        return {line: data['emergency'] for line, data in self.lines.items()}

    def get_priority_lines(self):
        return sorted(self.lines.items(), key=lambda x: (-x[1]['emergency'], -x[1]['vehicles']))


class TrafficControlSystem:
    def __init__(self, junctions):
        self.junctions = junctions

    def synchronize_junctions(self, j1_line4, j2_line1):
        j1_outgoing = self.junctions[0].lines[j1_line4]['vehicles']
        j2_incoming = j1_outgoing + random.randint(0, 20)  # Random traffic from other roads
        
        j2_capacity_remaining = self.junctions[1].capacities[j2_line1] - self.junctions[1].lines[j2_line1]['vehicles']
        
        if j2_incoming > j2_capacity_remaining:
            return False  # J2 can't handle the incoming traffic
        return True

    def adjust_green_time(self, base_time, line_vehicles, max_vehicles):
        additional_time = (line_vehicles / max_vehicles) * base_time if max_vehicles > 0 else 0
        return base_time + additional_time

    def adjust_yellow_time(self, base_yellow_time, line_vehicles, max_vehicles):
        if line_vehicles > max_vehicles * 0.75:
            return base_yellow_time + 2  # Extend yellow light by 2 seconds if line is 75% full
        return base_yellow_time

    def adjust_red_time(self, base_red_time, previous_green_shortened):
        if previous_green_shortened:
            return base_red_time + 3  # Extend red light by 3 seconds if previous green was shortened
        return base_red_time

    def run_traffic_cycle(self):
        base_green_time = 10  # Base green time in seconds
        base_yellow_time = 3  # Base yellow light duration in seconds
        base_red_time = 5     # Base red light duration in seconds

        for i, junction in enumerate(self.junctions):
            print(f"\nJunction {junction.name} Signal Cycle:")
            max_vehicles = max(junction.get_traffic_distribution().values())
            for line, data in junction.get_priority_lines():
                green_time = self.adjust_green_time(base_green_time, data['vehicles'], max_vehicles)
                yellow_time = self.adjust_yellow_time(base_yellow_time, data['vehicles'], max_vehicles)
                red_time = base_red_time

                emergency_status = data['emergency']
                
                if emergency_status:
                    green_time += 5  # Extra 5 seconds for emergency vehicle

                previous_green_shortened = False

                # For J1 Line 4, check if J2 Line 1 can handle the incoming traffic
                if junction.name == "J1" and line == "Line 4":
                    can_handle = self.synchronize_junctions("Line 4", "Line 1")
                    if not can_handle:
                        green_time *= 0.7  # Reduce by 30% if J2 Line 1 can't handle the traffic
                        previous_green_shortened = True
                        print(f"J1 Line 4: Reduced green time due to J2 Line 1 capacity. New green time: {green_time:.2f} seconds.")
                
                red_time = self.adjust_red_time(base_red_time, previous_green_shortened)

                # Display signal timings
                print(f"{line}: Green for {green_time:.2f} seconds. Vehicles: {data['vehicles']}. Emergency: {'Yes' if emergency_status else 'No'}")
                time.sleep(0.5)  # Simulate waiting for green signal

                print(f"{line}: Yellow for {yellow_time:.2f} seconds. Vehicles: {data['vehicles']}.")
                time.sleep(0.5)  # Simulate waiting for yellow signal

                print(f"{line}: Red for {red_time:.2f} seconds. Vehicles: {data['vehicles']}.")
                time.sleep(0.5)  # Simulate waiting for red signal


# Setup junctions
capacities_j1 = {'Line 1': 50, 'Line 2': 40, 'Line 3': 30, 'Line 4': 45}
capacities_j2 = {'Line 1': 50, 'Line 2': 40, 'Line 3': 30, 'Line 4': 45}
j1 = Junction("J1", capacities_j1)
j2 = Junction("J2", capacities_j2)

# Update vehicles and emergency status for test cases (random vehicles, manual emergency)
j1.update_vehicles("Line 1", emergency=0)
j1.update_vehicles("Line 2", emergency=0)  # Emergency vehicle on Line 2
j1.update_vehicles("Line 3", emergency=0)
j1.update_vehicles("Line 4", emergency=0)

j2.update_vehicles("Line 1", emergency=0)
j2.update_vehicles("Line 2", emergency=0)
j2.update_vehicles("Line 3", emergency=0)
j2.update_vehicles("Line 4", emergency=0)  # Emergency vehicle on Line 4

# Initialize Traffic Control System
traffic_system = TrafficControlSystem([j1, j2])

# Run traffic control cycle
traffic_system.run_traffic_cycle()
