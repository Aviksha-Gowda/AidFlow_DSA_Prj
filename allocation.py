# def allocate_resources(total_resources, population_dict):
#     total_people = sum(population_dict.values())
#     allocation = {zone: int(total_resources * population_dict[zone] / total_people) 
#                   for zone in population_dict}
#     return allocation


# def allocate_resources(total_resources, population_dict):
#     total_people = sum(population_dict.values())
#     allocation = {zone: int(total_resources * population_dict[zone] / total_people) 
#                   for zone in population_dict}
#     return allocation











#2 3
# Severity weights
# severity_weight = {'Low': 1, 'Medium': 2, 'High': 3}

# def allocate_resources_by_severity(total_resources, population_dict, severity_dict):
#     """
#     Allocate resources based on severity priority.
#     Returns allocation dict and list of zones not fully allocated (delayed zones)
#     """
#     # Convert severity to weight
#     weighted_severity = {zone: severity_weight[severity_dict[zone]] for zone in population_dict}
    
#     # Sort zones by severity descending
#     sorted_zones = sorted(population_dict.keys(), key=lambda z: weighted_severity[z], reverse=True)
    
#     allocation = {zone: 0 for zone in population_dict}
#     remaining_resources = total_resources
    
#     # Allocate proportional to population within severity priority
#     for zone in sorted_zones:
#         if remaining_resources <= 0:
#             break
#         alloc = min(population_dict[zone], remaining_resources)
#         allocation[zone] = alloc
#         remaining_resources -= alloc
    
#     # Zones not fully allocated
#     delayed_zones = [zone for zone in population_dict if allocation[zone] < population_dict[zone]]
    
#     return allocation, delayed_zones









#4# allocation.py

# def allocate_by_user_priority(total_resources, population_dict, priority_order):
#     """
#     Allocate resources strictly according to user-defined priority order.
#     Returns allocation dict and list of zones that may be delayed.
#     """
#     allocation = {zone: 0 for zone in population_dict}
#     remaining = total_resources
#     delayed_zones = []

#     for zone in priority_order:
#         if remaining <= 0:
#             delayed_zones.append(zone)
#             continue
#         # Allocate as much as possible
#         alloc = min(population_dict[zone], remaining)
#         allocation[zone] = alloc
#         remaining -= alloc

#     return allocation, delayed_zones







#5 Include Partially Allocated Zones ---all working
# def allocate_by_user_priority(total_resources, population_dict, priority_order):
#     allocation = {zone: 0 for zone in population_dict}
#     remaining = total_resources
#     delayed_zones = []

#     for zone in priority_order:
#         needed = population_dict[zone]
#         alloc = min(needed, remaining)
#         allocation[zone] = alloc
#         remaining -= alloc

#         # Flag as delayed if allocation < needed
#         if alloc < needed:
#             delayed_zones.append(zone)

#         # Stop allocation if resources exhausted
#         if remaining <= 0:
#             continue

#     return allocation, delayed_zones







def allocate_and_split_routes(total_resources, truck_capacity, destinations, population_dict):
    """
    Solves a basic Capacitated Vehicle Routing Problem (CVRP).
    Splits destinations into multiple trips if truck capacity is exceeded.
    """
    trips = []
    current_trip = []
    current_load = 0
    
    for dest in destinations:
        demand = population_dict[dest]
        if current_load + demand <= truck_capacity:
            current_trip.append(dest)
            current_load += demand
        else:
            # Finalize trip and start new one
            trips.append(current_trip)
            current_trip = [dest]
            current_load = demand
    
    if current_trip:
        trips.append(current_trip)
        
    return trips