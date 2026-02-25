# import streamlit as st
# import pandas as pd
# from routing import create_graph, get_routes
# from allocation import allocate_resources
# from visualization import plot_routes

# # Load data
# locations = pd.read_csv('data/locations.csv')
# edges_file = 'data/edges.csv'
# G = create_graph(edges_file)

# # UI Inputs
# relief_centers = locations[locations['Type']=='Relief Center']['Name'].tolist()
# affected_zones = locations[locations['Type']=='Affected Zone']['Name'].tolist()

# origin = st.selectbox('Select Relief Center (Origin):', relief_centers)
# destinations = st.multiselect('Select Affected Zones:', affected_zones)
# total_resources = st.number_input('Total Relief Packages Available:', min_value=1)
# people_per_destination = {zone: int(locations[locations['Name']==zone]['Population'].values[0]) for zone in destinations}

# if st.button('Submit'):
#     routes = get_routes(G, origin, destinations)
#     allocation = allocate_resources(total_resources, people_per_destination)
    
#     # Display results
#     for zone in destinations:
#         st.write(f"Destination: {zone}")
#         st.write(f"Route: {routes[zone]}")
#         st.write(f"Resources Allocated: {allocation[zone]}")
    
#     # Map visualization
#     # Define some dummy coordinates or use real lat/lon
#     locations_coords = {loc: (12.97, 77.59) for loc in relief_centers + affected_zones}
#     route_map = plot_routes(routes, locations_coords)
#     st.write(route_map)












#2
# import streamlit as st
# from routing import create_graph, get_routes
# from allocation import allocate_resources
# from visualization import plot_routes
# from streamlit_folium import st_folium

# # ---------- Data ----------
# edges_file = 'data/edges.csv'
# G = create_graph(edges_file)

# relief_centers = ['Center A', 'Center B', 'Center C']
# affected_zones = ['Zone 1', 'Zone 2', 'Zone 3', 'Zone 4', 'Zone 5']

# # ---------- Streamlit UI ----------
# st.title("Disaster Relief Routing & Resource Allocation System")

# origin = st.selectbox("Select Relief Center (Origin):", relief_centers)

# st.subheader("Enter Population for Each Affected Zone")
# population_per_zone = {}
# for zone in affected_zones:
#     population_per_zone[zone] = st.number_input(f'Population in {zone}:', min_value=1, value=100)

# st.subheader("Enter Total Resources Available")
# total_food_kits = st.number_input("Total Food Kits:", min_value=0, value=500)
# total_medicinal_kits = st.number_input("Total Medicinal Kits:", min_value=0, value=200)
# total_clothes = st.number_input("Total Clothes:", min_value=0, value=300)

# if st.button("Submit"):
#     # ---------- Routing ----------
#     routes = get_routes(G, origin, affected_zones)
    
#     # ---------- Resource Allocation ----------
#     food_allocation = allocate_resources(total_food_kits, population_per_zone)
#     med_allocation = allocate_resources(total_medicinal_kits, population_per_zone)
#     clothes_allocation = allocate_resources(total_clothes, population_per_zone)
    
#     # ---------- Display Results ----------
#     st.subheader("Routing & Resource Allocation")
#     for zone in affected_zones:
#         st.write(f"**{zone}**")
#         st.write(f"Route: {' → '.join(routes[zone])}")
#         st.write(f"Population: {population_per_zone[zone]}")
#         st.write(f"Food Kits: {food_allocation[zone]}")
#         st.write(f"Medicinal Kits: {med_allocation[zone]}")
#         st.write(f"Clothes: {clothes_allocation[zone]}")
#         st.write("---")
    
#     # ---------- Map Visualization ----------
#     # Dummy coordinates for demonstration
#     locations_coords = {
#         'Center A': (12.97, 77.59),
#         'Center B': (12.98, 77.58),
#         'Center C': (12.96, 77.57),
#         'Zone 1': (12.99, 77.60),
#         'Zone 2': (12.95, 77.61),
#         'Zone 3': (12.94, 77.59),
#         'Zone 4': (12.93, 77.60),
#         'Zone 5': (12.92, 77.58)
#     }
    
#     route_map = plot_routes(routes, locations_coords)
#     st.subheader("Map Visualization")
#     st_folium(route_map, width=700, height=500)











#3
# import streamlit as st
# from routing import create_graph, get_routes
# from allocation import allocate_resources_by_severity
# from visualization import plot_routes
# from streamlit_folium import st_folium

# # ---------- Data ----------
# edges_file = 'data/edges.csv'
# G = create_graph(edges_file)

# relief_centers = ['Center A', 'Center B', 'Center C']
# affected_zones = ['Zone 1', 'Zone 2', 'Zone 3', 'Zone 4', 'Zone 5']

# severity_options = ['Low', 'Medium', 'High']

# # ---------- Streamlit UI ----------
# st.title("Disaster Relief Routing & Priority Resource Allocation System")

# origin = st.selectbox("Select Relief Center (Origin):", relief_centers)

# st.subheader("Enter Population for Each Affected Zone")
# population_per_zone = {}
# for zone in affected_zones:
#     population_per_zone[zone] = st.number_input(f'Population in {zone}:', min_value=1, value=100)

# st.subheader("Enter Severity for Each Affected Zone")
# severity_per_zone = {}
# for zone in affected_zones:
#     severity_per_zone[zone] = st.selectbox(f"Severity in {zone}:", severity_options, index=1)

# st.subheader("Enter Total Resources Available")
# total_food_kits = st.number_input("Total Food Kits:", min_value=0, value=500)
# total_medicinal_kits = st.number_input("Total Medicinal Kits:", min_value=0, value=200)
# total_clothes = st.number_input("Total Clothes:", min_value=0, value=300)

# if st.button("Submit"):
#     # ---------- Routing ----------
#     routes = get_routes(G, origin, affected_zones)
    
#     # ---------- Resource Allocation ----------
#     food_allocation, delayed_food = allocate_resources_by_severity(
#         total_food_kits, population_per_zone, severity_per_zone
#     )
#     med_allocation, delayed_med = allocate_resources_by_severity(
#         total_medicinal_kits, population_per_zone, severity_per_zone
#     )
#     clothes_allocation, delayed_clothes = allocate_resources_by_severity(
#         total_clothes, population_per_zone, severity_per_zone
#     )
    
#     # ---------- Display Results ----------
#     st.subheader("Routing & Resource Allocation")
#     for zone in affected_zones:
#         st.write(f"**{zone}**")
#         st.write(f"Route: {' → '.join(routes[zone])}")
#         st.write(f"Population: {population_per_zone[zone]}")
#         st.write(f"Food Kits: {food_allocation[zone]}")
#         st.write(f"Medicinal Kits: {med_allocation[zone]}")
#         st.write(f"Clothes: {clothes_allocation[zone]}")
#         st.write("---")
    
#     # ---------- Display Warnings ----------
#     def show_warning(delayed_list, resource_name):
#         if delayed_list:
#             st.warning(
#                 f"⚠️ Regions receiving delayed {resource_name} due to higher priority elsewhere: "
#                 + ", ".join(delayed_list)
#             )
    
#     show_warning(delayed_food, "Food Kits")
#     show_warning(delayed_med, "Medicinal Kits")
#     show_warning(delayed_clothes, "Clothes")
    
#     # ---------- Map Visualization ----------
#     # Dummy coordinates for demonstration
#     locations_coords = {
#         'Center A': (12.97, 77.59),
#         'Center B': (12.98, 77.58),
#         'Center C': (12.96, 77.57),
#         'Zone 1': (12.99, 77.60),
#         'Zone 2': (12.95, 77.61),
#         'Zone 3': (12.94, 77.59),
#         'Zone 4': (12.93, 77.60),
#         'Zone 5': (12.92, 77.58)
#     }
    
#     route_map = plot_routes(routes, locations_coords)
#     st.subheader("Map Visualization")
#     st_folium(route_map, width=700, height=500)










#4
# import streamlit as st
# from routing import create_graph, get_routes
# from allocation import allocate_by_user_priority
# from visualization import plot_routes
# from streamlit_folium import st_folium

# # ---------- Data ----------
# edges_file = 'data/edges.csv'
# G = create_graph(edges_file)

# relief_centers = ['Center A', 'Center B', 'Center C']
# affected_zones = ['Zone 1', 'Zone 2', 'Zone 3', 'Zone 4', 'Zone 5']

# # ---------- Streamlit UI ----------
# st.title("Disaster Relief Routing & User-Defined Priority Allocation")

# origin = st.selectbox("Select Relief Center (Origin):", relief_centers)

# st.subheader("Enter Population for Each Affected Zone")
# population_per_zone = {}
# for zone in affected_zones:
#     population_per_zone[zone] = st.number_input(f'Population in {zone}:', min_value=1, value=100)

# st.subheader("Define Priority Order for Resource Allocation")

# # User-defined priority selection
# remaining_zones = affected_zones.copy()
# priority_order = []

# for i in range(1, len(affected_zones) + 1):
#     zone = st.selectbox(f"Select priority #{i}", remaining_zones)
#     priority_order.append(zone)
#     remaining_zones.remove(zone)

# st.write("Final allocation order:", priority_order)

# st.subheader("Enter Total Resources Available")
# total_food_kits = st.number_input("Total Food Kits:", min_value=0, value=500)
# total_medicinal_kits = st.number_input("Total Medicinal Kits:", min_value=0, value=200)
# total_clothes = st.number_input("Total Clothes:", min_value=0, value=300)

# if st.button("Submit"):
#     # ---------- Routing ----------
#     routes = get_routes(G, origin, affected_zones)
    
#     # ---------- Resource Allocation ----------
#     food_allocation, delayed_food = allocate_by_user_priority(
#         total_food_kits, population_per_zone, priority_order
#     )
#     med_allocation, delayed_med = allocate_by_user_priority(
#         total_medicinal_kits, population_per_zone, priority_order
#     )
#     clothes_allocation, delayed_clothes = allocate_by_user_priority(
#         total_clothes, population_per_zone, priority_order
#     )
    
#     # ---------- Display Results ----------
#     st.subheader("Routing & Resource Allocation")
#     for zone in affected_zones:
#         st.write(f"**{zone}**")
#         st.write(f"Route: {' → '.join(routes[zone])}")
#         st.write(f"Population: {population_per_zone[zone]}")
#         st.write(f"Food Kits: {food_allocation[zone]}")
#         st.write(f"Medicinal Kits: {med_allocation[zone]}")
#         st.write(f"Clothes: {clothes_allocation[zone]}")
#         st.write("---")
    
#     # ---------- Warnings for Delays ----------
#     def show_warning(delayed_list, resource_name):
#         if delayed_list:
#             st.warning(
#                 f"⚠️ Some regions may experience delays for {resource_name}: "
#                 + ", ".join(delayed_list)
#             )
    
#     show_warning(delayed_food, "Food Kits")
#     show_warning(delayed_med, "Medicinal Kits")
#     show_warning(delayed_clothes, "Clothes")
    
#     # ---------- Map Visualization ----------
#     # Dummy coordinates for demonstration
#     locations_coords = {
#         'Center A': (12.97, 77.59),
#         'Center B': (12.98, 77.58),
#         'Center C': (12.96, 77.57),
#         'Zone 1': (12.99, 77.60),
#         'Zone 2': (12.95, 77.61),
#         'Zone 3': (12.94, 77.59),
#         'Zone 4': (12.93, 77.60),
#         'Zone 5': (12.92, 77.58)
#     }
    
#     route_map = plot_routes(routes, locations_coords)
#     st.subheader("Map Visualization")
#     st_folium(route_map, width=700, height=500)






#5
# import streamlit as st
# from routing import create_graph, get_routes
# from allocation import allocate_by_user_priority
# from visualization import plot_routes
# from streamlit_folium import st_folium

# # ---------- Data ----------
# edges_file = 'data/edges.csv'
# G = create_graph(edges_file)

# relief_centers = ['Center A', 'Center B', 'Center C']
# affected_zones = ['Zone 1', 'Zone 2', 'Zone 3', 'Zone 4', 'Zone 5']

# # ---------- Streamlit UI ----------
# st.title("Disaster Relief Routing & User-Defined Priority Allocation")

# origin = st.selectbox("Select Relief Center (Origin):", relief_centers)

# st.subheader("Enter Population for Each Affected Zone")
# population_per_zone = {}
# for zone in affected_zones:
#     population_per_zone[zone] = st.number_input(f'Population in {zone}:', min_value=1, value=100)

# st.subheader("Define Priority Order for Resource Allocation")
# remaining_zones = affected_zones.copy()
# priority_order = []

# for i in range(1, len(affected_zones) + 1):
#     zone = st.selectbox(f"Select priority #{i}", remaining_zones)
#     priority_order.append(zone)
#     remaining_zones.remove(zone)

# st.write("Final allocation order:", priority_order)

# st.subheader("Enter Total Resources Available")
# total_food_kits = st.number_input("Total Food Kits:", min_value=0, value=500)
# total_medicinal_kits = st.number_input("Total Medicinal Kits:", min_value=0, value=200)
# total_clothes = st.number_input("Total Clothes:", min_value=0, value=300)

# if st.button("Submit"):
#     # ---------- Routing ----------
#     routes = get_routes(G, origin, affected_zones)
    
#     # ---------- Resource Allocation ----------
#     food_allocation, delayed_food = allocate_by_user_priority(
#         total_food_kits, population_per_zone, priority_order
#     )
#     med_allocation, delayed_med = allocate_by_user_priority(
#         total_medicinal_kits, population_per_zone, priority_order
#     )
#     clothes_allocation, delayed_clothes = allocate_by_user_priority(
#         total_clothes, population_per_zone, priority_order
#     )
    
#     # ---------- Display Results ----------
#     st.subheader("Routing & Resource Allocation (Priority Order)")
#     for zone in priority_order:
#         st.write(f"**{zone}**")
#         st.write(f"Route: {' → '.join(routes[zone])}")
#         st.write(f"Population: {population_per_zone[zone]}")
#         st.write(f"Food Kits: {food_allocation[zone]}")
#         st.write(f"Medicinal Kits: {med_allocation[zone]}")
#         st.write(f"Clothes: {clothes_allocation[zone]}")
#         st.write("---")
    
#     # ---------- Warnings for Delays ----------
#     def show_warning(delayed_list, resource_name):
#         if delayed_list:
#             st.warning(
#                 f"⚠️ Some regions may experience delays for {resource_name}: "
#                 + ", ".join(delayed_list)
#             )
    
#     show_warning(delayed_food, "Food Kits")
#     show_warning(delayed_med, "Medicinal Kits")
#     show_warning(delayed_clothes, "Clothes")
    
#     # ---------- Map Visualization ----------
#     # Dummy coordinates for demonstration
#     locations_coords = {
#         'Center A': (12.97, 77.59),
#         'Center B': (12.98, 77.58),
#         'Center C': (12.96, 77.57),
#         'Zone 1': (12.99, 77.60),
#         'Zone 2': (12.95, 77.61),
#         'Zone 3': (12.94, 77.59),
#         'Zone 4': (12.93, 77.60),
#         'Zone 5': (12.92, 77.58)
#     }
    
#     route_map = plot_routes(routes, locations_coords)
#     st.subheader("Map Visualization")
#     st_folium(route_map, width=700, height=500)







#6 updated for checkbox-based priority selection)
# import streamlit as st
# from routing import create_graph, get_routes
# from allocation import allocate_by_user_priority
# from visualization import plot_routes
# from streamlit_folium import st_folium

# # ---------- Data ----------
# edges_file = 'data/edges.csv'
# G = create_graph(edges_file)

# relief_centers = ['Center A', 'Center B', 'Center C']
# affected_zones = ['Zone 1', 'Zone 2', 'Zone 3', 'Zone 4', 'Zone 5']

# # ---------- Streamlit UI ----------
# st.title("Disaster Relief Routing & Checkbox-Based Priority Allocation")

# origin = st.selectbox("Select Relief Center (Origin):", relief_centers)

# st.subheader("Enter Population for Each Affected Zone")
# population_per_zone = {}
# for zone in affected_zones:
#     population_per_zone[zone] = st.number_input(f'Population in {zone}:', min_value=1, value=100)

# st.subheader("Select Affected Zones (Order Determines Priority)")
# selected_zones = []

# # Track selection order
# for zone in affected_zones:
#     if st.checkbox(zone):
#         selected_zones.append(zone)

# if not selected_zones:
#     st.warning("Please select at least one zone for allocation.")

# st.subheader("Enter Total Resources Available")
# total_food_kits = st.number_input("Total Food Kits:", min_value=0, value=500)
# total_medicinal_kits = st.number_input("Total Medicinal Kits:", min_value=0, value=200)
# total_clothes = st.number_input("Total Clothes:", min_value=0, value=300)

# if st.button("Submit") and selected_zones:
#     # ---------- Routing ----------
#     routes = get_routes(G, origin, selected_zones)
    
#     # ---------- Resource Allocation ----------
#     food_allocation, delayed_food = allocate_by_user_priority(
#         total_food_kits,
#         {zone: population_per_zone[zone] for zone in selected_zones},
#         selected_zones
#     )
#     med_allocation, delayed_med = allocate_by_user_priority(
#         total_medicinal_kits,
#         {zone: population_per_zone[zone] for zone in selected_zones},
#         selected_zones
#     )
#     clothes_allocation, delayed_clothes = allocate_by_user_priority(
#         total_clothes,
#         {zone: population_per_zone[zone] for zone in selected_zones},
#         selected_zones
#     )
    
#     # ---------- Display Results ----------
#     st.subheader("Routing & Resource Allocation (Selected Zones Only)")
#     for zone in selected_zones:
#         st.write(f"**{zone}**")
#         st.write(f"Route: {' → '.join(routes[zone])}")
#         st.write(f"Population: {population_per_zone[zone]}")
#         st.write(f"Food Kits: {food_allocation[zone]}")
#         st.write(f"Medicinal Kits: {med_allocation[zone]}")
#         st.write(f"Clothes: {clothes_allocation[zone]}")
#         st.write("---")
    
#     # ---------- Warnings for Delays ----------
#     def show_warning(delayed_list, resource_name):
#         if delayed_list:
#             st.warning(
#                 f"⚠️ Some selected regions may experience delays for {resource_name}: "
#                 + ", ".join(delayed_list)
#             )
    
#     show_warning(delayed_food, "Food Kits")
#     show_warning(delayed_med, "Medicinal Kits")
#     show_warning(delayed_clothes, "Clothes")
    
#     # ---------- Map Visualization ----------
#     # Dummy coordinates for demonstration
#     locations_coords = {
#         'Center A': (12.97, 77.59),
#         'Center B': (12.98, 77.58),
#         'Center C': (12.96, 77.57),
#         'Zone 1': (12.99, 77.60),
#         'Zone 2': (12.95, 77.61),
#         'Zone 3': (12.94, 77.59),
#         'Zone 4': (12.93, 77.60),
#         'Zone 5': (12.92, 77.58)
#     }
    
#     route_map = plot_routes(routes, locations_coords)
#     st.subheader("Map Visualization")
#     st_folium(route_map, width=700, height=500)











#7 updated for selection-first, population-second, priority-based allocation + working non dynamic
# import streamlit as st
# from routing import create_graph, get_routes
# from allocation import allocate_by_user_priority
# from visualization import plot_routes
# from streamlit_folium import st_folium

# # ---------- Data ----------
# edges_file = 'data/edges.csv'
# G = create_graph(edges_file)

# relief_centers = ['Center A', 'Center B', 'Center C']
# affected_zones = ['Zone 1', 'Zone 2', 'Zone 3', 'Zone 4', 'Zone 5']

# st.title("Disaster Relief Routing & Checkbox-Based Priority Allocation")

# # ---------- Initialize session state to track selection order ----------
# if 'selected_order' not in st.session_state:
#     st.session_state.selected_order = []

# # Function to handle checkbox click
# def checkbox_callback(zone):
#     if st.session_state[zone]:
#         if zone not in st.session_state.selected_order:
#             st.session_state.selected_order.append(zone)
#     else:
#         if zone in st.session_state.selected_order:
#             st.session_state.selected_order.remove(zone)

# # ---------- Step 1: Select Affected Zones ----------
# st.subheader("Select Affected Zones (Order of Selection Determines Priority)")

# for zone in affected_zones:
#     st.checkbox(
#         zone,
#         key=zone,
#         value=zone in st.session_state.selected_order,
#         on_change=checkbox_callback,
#         args=(zone,)
#     )

# selected_zones = st.session_state.selected_order.copy()

# if not selected_zones:
#     st.warning("Please select at least one zone for allocation.")

# # ---------- Step 2: Input Population for Selected Zones ----------
# population_per_zone = {}
# if selected_zones:
#     st.subheader("Enter Population for Selected Zones")
#     for zone in selected_zones:
#         population_per_zone[zone] = st.number_input(f'Population in {zone}:', min_value=1, value=100, key=f'pop_{zone}')

# # ---------- Step 3: Total Resources ----------
# st.subheader("Enter Total Resources Available")
# total_food_kits = st.number_input("Total Food Kits:", min_value=0, value=500)
# total_medicinal_kits = st.number_input("Total Medicinal Kits:", min_value=0, value=200)
# total_clothes = st.number_input("Total Clothes:", min_value=0, value=300)

# # ---------- Step 4: Submit & Allocate ----------
# if st.button("Submit") and selected_zones:
#     # ---------- Routing ----------
#     routes = get_routes(G, origin='Center A', destinations=selected_zones)

#     # ---------- Resource Allocation ----------
#     food_allocation, delayed_food = allocate_by_user_priority(
#         total_food_kits,
#         population_per_zone,
#         selected_zones
#     )
#     med_allocation, delayed_med = allocate_by_user_priority(
#         total_medicinal_kits,
#         population_per_zone,
#         selected_zones
#     )
#     clothes_allocation, delayed_clothes = allocate_by_user_priority(
#         total_clothes,
#         population_per_zone,
#         selected_zones
#     )

#     # ---------- Step 5: Display Results in Selection Order ----------
#     st.subheader("Routing & Resource Allocation (Priority Order Based on Selection)")
#     for zone in selected_zones:
#         st.write(f"**{zone}**")
#         st.write(f"Route: {' → '.join(routes[zone])}")
#         st.write(f"Population: {population_per_zone[zone]}")
#         st.write(f"Food Kits: {food_allocation[zone]}")
#         st.write(f"Medicinal Kits: {med_allocation[zone]}")
#         st.write(f"Clothes: {clothes_allocation[zone]}")
#         st.write("---")

#     # ---------- Warnings ----------
#     def show_warning(delayed_list, resource_name):
#         if delayed_list:
#             st.warning(
#                 f"⚠️ Some selected regions may experience delays for {resource_name}: "
#                 + ", ".join(delayed_list)
#             )

#     show_warning(delayed_food, "Food Kits")
#     show_warning(delayed_med, "Medicinal Kits")
#     show_warning(delayed_clothes, "Clothes")

#     # ---------- Map Visualization ----------
#     # Dummy coordinates for demonstration
#     locations_coords = {
#         'Center A': (12.97, 77.59),
#         'Center B': (12.98, 77.58),
#         'Center C': (12.96, 77.57),
#         'Zone 1': (12.99, 77.60),
#         'Zone 2': (12.95, 77.61),
#         'Zone 3': (12.94, 77.59),
#         'Zone 4': (12.93, 77.60),
#         'Zone 5': (12.92, 77.58)
#     }

#     route_map = plot_routes(routes, locations_coords)
#     st.subheader("Map Visualization")
#     st_folium(route_map, width=700, height=500)








#8 realistic dataimport streamlit as st
# import streamlit as st
# from allocation import allocate_by_user_priority
# from routing import create_graph, get_routes
# from visualization import plot_routes
# from streamlit_folium import st_folium

# # -------------------- Graph Setup --------------------
# edges_file = 'data/edges.csv'
# G = create_graph(edges_file)

# # -------------------- Relief Centers & Zones --------------------
# relief_centers = [
#     'Guwahati Relief Depot',
#     'Tezpur Relief Center',
#     'Dibrugarh Relief Hub'
# ]

# all_zones = [
#     'Jorhat',
#     'Lakhimpur',
#     'Morigaon',
#     'Dhemaji',
#     'Sivasagar'
# ]

# locations_coords = {
#     'Guwahati Relief Depot': (26.1445, 91.7362),
#     'Tezpur Relief Center': (26.6335, 92.8031),
#     'Dibrugarh Relief Hub': (27.4728, 94.9111),
#     'Jorhat': (26.7467, 94.2033),
#     'Lakhimpur': (27.2333, 94.1167),
#     'Morigaon': (26.3833, 92.4833),
#     'Dhemaji': (27.4833, 94.5833),
#     'Sivasagar': (26.9800, 94.6470)
# }

# st.title("Disaster Relief Routing & Allocation - Checkbox Priority")

# # -------------------- Initialize Session State --------------------
# if 'selected_order' not in st.session_state:
#     st.session_state.selected_order = []

# # -------------------- Checkbox Priority Selection --------------------
# def checkbox_callback(zone):
#     """Track selection order dynamically"""
#     if st.session_state[zone]:
#         if zone not in st.session_state.selected_order:
#             st.session_state.selected_order.append(zone)
#     else:
#         if zone in st.session_state.selected_order:
#             st.session_state.selected_order.remove(zone)

# st.subheader("Select Affected Zones (Order of Selection = Priority)")
# for zone in all_zones:
#     st.checkbox(
#         zone,
#         key=zone,
#         value=zone in st.session_state.selected_order,
#         on_change=checkbox_callback,
#         args=(zone,)
#     )

# selected_zones = st.session_state.selected_order.copy()

# if not selected_zones:
#     st.warning("Please select at least one zone to continue.")

# # -------------------- Population Input --------------------
# population_per_zone = {}
# if selected_zones:
#     st.subheader("Enter Population for Selected Zones")
#     for zone in selected_zones:
#         population_per_zone[zone] = st.number_input(
#             f"Population in {zone}:",
#             min_value=1,
#             value=100,
#             key=f'pop_{zone}'
#         )

# # -------------------- Resource Input --------------------
# st.subheader("Enter Total Resources Available")
# total_food = st.number_input("Total Food Kits:", min_value=0, value=500)
# total_medicine = st.number_input("Total Medicinal Kits:", min_value=0, value=200)
# total_clothes = st.number_input("Total Clothes:", min_value=0, value=300)

# # -------------------- Allocation & Routing --------------------
# if st.button("Allocate") and selected_zones:
#     # ---------------- Priority Order ----------------
#     # Priority strictly follows checkbox selection order
#     priority_order = selected_zones

#     # ---------------- Routing ----------------
#     # For simplicity, all allocations originate from Guwahati Relief Depot
#     routes = get_routes(G, origin='Guwahati Relief Depot', destinations=priority_order)

#     # ---------------- Resource Allocation ----------------
#     food_alloc, delayed_food = allocate_by_user_priority(total_food, population_per_zone, priority_order)
#     med_alloc, delayed_med = allocate_by_user_priority(total_medicine, population_per_zone, priority_order)
#     clothes_alloc, delayed_clothes = allocate_by_user_priority(total_clothes, population_per_zone, priority_order)

#     # ---------------- Display Results ----------------
#     st.subheader("Routing & Resource Allocation (Priority Order)")
#     for zone in priority_order:
#         st.write(f"**{zone}**")
#         st.write(f"Route: {' → '.join(routes[zone])}")
#         st.write(f"Population: {population_per_zone[zone]}")
#         st.write(f"Food Kits: {food_alloc[zone]}")
#         st.write(f"Medicinal Kits: {med_alloc[zone]}")
#         st.write(f"Clothes: {clothes_alloc[zone]}")
#         st.write("---")

#     # ---------------- Delayed Warnings ----------------
#     def show_warning(delayed, resource_name):
#         if delayed:
#             st.warning(f"⚠️ Delay in {resource_name} for: " + ", ".join(delayed))

#     show_warning(delayed_food, "Food Kits")
#     show_warning(delayed_med, "Medicinal Kits")
#     show_warning(delayed_clothes, "Clothes")

#     # ---------------- Map Visualization ----------------
#     route_map = plot_routes(routes, locations_coords)
#     st.subheader("Map of Routes")
#     st_folium(route_map, width=700, height=500)











#9 working but route not found
# import streamlit as st
# from streamlit_folium import st_folium
# import folium
# import networkx as nx

# # -------------------------------------------------------------
# # OSM PARSER (embedded version of read_pbf.py)
# # -------------------------------------------------------------
# import osmium

# class OSMParser(osmium.SimpleHandler):
#     def __init__(self):
#         super().__init__()
#         self.nodes = {}        # node_id → (lat, lon)
#         self.named_nodes = {}  # name → node_id
#         self.graph = nx.Graph()

#     def node(self, n):
#         if not n.location.valid():
#             return
        
#         lat, lon = n.location.lat, n.location.lon
#         self.nodes[n.id] = (lat, lon)

#         name = n.tags.get("name")
#         if name:
#             self.named_nodes[name] = n.id

#     def way(self, w):
#         # Use only ways that represent roads
#         if "highway" in w.tags and len(w.nodes) > 1:
#             for i in range(len(w.nodes) - 1):
#                 n1 = w.nodes[i].ref
#                 n2 = w.nodes[i + 1].ref

#                 if n1 in self.nodes and n2 in self.nodes:
#                     self.graph.add_edge(n1, n2)


# def parse_osm_pbf(pbf_file):
#     parser = OSMParser()
#     parser.apply_file(pbf_file)
#     return parser.nodes, parser.named_nodes, parser.graph

# # -------------------------------------------------------------
# # ALLOCATION LOGIC (unchanged)
# # -------------------------------------------------------------
# def allocate_by_user_priority(total_resources, population_dict, priority_order):
#     allocation = {zone: 0 for zone in population_dict}
#     remaining = total_resources
#     delayed_zones = []

#     for zone in priority_order:
#         needed = population_dict[zone]
#         alloc = min(needed, remaining)
#         allocation[zone] = alloc
#         remaining -= alloc

#         if alloc < needed:
#             delayed_zones.append(zone)

#         if remaining <= 0:
#             continue

#     return allocation, delayed_zones

# # -------------------------------------------------------------
# # STREAMLIT APP
# # -------------------------------------------------------------
# st.title("🗺️ Disaster Relief Routing & Priority-Based Resource Allocation (OSM Integrated)")

# # -------------------------------------------------------------
# # Step 0: Upload OSM PBF
# # -------------------------------------------------------------
# uploaded_file = st.file_uploader("Upload an .osm.pbf file", type=["pbf", "osm.pbf"])

# if uploaded_file is None:
#     st.info("Please upload an OSM .pbf map file to begin.")
#     st.stop()

# # Save uploaded file temporarily
# with open("uploaded.osm.pbf", "wb") as f:
#     f.write(uploaded_file.read())

# st.success("OSM file uploaded successfully. Parsing...")

# # Parse OSM
# nodes, named_nodes, osm_graph = parse_osm_pbf("uploaded.osm.pbf")

# if len(named_nodes) == 0:
#     st.error("No named places found in this OSM file.")
#     st.stop()

# place_names = sorted(list(named_nodes.keys()))

# st.success(f"Parsed {len(nodes)} nodes, {len(named_nodes)} named locations.")

# # -------------------------------------------------------------
# # Step 1: Select regions using real OSM names
# # -------------------------------------------------------------
# st.subheader("Select Affected Zones (Order Determines Priority)")

# # Tracking selection order
# if 'selected_order' not in st.session_state:
#     st.session_state.selected_order = []

# # Checkbox callback
# def checkbox_callback(zone):
#     if st.session_state[zone]:
#         if zone not in st.session_state.selected_order:
#             st.session_state.selected_order.append(zone)
#     else:
#         if zone in st.session_state.selected_order:
#             st.session_state.selected_order.remove(zone)

# # Show checkboxes for all place names
# for zone in place_names:
#     st.checkbox(
#         zone, 
#         key=zone,
#         value=zone in st.session_state.selected_order,
#         on_change=checkbox_callback,
#         args=(zone,)
#     )

# selected_zones = st.session_state.selected_order.copy()

# if not selected_zones:
#     st.warning("Please select at least one affected location.")
#     st.stop()

# # -------------------------------------------------------------
# # Step 2: Select Origin (Relief Center)
# # -------------------------------------------------------------
# st.subheader("Select Origin (Relief Center)")

# origin = st.selectbox("Origin point:", place_names)

# origin_node = named_nodes[origin]
# destination_nodes = [named_nodes[z] for z in selected_zones]

# # -------------------------------------------------------------
# # Step 3: Populations
# # -------------------------------------------------------------
# st.subheader("Enter Population for Selected Affected Zones")

# population_per_zone = {}
# for zone in selected_zones:
#     population_per_zone[zone] = st.number_input(
#         f"Population in {zone}:",
#         min_value=1,
#         value=100,
#         key=f"pop_{zone}"
#     )

# # -------------------------------------------------------------
# # Step 4: Resources
# # -------------------------------------------------------------
# st.subheader("Enter Total Resources Available")

# total_food_kits = st.number_input("Total Food Kits:", min_value=0, value=500)
# total_medicinal_kits = st.number_input("Total Medicinal Kits:", min_value=0, value=200)
# total_clothes = st.number_input("Total Clothes:", min_value=0, value=300)

# # -------------------------------------------------------------
# # Step 5: Submit
# # -------------------------------------------------------------
# if st.button("Submit"):

#     # ----------- Routing -----------
#     st.subheader("Routing")

#     routes = {}
#     routes_coords = {}

#     for zone, dest_node in zip(selected_zones, destination_nodes):
#         try:
#             path_nodes = nx.shortest_path(osm_graph, origin_node, dest_node)
#             routes[zone] = path_nodes
#             routes_coords[zone] = [nodes[n] for n in path_nodes]
#         except:
#             routes[zone] = None
#             routes_coords[zone] = []

#     # ----------- Allocation -----------
#     food_alloc, delayed_food = allocate_by_user_priority(total_food_kits, population_per_zone, selected_zones)
#     med_alloc, delayed_med = allocate_by_user_priority(total_medicinal_kits, population_per_zone, selected_zones)
#     clothes_alloc, delayed_clothes = allocate_by_user_priority(total_clothes, population_per_zone, selected_zones)

#     # ----------- Display Results -----------
#     st.subheader("Results (in Selection Priority Order)")

#     for zone in selected_zones:
#         st.write(f"### {zone}")
#         st.write(f"Population: {population_per_zone[zone]}")
#         st.write(f"Food Kits: {food_alloc[zone]}")
#         st.write(f"Medicinal Kits: {med_alloc[zone]}")
#         st.write(f"Clothes: {clothes_alloc[zone]}")
#         st.write("Route:")

#         if routes_coords[zone]:
#             st.write(" → ".join([str(n) for n in routes[zone]]))
#         else:
#             st.error("No route found.")

#         st.write("---")

#     # ----------- Warnings -----------
#     def warn(list_delayed, name):
#         if list_delayed:
#             st.warning(f"⚠ Some areas may face delays in {name}: {', '.join(list_delayed)}")

#     warn(delayed_food, "Food Kits")
#     warn(delayed_med, "Medicinal Kits")
#     warn(delayed_clothes, "Clothes")

#     # ----------- Map -----------
#     st.subheader("Map Visualization")

#     # Center map at origin
#     origin_lat, origin_lon = nodes[origin_node]
#     m = folium.Map(location=[origin_lat, origin_lon], zoom_start=14)

#     # Draw each route
#     for zone in selected_zones:
#         coords = routes_coords[zone]
#         if coords:
#             folium.PolyLine(coords, color='blue', weight=3).add_to(m)
#             folium.Marker(coords[-1], popup=zone).add_to(m)

#     st_folium(m, width=800, height=600)




















#10 working dynamic but result disappear
# import streamlit as st
# from streamlit_folium import st_folium
# import folium
# import networkx as nx
# import numpy as np
# from sklearn.cluster import DBSCAN
# import osmium

# # -------------------------------------------------------------
# # OSM Parser (same as before)
# # -------------------------------------------------------------
# class OSMParser(osmium.SimpleHandler):
#     def __init__(self):
#         super().__init__()
#         self.nodes = {}        # node_id → (lat, lon)
#         self.named_nodes = {}  # name → node_id
#         self.graph = nx.Graph()

#     def node(self, n):
#         if not n.location.valid():
#             return
#         lat, lon = n.location.lat, n.location.lon
#         self.nodes[n.id] = (lat, lon)
#         name = n.tags.get("name")
#         if name:
#             self.named_nodes[name] = n.id

#     def way(self, w):
#         if "highway" in w.tags and len(w.nodes) > 1:
#             for i in range(len(w.nodes) - 1):
#                 n1, n2 = w.nodes[i].ref, w.nodes[i+1].ref
#                 if n1 in self.nodes and n2 in self.nodes:
#                     self.graph.add_edge(n1, n2)

# def parse_osm_pbf(pbf_file):
#     parser = OSMParser()
#     parser.apply_file(pbf_file)
#     return parser.nodes, parser.named_nodes, parser.graph

# # -------------------------------------------------------------
# # Allocation (unchanged)
# # -------------------------------------------------------------
# def allocate_by_user_priority(total_resources, population_dict, priority_order):
#     allocation = {zone: 0 for zone in population_dict}
#     remaining = total_resources
#     delayed_zones = []
#     for zone in priority_order:
#         needed = population_dict[zone]
#         alloc = min(needed, remaining)
#         allocation[zone] = alloc
#         remaining -= alloc
#         if alloc < needed:
#             delayed_zones.append(zone)
#         if remaining <= 0:
#             continue
#     return allocation, delayed_zones

# # -------------------------------------------------------------
# # Streamlit UI
# # -------------------------------------------------------------
# st.title("🗺️ Clustered Disaster Relief Routing")

# # Upload OSM PBF
# uploaded_file = st.file_uploader("Upload .osm.pbf", type=["pbf", "osm.pbf"])
# if uploaded_file is None:
#     st.info("Please upload an OSM .pbf map file to begin.")
#     st.stop()

# with open("uploaded.osm.pbf", "wb") as f:
#     f.write(uploaded_file.read())

# nodes, named_nodes, osm_graph = parse_osm_pbf("uploaded.osm.pbf")

# if len(named_nodes) == 0:
#     st.error("No named places found in this OSM file.")
#     st.stop()

# # -------------------------------------------------------------
# # Cluster nodes dynamically using DBSCAN
# # -------------------------------------------------------------
# coords = np.array([nodes[n] for n in named_nodes.values()])
# node_ids = list(named_nodes.values())
# clustering = DBSCAN(eps=0.01, min_samples=2).fit(coords)  # eps ~ 0.01 degrees ≈ 1 km
# labels = clustering.labels_

# clusters = {}
# for label, nid in zip(labels, node_ids):
#     clusters.setdefault(label, []).append(nid)

# # Map cluster label to place names
# cluster_name_map = {}
# for lbl, nids in clusters.items():
#     cluster_name_map[lbl] = [name for name, nid in named_nodes.items() if nid in nids]

# # Step 1: Select cluster
# selected_cluster = st.selectbox(
#     "Select a cluster (group of nearby cities):",
#     options=[lbl for lbl in cluster_name_map.keys() if lbl != -1],  # -1 is noise
#     format_func=lambda x: f"Cluster {x} ({len(cluster_name_map[x])} nodes)"
# )

# cluster_nodes = cluster_name_map[selected_cluster]

# # Step 2: Select origin and destinations
# st.subheader("Select Origin & Destinations within Cluster")
# origin = st.selectbox("Origin", options=cluster_nodes)
# destinations = st.multiselect("Destinations", options=[n for n in cluster_nodes if n != origin])

# if not origin or len(destinations) == 0:
#     st.warning("Please select origin and at least one destination.")
#     st.stop()

# # Step 3: Populations
# st.subheader("Enter Population for Destinations")
# population_per_zone = {}
# for zone in destinations:
#     population_per_zone[zone] = st.number_input(f"Population in {zone}:", min_value=1, value=100, key=f"pop_{zone}")

# # Step 4: Resources
# st.subheader("Enter Total Resources Available")
# total_food_kits = st.number_input("Total Food Kits:", min_value=0, value=500)
# total_medicinal_kits = st.number_input("Total Medicinal Kits:", min_value=0, value=200)
# total_clothes = st.number_input("Total Clothes:", min_value=0, value=300)

# # Step 5: Compute routing
# if st.button("Compute Routes & Allocate"):
#     origin_node = named_nodes[origin]
#     dest_nodes = [named_nodes[d] for d in destinations]

#     routes = {}
#     routes_coords = {}
#     for dest_name, dest_node in zip(destinations, dest_nodes):
#         try:
#             path_nodes = nx.shortest_path(osm_graph, origin_node, dest_node)
#             routes[dest_name] = path_nodes
#             routes_coords[dest_name] = [nodes[n] for n in path_nodes]
#         except:
#             routes[dest_name] = None
#             routes_coords[dest_name] = []

#     # Resource allocation
#     food_alloc, delayed_food = allocate_by_user_priority(total_food_kits, population_per_zone, destinations)
#     med_alloc, delayed_med = allocate_by_user_priority(total_medicinal_kits, population_per_zone, destinations)
#     clothes_alloc, delayed_clothes = allocate_by_user_priority(total_clothes, population_per_zone, destinations)

#     # Display results
#     st.subheader("Results")
#     for zone in destinations:
#         st.write(f"### {zone}")
#         st.write(f"Population: {population_per_zone[zone]}")
#         st.write(f"Food Kits: {food_alloc[zone]}")
#         st.write(f"Medicinal Kits: {med_alloc[zone]}")
#         st.write(f"Clothes: {clothes_alloc[zone]}")
#         st.write("Route:", " → ".join([str(n) for n in routes.get(zone, [])]) if routes.get(zone) else "No route found")
#         st.write("---")

#     # Warnings
#     def warn(lst, res):
#         if lst:
#             st.warning(f"⚠ Some areas may face delays in {res}: {', '.join(lst)}")

#     warn(delayed_food, "Food Kits")
#     warn(delayed_med, "Medicinal Kits")
#     warn(delayed_clothes, "Clothes")

#     # Map
#     st.subheader("Map Visualization")
#     origin_lat, origin_lon = nodes[origin_node]
#     m = folium.Map(location=[origin_lat, origin_lon], zoom_start=13)

#     for zone in destinations:
#         coords = routes_coords[zone]
#         if coords:
#             folium.PolyLine(coords, color='blue', weight=3).add_to(m)
#             folium.Marker(coords[-1], popup=zone).add_to(m)

#     st_folium(m, width=800, height=600)


















#11
# import streamlit as st
# from streamlit_folium import st_folium
# import folium
# import networkx as nx
# import numpy as np
# from sklearn.cluster import DBSCAN
# import osmium

# # -------------------------------------------------------------
# # OSM Parser
# # -------------------------------------------------------------
# class OSMParser(osmium.SimpleHandler):
#     def __init__(self):
#         super().__init__()
#         self.nodes = {}        # node_id → (lat, lon)
#         self.named_nodes = {}  # name → node_id
#         self.graph = nx.Graph()

#     def node(self, n):
#         if not n.location.valid():
#             return
#         lat, lon = n.location.lat, n.location.lon
#         self.nodes[n.id] = (lat, lon)
#         name = n.tags.get("name")
#         if name:
#             self.named_nodes[name] = n.id

#     def way(self, w):
#         if "highway" in w.tags and len(w.nodes) > 1:
#             for i in range(len(w.nodes) - 1):
#                 n1, n2 = w.nodes[i].ref, w.nodes[i+1].ref
#                 if n1 in self.nodes and n2 in self.nodes:
#                     self.graph.add_edge(n1, n2)

# def parse_osm_pbf(pbf_file):
#     parser = OSMParser()
#     parser.apply_file(pbf_file)
#     return parser.nodes, parser.named_nodes, parser.graph

# # -------------------------------------------------------------
# # Allocation logic
# # -------------------------------------------------------------
# def allocate_by_user_priority(total_resources, population_dict, priority_order):
#     allocation = {zone: 0 for zone in population_dict}
#     remaining = total_resources
#     delayed_zones = []
#     for zone in priority_order:
#         needed = population_dict[zone]
#         alloc = min(needed, remaining)
#         allocation[zone] = alloc
#         remaining -= alloc
#         if alloc < needed:
#             delayed_zones.append(zone)
#         if remaining <= 0:
#             continue
#     return allocation, delayed_zones

# # -------------------------------------------------------------
# # Streamlit App
# # -------------------------------------------------------------
# st.title("🗺️ Clustered Disaster Relief Routing with Persistent Results")

# # -------------------------------------------------------------
# # Step 0: Upload OSM PBF
# # -------------------------------------------------------------
# uploaded_file = st.file_uploader("Upload an .osm.pbf file", type=["pbf", "osm.pbf"])
# if uploaded_file is None:
#     st.info("Please upload an OSM .pbf map file to begin.")
#     st.stop()

# with open("uploaded.osm.pbf", "wb") as f:
#     f.write(uploaded_file.read())

# nodes, named_nodes, osm_graph = parse_osm_pbf("uploaded.osm.pbf")

# if len(named_nodes) == 0:
#     st.error("No named places found in this OSM file.")
#     st.stop()

# # -------------------------------------------------------------
# # Cluster nodes dynamically using DBSCAN
# # -------------------------------------------------------------
# coords = np.array([nodes[n] for n in named_nodes.values()])
# node_ids = list(named_nodes.values())
# clustering = DBSCAN(eps=0.01, min_samples=2).fit(coords)
# labels = clustering.labels_

# clusters = {}
# for label, nid in zip(labels, node_ids):
#     clusters.setdefault(label, []).append(nid)

# cluster_name_map = {}
# for lbl, nids in clusters.items():
#     cluster_name_map[lbl] = [name for name, nid in named_nodes.items() if nid in nids]

# # Step 1: Select cluster
# selected_cluster = st.selectbox(
#     "Select a cluster (group of nearby cities):",
#     options=[lbl for lbl in cluster_name_map.keys() if lbl != -1],
#     format_func=lambda x: f"Cluster {x} ({len(cluster_name_map[x])} nodes)"
# )

# cluster_nodes = cluster_name_map[selected_cluster]

# # Step 2: Select origin and destinations
# st.subheader("Select Origin & Destinations within Cluster")
# origin = st.selectbox("Origin", options=cluster_nodes)
# destinations = st.multiselect("Destinations", options=[n for n in cluster_nodes if n != origin])

# if not origin or len(destinations) == 0:
#     st.warning("Please select origin and at least one destination.")
#     st.stop()

# # Step 3: Populations
# st.subheader("Enter Population for Destinations")
# population_per_zone = {}
# for zone in destinations:
#     population_per_zone[zone] = st.number_input(f"Population in {zone}:", min_value=1, value=100, key=f"pop_{zone}")

# # Step 4: Resources
# st.subheader("Enter Total Resources Available")
# total_food_kits = st.number_input("Total Food Kits:", min_value=0, value=500)
# total_medicinal_kits = st.number_input("Total Medicinal Kits:", min_value=0, value=200)
# total_clothes = st.number_input("Total Clothes:", min_value=0, value=300)

# # -------------------------------------------------------------
# # Step 5: Compute routes & allocation (store in session_state)
# # -------------------------------------------------------------
# if st.button("Compute Routes & Allocate"):
#     origin_node = named_nodes[origin]
#     dest_nodes = [named_nodes[d] for d in destinations]

#     routes = {}
#     routes_coords = {}
#     for dest_name, dest_node in zip(destinations, dest_nodes):
#         try:
#             path_nodes = nx.shortest_path(osm_graph, origin_node, dest_node)
#             routes[dest_name] = path_nodes
#             routes_coords[dest_name] = [nodes[n] for n in path_nodes]
#         except:
#             routes[dest_name] = None
#             routes_coords[dest_name] = []

#     food_alloc, delayed_food = allocate_by_user_priority(total_food_kits, population_per_zone, destinations)
#     med_alloc, delayed_med = allocate_by_user_priority(total_medicinal_kits, population_per_zone, destinations)
#     clothes_alloc, delayed_clothes = allocate_by_user_priority(total_clothes, population_per_zone, destinations)

#     # Store in session_state
#     st.session_state['routes'] = routes
#     st.session_state['routes_coords'] = routes_coords
#     st.session_state['food_alloc'] = food_alloc
#     st.session_state['med_alloc'] = med_alloc
#     st.session_state['clothes_alloc'] = clothes_alloc
#     st.session_state['delayed_food'] = delayed_food
#     st.session_state['delayed_med'] = delayed_med
#     st.session_state['delayed_clothes'] = delayed_clothes
#     st.session_state['computed'] = True

# # -------------------------------------------------------------
# # Step 6: Display results from session_state
# # -------------------------------------------------------------
# if st.session_state.get('computed', False):
#     routes = st.session_state['routes']
#     routes_coords = st.session_state['routes_coords']
#     food_alloc = st.session_state['food_alloc']
#     med_alloc = st.session_state['med_alloc']
#     clothes_alloc = st.session_state['clothes_alloc']
#     delayed_food = st.session_state['delayed_food']
#     delayed_med = st.session_state['delayed_med']
#     delayed_clothes = st.session_state['delayed_clothes']

#     st.subheader("Results")
#     for zone in destinations:
#         st.write(f"### {zone}")
#         st.write(f"Population: {population_per_zone[zone]}")
#         st.write(f"Food Kits: {food_alloc[zone]}")
#         st.write(f"Medicinal Kits: {med_alloc[zone]}")
#         st.write(f"Clothes: {clothes_alloc[zone]}")
#         st.write("Route:", " → ".join([str(n) for n in routes.get(zone, [])]) if routes.get(zone) else "No route found")
#         st.write("---")

#     # Warnings
#     def warn(lst, res):
#         if lst:
#             st.warning(f"⚠ Some areas may face delays in {res}: {', '.join(lst)}")

#     warn(delayed_food, "Food Kits")
#     warn(delayed_med, "Medicinal Kits")
#     warn(delayed_clothes, "Clothes")

#     # Map visualization
#     st.subheader("Map Visualization")
#     origin_node = named_nodes[origin]
#     origin_lat, origin_lon = nodes[origin_node]
#     m = folium.Map(location=[origin_lat, origin_lon], zoom_start=13)

#     for zone in destinations:
#         coords = routes_coords[zone]
#         if coords:
#             folium.PolyLine(coords, color='blue', weight=3).add_to(m)
#             folium.Marker(coords[-1], popup=zone).add_to(m)

#     st_folium(m, width=800, height=600)











#12 all perfect without straight route
# import streamlit as st
# from streamlit_folium import st_folium
# import folium
# import networkx as nx
# import numpy as np
# from sklearn.cluster import DBSCAN
# import osmium
# from math import radians, cos, sin, sqrt, atan2

# # ---------------- Haversine function ----------------
# def haversine(lat1, lon1, lat2, lon2):
#     R = 6371000  # meters
#     phi1, phi2 = radians(lat1), radians(lat2)
#     dphi = radians(lat2 - lat1)
#     dlambda = radians(lon2 - lon1)
#     a = sin(dphi/2)**2 + cos(phi1)*cos(phi2)*sin(dlambda/2)**2
#     c = 2 * atan2(sqrt(a), sqrt(1-a))
#     return R * c

# # ---------------- OSM Parser ----------------
# class OSMParser(osmium.SimpleHandler):
#     def __init__(self):
#         super().__init__()
#         self.nodes = {}        # node_id → (lat, lon)
#         self.named_nodes = {}  # name → node_id
#         self.graph = nx.Graph()

#     def node(self, n):
#         if not n.location.valid():
#             return
#         lat, lon = n.location.lat, n.location.lon
#         self.nodes[n.id] = (lat, lon)
#         name = n.tags.get("name")
#         if name:
#             self.named_nodes[name] = n.id

#     def way(self, w):
#         if "highway" in w.tags and len(w.nodes) > 1:
#             for i in range(len(w.nodes) - 1):
#                 n1, n2 = w.nodes[i].ref, w.nodes[i+1].ref
#                 if n1 in self.nodes and n2 in self.nodes:
#                     lat1, lon1 = self.nodes[n1]
#                     lat2, lon2 = self.nodes[n2]
#                     weight = haversine(lat1, lon1, lat2, lon2)
#                     self.graph.add_edge(n1, n2, weight=weight)

# def parse_osm_pbf(pbf_file):
#     parser = OSMParser()
#     parser.apply_file(pbf_file)
#     return parser.nodes, parser.named_nodes, parser.graph

# # ---------------- Allocation logic ----------------
# def allocate_by_user_priority(total_resources, population_dict, priority_order):
#     allocation = {zone: 0 for zone in population_dict}
#     remaining = total_resources
#     delayed_zones = []
#     for zone in priority_order:
#         needed = population_dict[zone]
#         alloc = min(needed, remaining)
#         allocation[zone] = alloc
#         remaining -= alloc
#         if alloc < needed:
#             delayed_zones.append(zone)
#         if remaining <= 0:
#             continue
#     return allocation, delayed_zones

# # ---------------- Helper functions ----------------
# def nearest_graph_node(node_name, nodes, named_nodes, osm_graph):
#     nid = named_nodes[node_name]
#     lat, lon = nodes[nid]
#     min_dist = float('inf')
#     nearest = nid
#     for n in osm_graph.nodes:
#         n_lat, n_lon = nodes[n]
#         dist = (lat - n_lat)**2 + (lon - n_lon)**2
#         if dist < min_dist:
#             min_dist = dist
#             nearest = n
#     return nearest

# def path_to_names(path, named_nodes):
#     node_names = []
#     for n in path:
#         found = [name for name, nid in named_nodes.items() if nid == n]
#         node_names.append(found[0] if found else "Unnamed")
#     return node_names

# # ---------------- Streamlit App ----------------
# st.title("🗺️ AIDFlow: Clustered Disaster Relief Routing with Allocation")

# # Step 0: Upload OSM PBF
# uploaded_file = st.file_uploader("Upload .osm.pbf file", type=["pbf", "osm.pbf"])
# if uploaded_file is None:
#     st.info("Please upload an OSM .pbf map file to begin.")
#     st.stop()

# with open("uploaded.osm.pbf", "wb") as f:
#     f.write(uploaded_file.read())

# nodes, named_nodes, osm_graph = parse_osm_pbf("uploaded.osm.pbf")

# if len(named_nodes) == 0:
#     st.error("No named places found in this OSM file.")
#     st.stop()

# # Step 1: Cluster nodes using DBSCAN
# coords = np.array([nodes[n] for n in named_nodes.values()])
# node_ids = list(named_nodes.values())
# clustering = DBSCAN(eps=0.001, min_samples=2).fit(coords)
# labels = clustering.labels_

# clusters = {}
# for label, nid in zip(labels, node_ids):
#     clusters.setdefault(label, []).append(nid)

# cluster_name_map = {}
# for lbl, nids in clusters.items():
#     cluster_name_map[lbl] = [name for name, nid in named_nodes.items() if nid in nids]

# available_clusters = [lbl for lbl in cluster_name_map.keys() if lbl != -1]
# selected_cluster = st.selectbox(
#     "Select a cluster of places:",
#     options=available_clusters,
#     format_func=lambda x: f"Cluster {x} ({len(cluster_name_map[x])} nodes)"
# )
# cluster_nodes = cluster_name_map[selected_cluster]

# # Step 2: Select origin & destinations
# st.subheader("Select Origin & Destinations in Cluster")
# origin = st.selectbox("Origin", options=cluster_nodes, index=0)
# destinations = st.multiselect("Destinations", options=[n for n in cluster_nodes if n != origin])

# if not origin or len(destinations) == 0:
#     st.warning("Please select an origin and at least one destination.")
#     st.stop()

# # Step 3: Populations
# st.subheader("Enter Population for Destinations")
# population_per_zone = {}
# for zone in destinations:
#     population_per_zone[zone] = st.number_input(f"Population in {zone}:", min_value=1, value=100, key=f"pop_{zone}")

# # Step 4: Resources
# st.subheader("Enter Total Resources Available")
# total_food_kits = st.number_input("Total Food Kits:", min_value=0, value=500)
# total_medicinal_kits = st.number_input("Total Medicinal Kits:", min_value=0, value=200)
# total_clothes = st.number_input("Total Clothes:", min_value=0, value=300)

# # Step 5: Compute routes & allocations
# if st.button("Compute Routes & Allocate"):

#     origin_node = nearest_graph_node(origin, nodes, named_nodes, osm_graph)
#     dest_nodes = [nearest_graph_node(d, nodes, named_nodes, osm_graph) for d in destinations]

#     # Weighted shortest paths
#     routes = {}
#     routes_coords = {}
#     routes_weights = {}
#     for dest_name, dest_node in zip(destinations, dest_nodes):
#         try:
#             path_nodes = nx.shortest_path(osm_graph, origin_node, dest_node, weight='weight')
#             path_weight = nx.shortest_path_length(osm_graph, origin_node, dest_node, weight='weight')
#             routes[dest_name] = path_nodes
#             routes_coords[dest_name] = [nodes[n] for n in path_nodes]
#             routes_weights[dest_name] = path_weight
#         except nx.NetworkXNoPath:
#             routes[dest_name] = None
#             routes_coords[dest_name] = None
#             routes_weights[dest_name] = None

#     # Allocation
#     food_alloc, delayed_food = allocate_by_user_priority(total_food_kits, population_per_zone, destinations)
#     med_alloc, delayed_med = allocate_by_user_priority(total_medicinal_kits, population_per_zone, destinations)
#     clothes_alloc, delayed_clothes = allocate_by_user_priority(total_clothes, population_per_zone, destinations)

#     # Save to session_state
#     st.session_state.update({
#         'routes': routes,
#         'routes_coords': routes_coords,
#         'routes_weights': routes_weights,
#         'food_alloc': food_alloc,
#         'med_alloc': med_alloc,
#         'clothes_alloc': clothes_alloc,
#         'delayed_food': delayed_food,
#         'delayed_med': delayed_med,
#         'delayed_clothes': delayed_clothes,
#         'origin': origin,
#         'destinations': destinations,
#         'computed': True
#     })

# # Step 6: Display results
# if st.session_state.get('computed', False):
#     routes = st.session_state['routes']
#     routes_coords = st.session_state['routes_coords']
#     routes_weights = st.session_state['routes_weights']
#     food_alloc = st.session_state['food_alloc']
#     med_alloc = st.session_state['med_alloc']
#     clothes_alloc = st.session_state['clothes_alloc']
#     delayed_food = st.session_state['delayed_food']
#     delayed_med = st.session_state['delayed_med']
#     delayed_clothes = st.session_state['delayed_clothes']
#     origin = st.session_state['origin']
#     destinations = st.session_state['destinations']

#     st.subheader("Outcomes")

#     for idx, zone in enumerate(destinations):
#         path = routes.get(zone)
#         weight_m = routes_weights.get(zone)
#         if path:
#             node_names = path_to_names(path, named_nodes)
#             st.write(f"### {zone}")
#             st.write(f"Population: {population_per_zone[zone]}")
#             st.write(f"Food Kits: {food_alloc[zone]}")
#             st.write(f"Medicinal Kits: {med_alloc[zone]}")
#             st.write(f"Clothes: {clothes_alloc[zone]}")
#             st.write(f"Route: {' → '.join(node_names)}")
#             st.write(f"Total distance: {weight_m/1000:.2f} km")
#         else:
#             st.write(f"No route found to {zone}")
#         st.write("---")

#     # Warnings
#     def warn(lst, res):
#         if lst:
#             st.warning(f"⚠ Some areas may face delays in {res}: {', '.join(lst)}")
#     warn(delayed_food, "Food Kits")
#     warn(delayed_med, "Medicinal Kits")
#     warn(delayed_clothes, "Clothes")

#     # Map
#     st.subheader("Map Visualization")
#     origin_node_id = nearest_graph_node(origin, nodes, named_nodes, osm_graph)
#     origin_lat, origin_lon = nodes[origin_node_id]
#     m = folium.Map(location=[origin_lat, origin_lon], zoom_start=15)

#     # Origin green
#     folium.Marker([origin_lat, origin_lon], popup=f"Origin: {origin}", icon=folium.Icon(color='green')).add_to(m)

#     # Destinations red labeled Dest 1, Dest 2, ...
#     for idx, zone in enumerate(destinations, start=1):
#         coords = routes_coords[zone]
#         if coords:
#             folium.Marker(coords[-1], popup=f"Dest {idx}: {zone}", icon=folium.Icon(color='red')).add_to(m)
#             folium.PolyLine(coords, color='blue', weight=3).add_to(m)

#     st_folium(m, width=800, height=600)















#13 working with only optimised route
# import streamlit as st
# from streamlit_folium import st_folium
# import folium
# import networkx as nx
# import numpy as np
# from sklearn.cluster import DBSCAN
# import osmium
# from math import radians, cos, sin, sqrt, atan2

# # ---------------- Haversine function ----------------
# def haversine(lat1, lon1, lat2, lon2):
#     R = 6371000  # meters
#     phi1, phi2 = radians(lat1), radians(lat2)
#     dphi = radians(lat2 - lat1)
#     dlambda = radians(lon2 - lon1)
#     a = sin(dphi/2)**2 + cos(phi1)*cos(phi2)*sin(dlambda/2)**2
#     c = 2 * atan2(sqrt(a), sqrt(1-a))
#     return R * c

# # ---------------- OSM Parser ----------------
# class OSMParser(osmium.SimpleHandler):
#     def __init__(self):
#         super().__init__()
#         self.nodes = {}        # node_id → (lat, lon)
#         self.named_nodes = {}  # name → node_id
#         self.graph = nx.Graph()

#     def node(self, n):
#         if not n.location.valid():
#             return
#         lat, lon = n.location.lat, n.location.lon
#         self.nodes[n.id] = (lat, lon)
#         name = n.tags.get("name")
#         if name:
#             self.named_nodes[name] = n.id

#     def way(self, w):
#         if "highway" in w.tags and len(w.nodes) > 1:
#             for i in range(len(w.nodes) - 1):
#                 n1, n2 = w.nodes[i].ref, w.nodes[i+1].ref
#                 if n1 in self.nodes and n2 in self.nodes:
#                     lat1, lon1 = self.nodes[n1]
#                     lat2, lon2 = self.nodes[n2]
#                     weight = haversine(lat1, lon1, lat2, lon2)
#                     self.graph.add_edge(n1, n2, weight=weight)

# def parse_osm_pbf(pbf_file):
#     parser = OSMParser()
#     parser.apply_file(pbf_file)
#     return parser.nodes, parser.named_nodes, parser.graph

# # ---------------- Allocation logic ----------------
# def allocate_by_user_priority(total_resources, population_dict, priority_order):
#     allocation = {zone: 0 for zone in population_dict}
#     remaining = total_resources
#     delayed_zones = []
#     for zone in priority_order:
#         needed = population_dict[zone]
#         alloc = min(needed, remaining)
#         allocation[zone] = alloc
#         remaining -= alloc
#         if alloc < needed:
#             delayed_zones.append(zone)
#         if remaining <= 0:
#             continue
#     return allocation, delayed_zones

# # ---------------- Helper functions ----------------
# def nearest_graph_node(node_name, nodes, named_nodes, osm_graph):
#     nid = named_nodes[node_name]
#     lat, lon = nodes[nid]
#     min_dist = float('inf')
#     nearest = nid
#     for n in osm_graph.nodes:
#         n_lat, n_lon = nodes[n]
#         dist = (lat - n_lat)**2 + (lon - n_lon)**2
#         if dist < min_dist:
#             min_dist = dist
#             nearest = n
#     return nearest

# def path_to_names(path, named_nodes):
#     node_names = []
#     for n in path:
#         found = [name for name, nid in named_nodes.items() if nid == n]
#         node_names.append(found[0] if found else "Unnamed")
#     return node_names

# # ---------------- Multi-stop Nearest-Neighbor Route ----------------
# def compute_multi_stop_route(origin_name, destinations, nodes, named_nodes, osm_graph):
#     # Convert names → graph node IDs
#     current = nearest_graph_node(origin_name, nodes, named_nodes, osm_graph)
#     remaining = destinations.copy()

#     ordered_stops = [origin_name]
#     complete_path = []
#     total_distance = 0

#     while remaining:
#         nearest_dest = None
#         nearest_node = None
#         shortest = float('inf')

#         for dest in remaining:
#             dest_node = nearest_graph_node(dest, nodes, named_nodes, osm_graph)
#             try:
#                 d = nx.shortest_path_length(osm_graph, current, dest_node, weight="weight")
#                 if d < shortest:
#                     shortest = d
#                     nearest_dest = dest
#                     nearest_node = dest_node
#             except nx.NetworkXNoPath:
#                 continue

#         ordered_stops.append(nearest_dest)

#         # Get shortest path
#         path_nodes = nx.shortest_path(osm_graph, current, nearest_node, weight="weight")

#         # Append cleanly (avoid duplicate nodes)
#         if complete_path:
#             complete_path += path_nodes[1:]
#         else:
#             complete_path = path_nodes

#         total_distance += shortest
#         current = nearest_node
#         remaining.remove(nearest_dest)

#     # Convert to coords
#     full_coords = [nodes[n] for n in complete_path]
#     readable_names = path_to_names(complete_path, named_nodes)

#     return ordered_stops, readable_names, full_coords, total_distance

# # ---------------- Streamlit App ----------------
# st.title("🗺️ AIDFlow: Optimized Multi-Stop Disaster Relief Routing")

# # Step 0: Upload OSM PBF
# uploaded_file = st.file_uploader("Upload .osm.pbf file", type=["pbf", "osm.pbf"])
# if uploaded_file is None:
#     st.info("Please upload an OSM .pbf map file to begin.")
#     st.stop()

# with open("uploaded.osm.pbf", "wb") as f:
#     f.write(uploaded_file.read())

# nodes, named_nodes, osm_graph = parse_osm_pbf("uploaded.osm.pbf")

# if len(named_nodes) == 0:
#     st.error("No named places found in this OSM file.")
#     st.stop()

# # Step 1: Cluster nodes using DBSCAN
# coords = np.array([nodes[n] for n in named_nodes.values()])
# node_ids = list(named_nodes.values())
# clustering = DBSCAN(eps=0.001, min_samples=2).fit(coords)
# labels = clustering.labels_

# clusters = {}
# for label, nid in zip(labels, node_ids):
#     clusters.setdefault(label, []).append(nid)

# cluster_name_map = {}
# for lbl, nids in clusters.items():
#     cluster_name_map[lbl] = [name for name, nid in named_nodes.items() if nid in nids]

# available_clusters = [lbl for lbl in cluster_name_map.keys() if lbl != -1]
# selected_cluster = st.selectbox(
#     "Select a cluster of places:",
#     options=available_clusters,
#     format_func=lambda x: f"Cluster {x} ({len(cluster_name_map[x])} nodes)"
# )
# cluster_nodes = cluster_name_map[selected_cluster]

# # Step 2: Select origin & destinations
# st.subheader("Select Origin & Destinations in Cluster")
# origin = st.selectbox("Origin", options=cluster_nodes, index=0)
# destinations = st.multiselect("Destinations", options=[n for n in cluster_nodes if n != origin])

# if not origin or len(destinations) == 0:
#     st.warning("Please select an origin and at least one destination.")
#     st.stop()

# # Step 3: Populations
# st.subheader("Enter Population for Destinations")
# population_per_zone = {}
# for zone in destinations:
#     population_per_zone[zone] = st.number_input(f"Population in {zone}:", min_value=1, value=100, key=f"pop_{zone}")

# # Step 4: Resources
# st.subheader("Enter Total Resources Available")
# total_food_kits = st.number_input("Total Food Kits:", min_value=0, value=500)
# total_medicinal_kits = st.number_input("Total Medicinal Kits:", min_value=0, value=200)
# total_clothes = st.number_input("Total Clothes:", min_value=0, value=300)

# # Step 5: Compute routes & allocations
# if st.button("Compute Routes & Allocate"):

#     origin_node = nearest_graph_node(origin, nodes, named_nodes, osm_graph)
#     dest_nodes = [nearest_graph_node(d, nodes, named_nodes, osm_graph) for d in destinations]

#     # Weighted shortest paths (individual)
#     routes = {}
#     routes_coords = {}
#     routes_weights = {}
#     for dest_name, dest_node in zip(destinations, dest_nodes):
#         try:
#             path_nodes = nx.shortest_path(osm_graph, origin_node, dest_node, weight='weight')
#             path_weight = nx.shortest_path_length(osm_graph, origin_node, dest_node, weight='weight')
#             routes[dest_name] = path_nodes
#             routes_coords[dest_name] = [nodes[n] for n in path_nodes]
#             routes_weights[dest_name] = path_weight
#         except nx.NetworkXNoPath:
#             routes[dest_name] = None
#             routes_coords[dest_name] = None
#             routes_weights[dest_name] = None

#     # Allocation
#     food_alloc, delayed_food = allocate_by_user_priority(total_food_kits, population_per_zone, destinations)
#     med_alloc, delayed_med = allocate_by_user_priority(total_medicinal_kits, population_per_zone, destinations)
#     clothes_alloc, delayed_clothes = allocate_by_user_priority(total_clothes, population_per_zone, destinations)

#     # Multi-stop route (NEW)
#     ordered_stops, multi_names, multi_coords, multi_dist = compute_multi_stop_route(
#         origin,
#         destinations,
#         nodes,
#         named_nodes,
#         osm_graph
#     )

#     # Save results
#     st.session_state.update({
#         'routes': routes,
#         'routes_coords': routes_coords,
#         'routes_weights': routes_weights,
#         'food_alloc': food_alloc,
#         'med_alloc': med_alloc,
#         'clothes_alloc': clothes_alloc,
#         'delayed_food': delayed_food,
#         'delayed_med': delayed_med,
#         'delayed_clothes': delayed_clothes,
#         'origin': origin,
#         'destinations': destinations,
#         'ordered_stops': ordered_stops,
#         'multi_names': multi_names,
#         'multi_coords': multi_coords,
#         'multi_dist': multi_dist,
#         'computed': True
#     })

# # Step 6: Display results
# if st.session_state.get('computed', False):
#     routes = st.session_state['routes']
#     routes_coords = st.session_state['routes_coords']
#     routes_weights = st.session_state['routes_weights']
#     food_alloc = st.session_state['food_alloc']
#     med_alloc = st.session_state['med_alloc']
#     clothes_alloc = st.session_state['clothes_alloc']
#     delayed_food = st.session_state['delayed_food']
#     delayed_med = st.session_state['delayed_med']
#     delayed_clothes = st.session_state['delayed_clothes']
#     origin = st.session_state['origin']
#     destinations = st.session_state['destinations']

#     ordered_stops = st.session_state['ordered_stops']
#     multi_names = st.session_state['multi_names']
#     multi_coords = st.session_state['multi_coords']
#     multi_dist = st.session_state['multi_dist']

#     st.subheader("Individual Outcomes")
#     for zone in destinations:
#         path = routes.get(zone)
#         weight_m = routes_weights.get(zone)
#         if path:
#             node_names = path_to_names(path, named_nodes)
#             st.write(f"### {zone}")
#             st.write(f"Population: {population_per_zone[zone]}")
#             st.write(f"Food Kits: {food_alloc[zone]}")
#             st.write(f"Medicinal Kits: {med_alloc[zone]}")
#             st.write(f"Clothes: {clothes_alloc[zone]}")
#             st.write(f"Route: {' → '.join(node_names)}")
#             st.write(f"Total distance: {weight_m/1000:.2f} km")
#         else:
#             st.write(f"No route found to {zone}")
#         st.write("---")

#     # Warnings
#     if delayed_food:
#         st.warning(f"⚠ Delayed Food: {', '.join(delayed_food)}")
#     if delayed_med:
#         st.warning(f"⚠ Delayed Medical Kits: {', '.join(delayed_med)}")
#     if delayed_clothes:
#         st.warning(f"⚠ Delayed Clothes: {', '.join(delayed_clothes)}")

#     # ----------- Multi-stop optimized route -----------
#     st.subheader("🚀 Optimized Multi-Stop Visit Order (Nearest Neighbor)")
#     st.write(" → ".join(ordered_stops))
#     st.write(f"Total travel distance: {multi_dist/1000:.2f} km")

#     # Map
#     st.subheader("Map Visualization")
#     origin_node = nearest_graph_node(origin, nodes, named_nodes, osm_graph)
#     origin_lat, origin_lon = nodes[origin_node]
#     m = folium.Map(location=[origin_lat, origin_lon], zoom_start=15)

#     # Origin green
#     folium.Marker([origin_lat, origin_lon], popup=f"Origin: {origin}", icon=folium.Icon(color='green')).add_to(m)

#     # Destinations red
#     for idx, zone in enumerate(destinations, start=1):
#         coords = routes_coords[zone]
#         if coords:
#             folium.Marker(coords[-1], popup=f"Dest {idx}: {zone}", icon=folium.Icon(color='red')).add_to(m)
#             folium.PolyLine(coords, color='blue', weight=3).add_to(m)

#     # Full optimized route in green
#     if multi_coords:
#         folium.PolyLine(multi_coords, color='green', weight=4).add_to(m)

#     st_folium(m, width=800, height=600)





















#14 fully correct
# import streamlit as st
# from streamlit_folium import st_folium
# import folium
# import networkx as nx
# import numpy as np
# from sklearn.cluster import DBSCAN
# import osmium
# from math import radians, cos, sin, sqrt, atan2
# from copy import deepcopy

# # ---------------- Haversine function ----------------
# def haversine(lat1, lon1, lat2, lon2):
#     R = 6371000  # meters
#     phi1, phi2 = radians(lat1), radians(lat2)
#     dphi = radians(lat2 - lat1)
#     dlambda = radians(lon2 - lon1)
#     a = sin(dphi/2)**2 + cos(phi1)*cos(phi2)*sin(dlambda/2)**2
#     c = 2 * atan2(sqrt(a), sqrt(1-a))
#     return R * c

# # ---------------- OSM Parser ----------------
# class OSMParser(osmium.SimpleHandler):
#     def __init__(self):
#         super().__init__()
#         self.nodes = {}        # node_id → (lat, lon)
#         self.named_nodes = {}  # name → node_id
#         self.graph = nx.Graph()

#     def node(self, n):
#         # store node coordinates and any name tag
#         if not n.location.valid():
#             return
#         lat, lon = n.location.lat, n.location.lon
#         self.nodes[n.id] = (lat, lon)
#         name = n.tags.get("name")
#         if name:
#             # if multiple nodes share the same name, last one wins — acceptable for small tests
#             self.named_nodes[name] = n.id

#     def way(self, w):
#         # only consider ways that are roads (have highway tag) and have at least two nodes
#         if "highway" in w.tags and len(w.nodes) > 1:
#             for i in range(len(w.nodes) - 1):
#                 n1, n2 = w.nodes[i].ref, w.nodes[i+1].ref
#                 if n1 in self.nodes and n2 in self.nodes:
#                     lat1, lon1 = self.nodes[n1]
#                     lat2, lon2 = self.nodes[n2]
#                     weight = haversine(lat1, lon1, lat2, lon2)
#                     # add edge with weight as distance in meters
#                     self.graph.add_edge(n1, n2, weight=weight)

# def parse_osm_pbf(pbf_file):
#     parser = OSMParser()
#     parser.apply_file(pbf_file)
#     return parser.nodes, parser.named_nodes, parser.graph

# # ---------------- Allocation logic ----------------
# def allocate_by_user_priority(total_resources, population_dict, priority_order):
#     allocation = {zone: 0 for zone in population_dict}
#     remaining = total_resources
#     delayed_zones = []
#     for zone in priority_order:
#         needed = population_dict[zone]
#         alloc = min(needed, remaining)
#         allocation[zone] = alloc
#         remaining -= alloc
#         if alloc < needed:
#             delayed_zones.append(zone)
#         if remaining <= 0:
#             continue
#     return allocation, delayed_zones

# # ---------------- Helper functions ----------------
# def nearest_graph_node(node_name, nodes, named_nodes, osm_graph):
#     """
#     Map a named place (string) to the closest existing node in the routing graph.
#     This function first looks up the OSM node id for the name, then finds the
#     closest graph node (by euclidean in lat/lon) among nodes present in osm_graph.
#     """
#     if node_name not in named_nodes:
#         raise KeyError(f"Name '{node_name}' not found in named_nodes.")
#     base_nid = named_nodes[node_name]
#     lat, lon = nodes[base_nid]
#     min_dist = float('inf')
#     nearest = base_nid
#     for n in osm_graph.nodes:
#         n_lat, n_lon = nodes.get(n, (None, None))
#         if n_lat is None:
#             continue
#         # use squared lat/lon distance (fast) — relative ordering preserved
#         dist = (lat - n_lat)**2 + (lon - n_lon)**2
#         if dist < min_dist:
#             min_dist = dist
#             nearest = n
#     return nearest

# def path_to_names(path, named_nodes):
#     node_names = []
#     for n in path:
#         found = [name for name, nid in named_nodes.items() if nid == n]
#         node_names.append(found[0] if found else "Unnamed")
#     return node_names

# # ---------------- Multi-stop Nearest-Neighbor Route ----------------
# def compute_multi_stop_route(origin_name, destinations, nodes, named_nodes, osm_graph):
#     """
#     Nearest-neighbor multi-stop route:
#     Start at origin_name, pick nearest unvisited destination (by shortest path distance on osm_graph),
#     append, and repeat until all destinations are visited.
#     Returns:
#       ordered_stops: list of names starting with origin and followed by destination names in visit order
#       readable_names: list of place names encountered along the concatenated node path (for display)
#       full_coords: list of (lat, lon) for the full concatenated path
#       total_distance: sum of shortest-path distances (meters)
#     """
#     if not destinations:
#         return [origin_name], [], [], 0.0

#     current = nearest_graph_node(origin_name, nodes, named_nodes, osm_graph)
#     remaining = deepcopy(destinations)
#     ordered_stops = [origin_name]
#     complete_path = []
#     total_distance = 0.0

#     while remaining:
#         nearest_dest = None
#         nearest_node = None
#         shortest = float('inf')
#         for dest in remaining:
#             dest_node = nearest_graph_node(dest, nodes, named_nodes, osm_graph)
#             try:
#                 d = nx.shortest_path_length(osm_graph, current, dest_node, weight="weight")
#                 if d < shortest:
#                     shortest = d
#                     nearest_dest = dest
#                     nearest_node = dest_node
#             except nx.NetworkXNoPath:
#                 continue

#         if nearest_dest is None:
#             # remaining destinations unreachable
#             break

#         ordered_stops.append(nearest_dest)
#         # actual path nodes
#         path_nodes = nx.shortest_path(osm_graph, current, nearest_node, weight="weight")
#         if complete_path:
#             complete_path += path_nodes[1:]
#         else:
#             complete_path = path_nodes
#         total_distance += shortest
#         current = nearest_node
#         remaining.remove(nearest_dest)

#     full_coords = [nodes[n] for n in complete_path] if complete_path else []
#     readable_names = path_to_names(complete_path, named_nodes) if complete_path else []
#     return ordered_stops, readable_names, full_coords, total_distance

# # ---------------- User-selected order distance ----------------
# def compute_user_order_distance(origin_name, user_destinations, nodes, named_nodes, osm_graph):
#     """
#     Compute total distance and full path following the exact order:
#     origin -> dest1 -> dest2 -> ... -> destN
#     Returns:
#       ordered (list of names including origin)
#       full_coords (list of (lat,lon))
#       total_distance (meters) or None if a hop is unreachable
#     """
#     if not user_destinations:
#         return [origin_name], [], 0.0

#     ordered = [origin_name] + list(user_destinations)
#     full_path_nodes = []
#     total_distance = 0.0

#     for i in range(len(ordered) - 1):
#         start_name = ordered[i]
#         end_name = ordered[i+1]
#         start_node = nearest_graph_node(start_name, nodes, named_nodes, osm_graph)
#         end_node = nearest_graph_node(end_name, nodes, named_nodes, osm_graph)
#         try:
#             path_nodes = nx.shortest_path(osm_graph, start_node, end_node, weight="weight")
#             distance = nx.shortest_path_length(osm_graph, start_node, end_node, weight="weight")
#             if full_path_nodes:
#                 full_path_nodes += path_nodes[1:]
#             else:
#                 full_path_nodes = path_nodes
#             total_distance += distance
#         except nx.NetworkXNoPath:
#             return ordered, [], None

#     coords = [nodes[n] for n in full_path_nodes] if full_path_nodes else []
#     return ordered, coords, total_distance

# # ---------------- Streamlit App ----------------
# st.set_page_config(layout="wide")
# st.title("🗺️ AIDFlow: Optimized & User-Ordered Multi-Stop Disaster Relief Routing and Allocation")

# # Step 0: Upload OSM PBF
# uploaded_file = st.file_uploader("Upload .osm.pbf file", type=["pbf", "osm.pbf"])
# if uploaded_file is None:
#     st.info("Please upload an OSM .pbf map file to begin.")
#     st.stop()

# # Save uploaded file temporarily
# with open("uploaded.osm.pbf", "wb") as f:
#     f.write(uploaded_file.read())

# # Parse OSM
# try:
#     nodes, named_nodes, osm_graph = parse_osm_pbf("uploaded.osm.pbf")
# except Exception as e:
#     st.error(f"Error parsing PBF: {e}")
#     st.stop()

# if len(named_nodes) == 0:
#     st.error("No named places found in this OSM file.")
#     st.stop()

# place_names = sorted(list(named_nodes.keys()))

# # Optional quick info
# st.sidebar.markdown(f"**Parsed nodes:** {len(nodes)}  \n**Named places:** {len(named_nodes)}  \n**Graph nodes:** {len(osm_graph.nodes)}")

# # Step 1: Cluster nodes using DBSCAN (to present groups)
# coords = np.array([nodes[n] for n in named_nodes.values()])
# node_ids = list(named_nodes.values())

# # If there are too few named nodes, skip clustering and present all names
# if len(node_ids) < 3:
#     clusters = {0: node_ids}
#     labels = np.array([0]*len(node_ids))
# else:
#     clustering = DBSCAN(eps=0.001, min_samples=2).fit(coords)
#     labels = clustering.labels_
#     clusters = {}
#     for label, nid in zip(labels, node_ids):
#         clusters.setdefault(label, []).append(nid)

# cluster_name_map = {}
# for lbl, nids in clusters.items():
#     cluster_name_map[lbl] = [name for name, nid in named_nodes.items() if nid in nids]

# available_clusters = [lbl for lbl in cluster_name_map.keys() if lbl != -1]
# if not available_clusters:
#     # If only noise or single cluster, just pick all names
#     available_clusters = [list(cluster_name_map.keys())[0]]

# selected_cluster = st.selectbox(
#     "Select a cluster of places:",
#     options=available_clusters,
#     format_func=lambda x: f"Cluster {x} ({len(cluster_name_map[x])} nodes)"
# )
# cluster_nodes = cluster_name_map[selected_cluster]

# # Step 2: Select origin & destinations (names from the cluster)
# st.subheader("Select Origin & Destinations in Cluster")
# origin = st.selectbox("Origin", options=cluster_nodes, index=0)
# destinations = st.multiselect("Destinations (select in the order you prefer):", options=[n for n in cluster_nodes if n != origin])

# if not origin or len(destinations) == 0:
#     st.warning("Please select an origin and at least one destination.")
#     st.stop()

# # Step 3: Populations (for allocation)
# st.subheader("Enter Population for Destinations")
# population_per_zone = {}
# for zone in destinations:
#     population_per_zone[zone] = st.number_input(f"Population in {zone}:", min_value=1, value=100, key=f"pop_{zone}")

# # Step 4: Resources
# st.subheader("Enter Total Resources Available")
# total_food_kits = st.number_input("Total Food Kits:", min_value=0, value=500)
# total_medicinal_kits = st.number_input("Total Medicinal Kits:", min_value=0, value=200)
# total_clothes = st.number_input("Total Clothes:", min_value=0, value=300)

# # Step 5: Compute routes & allocations
# if st.button("Compute Routes & Allocate"):

#     origin_node = nearest_graph_node(origin, nodes, named_nodes, osm_graph)
#     dest_nodes = [nearest_graph_node(d, nodes, named_nodes, osm_graph) for d in destinations]

#     # Weighted shortest paths (individual)
#     routes = {}
#     routes_coords = {}
#     routes_weights = {}
#     for dest_name, dest_node in zip(destinations, dest_nodes):
#         try:
#             path_nodes = nx.shortest_path(osm_graph, origin_node, dest_node, weight='weight')
#             path_weight = nx.shortest_path_length(osm_graph, origin_node, dest_node, weight='weight')
#             routes[dest_name] = path_nodes
#             routes_coords[dest_name] = [nodes[n] for n in path_nodes]
#             routes_weights[dest_name] = path_weight
#         except nx.NetworkXNoPath:
#             routes[dest_name] = None
#             routes_coords[dest_name] = None
#             routes_weights[dest_name] = None

#     # Allocation
#     food_alloc, delayed_food = allocate_by_user_priority(total_food_kits, population_per_zone, destinations)
#     med_alloc, delayed_med = allocate_by_user_priority(total_medicinal_kits, population_per_zone, destinations)
#     clothes_alloc, delayed_clothes = allocate_by_user_priority(total_clothes, population_per_zone, destinations)

#     # Multi-stop route (optimized nearest neighbor)
#     ordered_stops, multi_names, multi_coords, multi_dist = compute_multi_stop_route(
#         origin,
#         destinations,
#         nodes,
#         named_nodes,
#         osm_graph
#     )

#     # User-ordered route (exact order selected by user)
#     user_order, user_coords, user_dist = compute_user_order_distance(
#         origin,
#         destinations,
#         nodes,
#         named_nodes,
#         osm_graph
#     )

#     # Save results into session
#     st.session_state.update({
#         'routes': routes,
#         'routes_coords': routes_coords,
#         'routes_weights': routes_weights,
#         'food_alloc': food_alloc,
#         'med_alloc': med_alloc,
#         'clothes_alloc': clothes_alloc,
#         'delayed_food': delayed_food,
#         'delayed_med': delayed_med,
#         'delayed_clothes': delayed_clothes,
#         'origin': origin,
#         'destinations': destinations,
#         'ordered_stops': ordered_stops,
#         'multi_names': multi_names,
#         'multi_coords': multi_coords,
#         'multi_dist': multi_dist,
#         'user_order': user_order,
#         'user_coords': user_coords,
#         'user_dist': user_dist,
#         'computed': True
#     })

# # Step 6: Display results
# if st.session_state.get('computed', False):
#     routes = st.session_state['routes']
#     routes_coords = st.session_state['routes_coords']
#     routes_weights = st.session_state['routes_weights']
#     food_alloc = st.session_state['food_alloc']
#     med_alloc = st.session_state['med_alloc']
#     clothes_alloc = st.session_state['clothes_alloc']
#     delayed_food = st.session_state['delayed_food']
#     delayed_med = st.session_state['delayed_med']
#     delayed_clothes = st.session_state['delayed_clothes']
#     origin = st.session_state['origin']
#     destinations = st.session_state['destinations']

#     ordered_stops = st.session_state['ordered_stops']
#     multi_names = st.session_state['multi_names']
#     multi_coords = st.session_state['multi_coords']
#     multi_dist = st.session_state['multi_dist']

#     user_order = st.session_state['user_order']
#     user_coords = st.session_state['user_coords']
#     user_dist = st.session_state['user_dist']

#     # Display individual outcomes
#     st.subheader("Individual Outcomes (Origin → Destination shortest path)")
#     for zone in destinations:
#         path = routes.get(zone)
#         weight_m = routes_weights.get(zone)
#         if path:
#             node_names = path_to_names(path, named_nodes)
#             st.write(f"### {zone}")
#             st.write(f"Population: {population_per_zone[zone]}")
#             st.write(f"Food Kits: {food_alloc[zone]}")
#             st.write(f"Medicinal Kits: {med_alloc[zone]}")
#             st.write(f"Clothes: {clothes_alloc[zone]}")
#             # st.write(f"Route: {' → '.join(node_names)}")
#             st.write(f"Total distance: {weight_m/1000:.2f} km")
#         else:
#             st.write(f"No route found to {zone}")
#         st.write("---")

#     # Warnings about delays
#     if delayed_food:
#         st.warning(f"⚠ Delayed Food: {', '.join(delayed_food)}")
#     if delayed_med:
#         st.warning(f"⚠ Delayed Medical Kits: {', '.join(delayed_med)}")
#     if delayed_clothes:
#         st.warning(f"⚠ Delayed Clothes: {', '.join(delayed_clothes)}")

#     # Multi-stop optimized route
#     st.subheader("🚀 Optimized Multi-Stop Visit Order (Nearest Neighbor)")
#     st.write(" → ".join(ordered_stops))
#     st.write(f"Total travel distance (optimized): {multi_dist/1000:.2f} km")

#     # User-selected order distance
#     st.subheader("🧭 User-Selected Visit Order (Exact order you selected)")
#     if user_dist is None:
#         st.error("No valid route found for the user-selected travel order (one or more hops unreachable).")
#     else:
#         st.write(" → ".join(user_order))
#         st.write(f"Total travel distance (user order): {user_dist/1000:.2f} km")

#     # # Toggle which route(s) to display on the map
#     # st.subheader("Map Display Options")
#     # display_choice = st.selectbox("Show Route:", options=["Optimized Route", "User-Selected Route", "Both Routes"])

#     # # Map
#     # st.subheader("Map Visualization")
#     # origin_node = nearest_graph_node(origin, nodes, named_nodes, osm_graph)
#     # origin_lat, origin_lon = nodes[origin_node]
#     # m = folium.Map(location=[origin_lat, origin_lon], zoom_start=14)

#     # # Origin marker
#     # folium.Marker([origin_lat, origin_lon], popup=f"Origin: {origin}", icon=folium.Icon(color='green')).add_to(m)

#     # # Draw individual shortest paths (blue) and destination markers
#     # for idx, zone in enumerate(destinations, start=1):
#     #     coords = routes_coords.get(zone)
#     #     if coords:
#     #         # destination marker
#     #         folium.Marker(coords[-1], popup=f"Dest {idx}: {zone}", icon=folium.Icon(color='red')).add_to(m)
#     #         # individual route (dashed thinner blue)
#     #         folium.PolyLine(coords, color='blue', weight=2, opacity=0.6).add_to(m)

#     # # Draw optimized route (green)
#     # if display_choice in ("Optimized Route", "Both Routes") and multi_coords:
#     #     folium.PolyLine(multi_coords, color='green', weight=5, opacity=0.9, tooltip="Optimized route").add_to(m)
#     #     # mark the intermediate stops on optimized route
#     #     try:
#     #         for i, name in enumerate(ordered_stops[1:], start=1):
#     #             # find node and coords for the named stop
#     #             nid = nearest_graph_node(name, nodes, named_nodes, osm_graph)
#     #             lat, lon = nodes[nid]
#     #             folium.CircleMarker([lat, lon], radius=4, color='green', fill=True, fill_opacity=1, popup=f"{i}. {name}").add_to(m)
#     #     except Exception:
#     #         pass

#     # # Draw user-ordered route (orange)
#     # if display_choice in ("User-Selected Route", "Both Routes") and user_coords:
#     #     if user_dist is not None:
#     #         folium.PolyLine(user_coords, color='orange', weight=5, opacity=0.9, tooltip="User-ordered route").add_to(m)
#     #         try:
#     #             # user_order includes origin + destinations
#     #             for i, name in enumerate(user_order[1:], start=1):
#     #                 nid = nearest_graph_node(name, nodes, named_nodes, osm_graph)
#     #                 lat, lon = nodes[nid]
#     #                 folium.CircleMarker([lat, lon], radius=4, color='orange', fill=True, fill_opacity=1, popup=f"{i}. {name}").add_to(m)
#     #         except Exception:
#     #             pass
#     #     else:
#     #         st.info("User-ordered route cannot be drawn because one or more hops are unreachable.")


#     # Toggle which route(s) to display on the map
#     st.subheader("Map Display Options")
#     display_choice = st.selectbox(
#         "Show Route:",
#         options=["Optimized Route", "User-Selected Route", "Both Routes"]
#     )

#     # Map
#     st.subheader("Map Visualization")
#     origin_node = nearest_graph_node(origin, nodes, named_nodes, osm_graph)
#     origin_lat, origin_lon = nodes[origin_node]
#     m = folium.Map(location=[origin_lat, origin_lon], zoom_start=14)

#     # Origin marker
#     folium.Marker([origin_lat, origin_lon], popup=f"Origin: {origin}", icon=folium.Icon(color='green')).add_to(m)

#     # ---------- BLUE ROUTES (individual paths) ----------
#     if display_choice in ("Optimized Route", "Both Routes"):
#         for idx, zone in enumerate(destinations, start=1):
#             coords = routes_coords.get(zone)
#             if coords:
#                 folium.Marker(coords[-1], popup=f"Dest {idx}: {zone}", icon=folium.Icon(color='red')).add_to(m)
#                 folium.PolyLine(coords, color='blue', weight=2, opacity=0.6).add_to(m)

#     # ---------- GREEN ROUTE (optimized NNH route) ----------
#     if display_choice in ("Optimized Route", "Both Routes") and multi_coords:
#         folium.PolyLine(multi_coords, color='green', weight=5, opacity=0.9,
#                         tooltip="Optimized route").add_to(m)
#         try:
#             for i, name in enumerate(ordered_stops[1:], start=1):
#                 nid = nearest_graph_node(name, nodes, named_nodes, osm_graph)
#                 lat, lon = nodes[nid]
#                 folium.CircleMarker([lat, lon], radius=4, color='green', fill=True,
#                                     fill_opacity=1, popup=f"{i}. {name}").add_to(m)
#         except Exception:
#             pass

#     # ---------- ORANGE ROUTE (user-selected order) ----------
#     if display_choice in ("User-Selected Route", "Both Routes") and user_coords:
#         if user_dist is not None:
#             folium.PolyLine(user_coords, color='orange', weight=5, opacity=0.9,
#                             tooltip="User-ordered route").add_to(m)
#             try:
#                 for i, name in enumerate(user_order[1:], start=1):
#                     nid = nearest_graph_node(name, nodes, named_nodes, osm_graph)
#                     lat, lon = nodes[nid]
#                     folium.CircleMarker([lat, lon], radius=4, color='orange', fill=True,
#                                         fill_opacity=1, popup=f"{i}. {name}").add_to(m)
#             except Exception:
#                 pass
#         else:
#             st.info("User-ordered route cannot be drawn because one or more hops are unreachable.")

    


#     # Add simple legend (HTML)
#     # legend_html = """
#     #  <div style="
#     #  position: fixed;
#     #  bottom: 50px; left: 10px; width:210px; height:150px;
#     #  background-color: white; z-index:9999; padding:10px; border:2px solid grey;" color: black>
#     #  <b>Legend</b><br>
#     #  <i style="color:blue">Blue</i> — individual shortest paths (origin→each destination)<br>
#     #  <i style="color:green">Green</i> — optimized multi-stop route (nearest-neighbor)<br>
#     #  <i style="color:orange">Orange</i> — user-selected visit order<br>
#     #  <i style="color:green">●</i> Origin marker is green, destination markers are red
#     #  </div>
#     #  """
#     legend_html = """
#      <div style="
#      position: fixed;
#      bottom: 50px; left: 10px; width:260px; height:auto;
#      background-color: white; z-index:9999; padding:10px; border:2px solid grey;
#      font-size:14px; line-height:1.3;">
     
#      <b style="color:black;">Legend</b><br>

#      <span style="color:blue;">● Blue</span>
#      <span style="color:black;"> — individual shortest paths (origin→each destination)</span><br>

#      <span style="color:green;">● Green</span>
#      <span style="color:black;"> — optimized multi-stop route (nearest-neighbor)</span><br>

#      <span style="color:orange;">● Orange</span>
#      <span style="color:black;"> — user-selected visit order</span><br>

#      <span style="color:green;">●</span>
#      <span style="color:black;"> Origin marker, destinations are red</span>
#      </div>
#      """

#     m.get_root().html.add_child(folium.Element(legend_html))

#     st_folium(m, width=1000, height=700)
















# import streamlit as st
# from streamlit_folium import st_folium
# import folium
# import networkx as nx
# import numpy as np
# from sklearn.cluster import DBSCAN
# import osmium
# from math import radians, cos, sin, sqrt, atan2
# import random
# import time

# # ---------------- 1. Mathematical Helpers ----------------
# def haversine(lat1, lon1, lat2, lon2):
#     R = 6371000 
#     phi1, phi2 = radians(lat1), radians(lat2)
#     dphi, dlambda = radians(lat2 - lat1), radians(lon2 - lon1)
#     a = sin(dphi/2)**2 + cos(phi1)*cos(phi2)*sin(dlambda/2)**2
#     return R * 2 * atan2(sqrt(a), sqrt(1-a))

# # ---------------- 2. OSM Parser ----------------
# class OSMParser(osmium.SimpleHandler):
#     def __init__(self):
#         super().__init__()
#         self.nodes = {}        
#         self.named_nodes = {}  
#         self.graph = nx.Graph()

#     def node(self, n):
#         if not n.location.valid(): return
#         self.nodes[n.id] = (n.location.lat, n.location.lon)
#         if n.tags.get("name"): self.named_nodes[n.tags.get("name")] = n.id

#     def way(self, w):
#         if "highway" in w.tags and len(w.nodes) > 1:
#             for i in range(len(w.nodes) - 1):
#                 n1, n2 = w.nodes[i].ref, w.nodes[i+1].ref
#                 if n1 in self.nodes and n2 in self.nodes:
#                     weight = haversine(*self.nodes[n1], *self.nodes[n2])
#                     self.graph.add_edge(n1, n2, weight=weight)

# def parse_osm_pbf(pbf_file):
#     parser = OSMParser()
#     parser.apply_file(pbf_file)
#     return parser.nodes, parser.named_nodes, parser.graph

# # ---------------- 3. Genetic Algorithm Optimizer ----------------
# class GeneticOptimizer:
#     def __init__(self, graph, points, pop_size=50, generations=100):
#         self.G, self.points = graph, points
#         self.pop_size, self.generations = pop_size, generations
#         self.matrix = self._build_matrix()

#     def _build_matrix(self):
#         sz = len(self.points)
#         mat = np.zeros((sz, sz))
#         for i in range(sz):
#             for j in range(sz):
#                 if i == j: continue
#                 try: 
#                     mat[i][j] = nx.shortest_path_length(self.G, self.points[i], self.points[j], weight='weight')
#                 except: 
#                     mat[i][j] = 1e6
#         return mat

#     def _fitness(self, genome):
#         dist = self.matrix[0][genome[0]]
#         for i in range(len(genome)-1): dist += self.matrix[genome[i]][genome[i+1]]
#         return dist

#     def solve(self):
#         n = len(self.points) - 1
#         if n <= 0: return [0], 0
#         indices = list(range(1, n + 1))
#         pop = [random.sample(indices, n) for _ in range(self.pop_size)]
#         for _ in range(self.generations):
#             pop = sorted(pop, key=self._fitness)
#             new_gen = pop[:5]
#             while len(new_gen) < self.pop_size:
#                 p1, p2 = random.sample(pop[:20], 2)
#                 a, b = sorted(random.sample(range(n), 2))
#                 child = [None]*n
#                 child[a:b] = p1[a:b]
#                 p2_rem = [x for x in p2 if x not in child]
#                 ptr = 0
#                 for i in range(n):
#                     if child[i] is None: child[i] = p2_rem[ptr]; ptr += 1
#                 new_gen.append(child)
#             pop = new_gen
#         best = sorted(pop, key=self._fitness)[0]
#         return [0] + best, self._fitness(best)

# # ---------------- 4. Helper Logic ----------------
# def allocate_resources(total, pop_dict, order):
#     alloc, rem = {z: 0 for z in pop_dict}, total
#     for z in order:
#         a = min(pop_dict[z], rem)
#         alloc[z] = a
#         rem -= a
#     return alloc

# def get_nid(name, nodes, named_nodes, graph):
#     base = named_nodes[name]
#     return min(graph.nodes, key=lambda n: (nodes[base][0]-nodes[n][0])**2 + (nodes[base][1]-nodes[n][1])**2)

# # ---------------- 5. Streamlit App ----------------
# st.set_page_config(layout="wide")
# st.title("🗺️ AIDFlow: Optimized & User-Ordered Multi Stop Disaster Relief Routing and Allocation")

# uploaded_file = st.file_uploader("Upload .osm.pbf file", type=["pbf", "osm.pbf"])
# if not uploaded_file: st.stop()

# with open("uploaded.osm.pbf", "wb") as f: f.write(uploaded_file.read())
# nodes, named_nodes, osm_graph = parse_osm_pbf("uploaded.osm.pbf")

# # Clustering
# coords_arr = np.array([nodes[n] for n in named_nodes.values()])
# clustering = DBSCAN(eps=0.001, min_samples=2).fit(coords_arr)
# cluster_map = {}
# for lbl, nid in zip(clustering.labels_, named_nodes.values()):
#     if lbl != -1:
#         names = [name for name, i in named_nodes.items() if i == nid]
#         cluster_map.setdefault(lbl, []).extend(names)

# available_clusters = list(cluster_map.keys())
# selected_cluster = st.selectbox("Select a cluster of places:", options=available_clusters, 
#                                 format_func=lambda x: f"Cluster {x} ({len(cluster_map[x])} nodes)")
# cluster_nodes = cluster_map[selected_cluster]

# # Inputs
# origin = st.selectbox("Origin (Depot)", options=cluster_nodes)
# destinations = st.multiselect("Destinations (Selection Order)", options=[n for n in cluster_nodes if n != origin])
# if not origin or not destinations: st.stop()

# pop_per_zone = {z: st.number_input(f"Population: {z}", 1, 1000, 100) for z in destinations}
# t_food = st.number_input("Total Food Kits:", value=500)
# t_med = st.number_input("Total Med Kits:", value=200)
# t_clothes = st.number_input("Total Clothes:", value=300)

# if st.button("Compute & Compare All Methods"):
#     orig_id = get_nid(origin, nodes, named_nodes, osm_graph)
#     dest_name_map = {get_nid(d, nodes, named_nodes, osm_graph): d for d in destinations}
#     dest_ids = list(dest_name_map.keys())
#     all_pts = [orig_id] + dest_ids

#     # 1. User Order
#     u_dist = 0.0
#     for i in range(len(all_pts)-1):
#         try: u_dist += nx.shortest_path_length(osm_graph, all_pts[i], all_pts[i+1], weight='weight')
#         except: u_dist += 1000.0
    
#     # 2. Greedy
#     unvisited = list(dest_ids); curr = orig_id; g_dist = 0; g_stops = [origin]
#     while unvisited:
#         try:
#             nxt = min(unvisited, key=lambda x: nx.shortest_path_length(osm_graph, curr, x, weight='weight'))
#             g_dist += nx.shortest_path_length(osm_graph, curr, nxt, weight='weight')
#             g_stops.append(dest_name_map[nxt]); unvisited.remove(nxt); curr = nxt
#         except:
#             fallback = unvisited.pop(0); g_stops.append(dest_name_map[fallback]); g_dist += 1000.0

#     # 3. Genetic
#     ga = GeneticOptimizer(osm_graph, all_pts)
#     ga_idx, ga_dist = ga.solve()
#     ga_stops = [([origin] + destinations)[i] for i in ga_idx]

#     # Allocation
#     f_a = allocate_resources(t_food, pop_per_zone, destinations)
#     m_a = allocate_resources(t_med, pop_per_zone, destinations)
#     c_a = allocate_resources(t_clothes, pop_per_zone, destinations)

#     def get_coords(path_ids):
#         c = []
#         for i in range(len(path_ids)-1):
#             try:
#                 p = nx.shortest_path(osm_graph, path_ids[i], path_ids[i+1], weight='weight')
#                 c.extend([nodes[n] for n in (p if i==0 else p[1:])])
#             except: continue
#         return c

#     st.session_state.update({
#         'comp': True, 'f_a': f_a, 'm_a': m_a, 'c_a': c_a,
#         'u_order': [origin] + destinations, 'u_dist': u_dist,
#         'g_order': g_stops, 'g_dist': g_dist,
#         'ga_order': ga_stops, 'ga_dist': ga_dist,
#         'ga_coords': get_coords([all_pts[i] for i in ga_idx]),
#         'u_coords': get_coords(all_pts),
#         'map_loc': nodes[orig_id], 'origin_name': origin
#     })

# # Display Results
# if st.session_state.get('comp', False):
#     st.divider()
#     st.subheader("📊 Method Accuracy & Performance Comparison")
#     c1, c2, c3 = st.columns(3)
#     c1.metric("User Manual Dist", f"{st.session_state['u_dist']/1000:.2f} km")
#     c2.metric("Greedy Dist", f"{st.session_state['g_dist']/1000:.2f} km")
#     c3.metric("Genetic Dist", f"{st.session_state['ga_dist']/1000:.2f} km")

#     st.subheader("📍 Detailed Destination Visit Orders")
#     st.success(f"**Genetic Optimizer:** {' → '.join(st.session_state['ga_order'])} | **Dist:** {st.session_state['ga_dist']/1000:.2f} km")
#     st.info(f"**Greedy Optimizer:** {' → '.join(st.session_state['g_order'])} | **Dist:** {st.session_state['g_dist']/1000:.2f} km")
#     st.warning(f"**User Manual Order:** {' → '.join(st.session_state['u_order'])} | **Dist:** {st.session_state['u_dist']/1000:.2f} km")

#     st.subheader("📦 Individual Allocation Outcomes")
#     for z in destinations:
#         st.write(f"**{z}** | Pop: {pop_per_zone[z]} | Food: {st.session_state['f_a'][z]} | Med: {st.session_state['m_a'][z]} | Clothes: {st.session_state['c_a'][z]}")
    
#     st.subheader("🗺️ Route Visualization")
#     choice = st.radio("Select View:", ["Genetic Algorithm Path (Optimized)", "User Manual Path"])
#     m = folium.Map(location=st.session_state['map_loc'], zoom_start=15)
    
#     # Legend
#     legend_html = f'''
#     <div style="position: fixed; bottom: 50px; left: 50px; width: 180px; height: 100px; 
#     background-color: black; border:2px solid grey; z-index:9999; font-size:14px; padding: 10px;">
#     <b>Legend</b><br>
#     <i style="background: green; width: 10px; height: 10px; display: inline-block;"></i> {"GA Optimized" if "Genetic" in choice else "User Order"}<br>
#     <i style="color: green; font-weight: bold;">🏠</i> Origin (Depot)<br>
#     <i style="color: blue; font-weight: bold;">📍</i> Numbered Stops
#     </div>
#     '''
#     m.get_root().html.add_child(folium.Element(legend_html))

#     active_coords = st.session_state['ga_coords'] if "Genetic" in choice else st.session_state['u_coords']
#     active_stops = st.session_state['ga_order'] if "Genetic" in choice else st.session_state['u_order']
#     line_color = 'green' if "Genetic" in choice else 'orange'
    
#     if active_coords:
#         folium.PolyLine(active_coords, color=line_color, weight=5).add_to(m)
    
#     # Markers
#     folium.Marker(st.session_state['map_loc'], popup=f"Origin: {st.session_state['origin_name']}", 
#                   icon=folium.Icon(color='green', icon='home')).add_to(m)
    
#     for i, stop_name in enumerate(active_stops[1:], 1): # Start from 1 to skip origin
#         folium.Marker(nodes[named_nodes[stop_name]], 
#                       popup=f"Stop {i}: {stop_name}",
#                       icon=folium.DivIcon(html=f"""<div style="font-family: sans-serif; color: white; background-color: blue; 
#                                             border-radius: 50%; width: 25px; height: 25px; display: flex; 
#                                             justify-content: center; align-items: center; border: 2px solid white; 
#                                             font-weight: bold; box-shadow: 2px 2px 3px rgba(0,0,0,0.4);">{i}</div>""")
#         ).add_to(m)

#     st_folium(m, width=1200, height=500)














# import streamlit as st
# from streamlit_folium import st_folium
# import folium
# import networkx as nx
# import numpy as np
# from sklearn.cluster import DBSCAN
# import osmium
# from math import radians, cos, sin, sqrt, atan2
# import random
# import time

# # ---------------- 1. Mathematical Helpers ----------------
# def haversine(lat1, lon1, lat2, lon2):
#     R = 6371000 
#     phi1, phi2 = radians(lat1), radians(lat2)
#     dphi, dlambda = radians(lat2 - lat1), radians(lon2 - lon1)
#     a = sin(dphi/2)**2 + cos(phi1)*cos(phi2)*sin(dlambda/2)**2
#     return R * 2 * atan2(sqrt(a), sqrt(1-a))

# # ---------------- 2. OSM Parser ----------------
# class OSMParser(osmium.SimpleHandler):
#     def __init__(self):
#         super().__init__()
#         self.nodes = {}        
#         self.named_nodes = {}  
#         self.graph = nx.Graph()

#     def node(self, n):
#         if not n.location.valid(): return
#         self.nodes[n.id] = (n.location.lat, n.location.lon)
#         if n.tags.get("name"): self.named_nodes[n.tags.get("name")] = n.id

#     def way(self, w):
#         if "highway" in w.tags and len(w.nodes) > 1:
#             for i in range(len(w.nodes) - 1):
#                 n1, n2 = w.nodes[i].ref, w.nodes[i+1].ref
#                 if n1 in self.nodes and n2 in self.nodes:
#                     weight = haversine(*self.nodes[n1], *self.nodes[n2])
#                     self.graph.add_edge(n1, n2, weight=weight)

# def parse_osm_pbf(pbf_file):
#     parser = OSMParser()
#     parser.apply_file(pbf_file)
#     return parser.nodes, parser.named_nodes, parser.graph

# # ---------------- 3. Genetic Algorithm Optimizer ----------------
# class GeneticOptimizer:
#     def __init__(self, graph, points, pop_size=50, generations=100):
#         self.G, self.points = graph, points
#         self.pop_size, self.generations = pop_size, generations
#         self.matrix = self._build_matrix()

#     def _build_matrix(self):
#         sz = len(self.points)
#         mat = np.zeros((sz, sz))
#         for i in range(sz):
#             for j in range(sz):
#                 if i == j: continue
#                 try: 
#                     mat[i][j] = nx.shortest_path_length(self.G, self.points[i], self.points[j], weight='weight')
#                 except: 
#                     mat[i][j] = 1e6
#         return mat

#     def _fitness(self, genome):
#         dist = self.matrix[0][genome[0]]
#         for i in range(len(genome)-1): dist += self.matrix[genome[i]][genome[i+1]]
#         return dist

#     def solve(self):
#         n = len(self.points) - 1
#         if n <= 0: return [0], 0
#         indices = list(range(1, n + 1))
#         pop = [random.sample(indices, n) for _ in range(self.pop_size)]
#         for _ in range(self.generations):
#             pop = sorted(pop, key=self._fitness)
#             new_gen = pop[:5]
#             while len(new_gen) < self.pop_size:
#                 p1, p2 = random.sample(pop[:20], 2)
#                 a, b = sorted(random.sample(range(n), 2))
#                 child = [None]*n
#                 child[a:b] = p1[a:b]
#                 p2_rem = [x for x in p2 if x not in child]
#                 ptr = 0
#                 for i in range(n):
#                     if child[i] is None: child[i] = p2_rem[ptr]; ptr += 1
#                 new_gen.append(child)
#             pop = new_gen
#         best = sorted(pop, key=self._fitness)[0]
#         return [0] + best, self._fitness(best)

# # ---------------- 4. Helper Logic ----------------
# def allocate_resources(total, pop_dict, order):
#     alloc, rem = {z: 0 for z in pop_dict}, total
#     for z in order:
#         a = min(pop_dict[z], rem)
#         alloc[z] = a
#         rem -= a
#     return alloc

# def get_nid(name, nodes, named_nodes, graph):
#     base = named_nodes[name]
#     return min(graph.nodes, key=lambda n: (nodes[base][0]-nodes[n][0])**2 + (nodes[base][1]-nodes[n][1])**2)

# # ---------------- 5. Streamlit App ----------------
# st.set_page_config(layout="wide")
# st.title("🗺️ AIDFlow: Optimized & User-Ordered Multi Stop Disaster Relief Routing and Allocation")

# uploaded_file = st.file_uploader("Upload .osm.pbf file", type=["pbf", "osm.pbf"])
# if not uploaded_file: st.stop()

# with open("uploaded.osm.pbf", "wb") as f: f.write(uploaded_file.read())
# nodes, named_nodes, osm_graph = parse_osm_pbf("uploaded.osm.pbf")

# # Clustering
# coords_arr = np.array([nodes[n] for n in named_nodes.values()])
# clustering = DBSCAN(eps=0.001, min_samples=2).fit(coords_arr)
# # clustering = DBSCAN(eps=1/111, min_samples=2).fit(coords_arr)
# cluster_map = {}
# for lbl, nid in zip(clustering.labels_, named_nodes.values()):
#     if lbl != -1:
#         names = [name for name, i in named_nodes.items() if i == nid]
#         cluster_map.setdefault(lbl, []).extend(names)

# available_clusters = list(cluster_map.keys())
# selected_cluster = st.selectbox("Select a cluster of places:", options=available_clusters, 
#                                 format_func=lambda x: f"Cluster {x} ({len(cluster_map[x])} nodes)")
# cluster_nodes = cluster_map[selected_cluster]

# # Inputs
# origin = st.selectbox("Origin (Depot)", options=cluster_nodes)
# destinations = st.multiselect("Destinations (Selection Order)", options=[n for n in cluster_nodes if n != origin])
# if not origin or not destinations: st.stop()

# pop_per_zone = {z: st.number_input(f"Population: {z}", 1, 1000, 100) for z in destinations}
# t_food = st.number_input("Total Food Kits:", value=500)
# t_med = st.number_input("Total Med Kits:", value=200)
# t_clothes = st.number_input("Total Clothes:", value=300)

# if st.button("Compute & Compare All Methods"):
#     orig_id = get_nid(origin, nodes, named_nodes, osm_graph)
#     dest_name_map = {get_nid(d, nodes, named_nodes, osm_graph): d for d in destinations}
#     dest_ids = list(dest_name_map.keys())
#     all_pts = [orig_id] + dest_ids

#     # 1. User Order
#     u_dist = 0.0
#     for i in range(len(all_pts)-1):
#         try: u_dist += nx.shortest_path_length(osm_graph, all_pts[i], all_pts[i+1], weight='weight')
#         except: u_dist += 1000.0
    
#     # 2. Greedy
#     unvisited = list(dest_ids); curr = orig_id; g_dist = 0; g_stops = [origin]
#     while unvisited:
#         try:
#             nxt = min(unvisited, key=lambda x: nx.shortest_path_length(osm_graph, curr, x, weight='weight'))
#             g_dist += nx.shortest_path_length(osm_graph, curr, nxt, weight='weight')
#             g_stops.append(dest_name_map[nxt]); unvisited.remove(nxt); curr = nxt
#         except:
#             fallback = unvisited.pop(0); g_stops.append(dest_name_map[fallback]); g_dist += 1000.0

#     # 3. Genetic
#     ga = GeneticOptimizer(osm_graph, all_pts)
#     ga_idx, ga_dist = ga.solve()
#     ga_stops = [([origin] + destinations)[i] for i in ga_idx]

#     # Allocation
#     f_a = allocate_resources(t_food, pop_per_zone, destinations)
#     m_a = allocate_resources(t_med, pop_per_zone, destinations)
#     c_a = allocate_resources(t_clothes, pop_per_zone, destinations)

#     def get_coords(path_ids):
#         c = []
#         for i in range(len(path_ids)-1):
#             try:
#                 p = nx.shortest_path(osm_graph, path_ids[i], path_ids[i+1], weight='weight')
#                 c.extend([nodes[n] for n in (p if i==0 else p[1:])])
#             except: continue
#         return c

#     st.session_state.update({
#         'comp': True, 'f_a': f_a, 'm_a': m_a, 'c_a': c_a,
#         'u_order': [origin] + destinations, 'u_dist': u_dist,
#         'g_order': g_stops, 'g_dist': g_dist,
#         'ga_order': ga_stops, 'ga_dist': ga_dist,
#         'ga_coords': get_coords([all_pts[i] for i in ga_idx]),
#         'u_coords': get_coords(all_pts),
#         'map_loc': nodes[orig_id], 'origin_name': origin
#     })

# # Display Results
# if st.session_state.get('comp', False):
#     st.divider()

#     st.subheader("📊 Method Accuracy & Performance Comparison")
#     c1, c2, c3 = st.columns(3)
#     c1.metric("User Manual Dist", f"{st.session_state['u_dist']/1000:.2f} km")
#     c2.metric("Greedy Dist", f"{st.session_state['g_dist']/1000:.2f} km")
#     c3.metric("Genetic Dist", f"{st.session_state['ga_dist']/1000:.2f} km")

#     st.subheader("📍 Detailed Destination Visit Orders")
#     st.success(f"**Genetic Optimizer:** {' → '.join(st.session_state['ga_order'])} | **Dist:** {st.session_state['ga_dist']/1000:.2f} km")
#     st.info(f"**Greedy Optimizer:** {' → '.join(st.session_state['g_order'])} | **Dist:** {st.session_state['g_dist']/1000:.2f} km")
#     st.warning(f"**User Manual Order:** {' → '.join(st.session_state['u_order'])} | **Dist:** {st.session_state['u_dist']/1000:.2f} km")

#     st.subheader("📦 Individual Allocation Outcomes")
#     for z in destinations:
#         st.write(f"**{z}** | Pop: {pop_per_zone[z]} | Food: {st.session_state['f_a'][z]} | Med: {st.session_state['m_a'][z]} | Clothes: {st.session_state['c_a'][z]}")
    
#     # --- ADDED: Resource Deficit Warning Section ---
#     st.subheader("⚠️ Resource Deficit Alerts")
#     any_shortage = False
#     for z in destinations:
#         shortages = []
#         required = pop_per_zone[z]
        
#         # Check Food
#         if st.session_state['f_a'][z] < required:
#             shortages.append(f"Food Kits (Deficit: {required - st.session_state['f_a'][z]})")
        
#         # Check Med
#         if st.session_state['m_a'][z] < required:
#             shortages.append(f"Med Kits (Deficit: {required - st.session_state['m_a'][z]})")
            
#         # Check Clothes
#         if st.session_state['c_a'][z] < required:
#             shortages.append(f"Clothes (Deficit: {required - st.session_state['c_a'][z]})")
            
#         if shortages:
#             st.error(f"**{z}:** Missing resources — {', '.join(shortages)}")
#             any_shortage = True
            
#     if not any_shortage:
#         st.success("✅ All destinations fully supplied based on population demand.")
#     st.divider()
    
#     st.subheader("🗺️ Route Visualization")
#     choice = st.radio("Select View:", ["Genetic Algorithm Path (Optimized)", "User Manual Path"])
#     m = folium.Map(location=st.session_state['map_loc'], zoom_start=15)
    
#     # Legend
#     legend_html = f'''
#     <div style="position: fixed; bottom: 50px; left: 50px; width: 180px; height: 100px; 
#     background-color: black; border:2px solid grey; z-index:9999; font-size:14px; padding: 10px;">
#     <b>Legend</b><br>
#     <i style="background: green; width: 10px; height: 10px; display: inline-block;"></i> {"GA Optimized" if "Genetic" in choice else "User Order"}<br>
#     <i style="color: green; font-weight: bold;">🏠</i> Origin (Depot)<br>
#     <i style="color: blue; font-weight: bold;">📍</i> Numbered Stops
#     </div>
#     '''
#     m.get_root().html.add_child(folium.Element(legend_html))

#     active_coords = st.session_state['ga_coords'] if "Genetic" in choice else st.session_state['u_coords']
#     active_stops = st.session_state['ga_order'] if "Genetic" in choice else st.session_state['u_order']
#     line_color = 'green' if "Genetic" in choice else 'orange'
    
#     if active_coords:
#         folium.PolyLine(active_coords, color=line_color, weight=5).add_to(m)
    
#     # Markers
#     folium.Marker(st.session_state['map_loc'], popup=f"Origin: {st.session_state['origin_name']}", 
#                   icon=folium.Icon(color='green', icon='home')).add_to(m)
    
#     for i, stop_name in enumerate(active_stops[1:], 1): # Start from 1 to skip origin
#         folium.Marker(nodes[named_nodes[stop_name]], 
#                       popup=f"Stop {i}: {stop_name}",
#                       icon=folium.DivIcon(html=f"""<div style="font-family: sans-serif; color: white; background-color: blue; 
#                                             border-radius: 50%; width: 25px; height: 25px; display: flex; 
#                                             justify-content: center; align-items: center; border: 2px solid white; 
#                                             font-weight: bold; box-shadow: 2px 2px 3px rgba(0,0,0,0.4);">{i}</div>""")
#         ).add_to(m)

#     # st_folium(m, width=1200, height=500)





















import streamlit as st
from streamlit_folium import st_folium
import folium
import networkx as nx
import numpy as np
from sklearn.cluster import DBSCAN
import osmium
from math import radians, cos, sin, sqrt, atan2
import random
import time

# ============================================================
# 1. Mathematical Helpers
# ============================================================
def haversine(lat1, lon1, lat2, lon2):
    R = 6371000
    phi1, phi2 = radians(lat1), radians(lat2)
    dphi, dlambda = radians(lat2 - lat1), radians(lon2 - lon1)
    a = sin(dphi/2)**2 + cos(phi1)*cos(phi2)*sin(dlambda/2)**2
    return R * 2 * atan2(sqrt(a), sqrt(1-a))

# ============================================================
# 2. OSM Parser
# ============================================================
class OSMParser(osmium.SimpleHandler):
    def __init__(self):
        super().__init__()
        self.nodes = {}
        self.named_nodes = {}
        self.graph = nx.Graph()

    def node(self, n):
        if not n.location.valid(): return
        self.nodes[n.id] = (n.location.lat, n.location.lon)
        if n.tags.get("name"): self.named_nodes[n.tags.get("name")] = n.id

    def way(self, w):
        if "highway" in w.tags and len(w.nodes) > 1:
            for i in range(len(w.nodes) - 1):
                n1, n2 = w.nodes[i].ref, w.nodes[i+1].ref
                if n1 in self.nodes and n2 in self.nodes:
                    weight = haversine(*self.nodes[n1], *self.nodes[n2])
                    self.graph.add_edge(n1, n2, weight=weight)

def parse_osm_pbf(pbf_file):
    parser = OSMParser()
    parser.apply_file(pbf_file)
    return parser.nodes, parser.named_nodes, parser.graph

# ============================================================
# 3. Genetic Algorithm Optimizer
# ============================================================
class GeneticOptimizer:
    def __init__(self, graph, points, pop_size=50, generations=100):
        self.G, self.points = graph, points
        self.pop_size, self.generations = pop_size, generations
        self.matrix = self._build_matrix()

    def _build_matrix(self):
        sz = len(self.points)
        mat = np.zeros((sz, sz))
        for i in range(sz):
            for j in range(sz):
                if i == j: continue
                try:
                    mat[i][j] = nx.shortest_path_length(self.G, self.points[i], self.points[j], weight='weight')
                except:
                    mat[i][j] = 1e6
        return mat

    def _fitness(self, genome):
        dist = self.matrix[0][genome[0]]
        for i in range(len(genome)-1): dist += self.matrix[genome[i]][genome[i+1]]
        return dist

    def solve(self):
        n = len(self.points) - 1
        if n <= 0: return [0], 0
        indices = list(range(1, n + 1))
        pop = [random.sample(indices, n) for _ in range(self.pop_size)]
        for _ in range(self.generations):
            pop = sorted(pop, key=self._fitness)
            new_gen = pop[:5]
            while len(new_gen) < self.pop_size:
                p1, p2 = random.sample(pop[:20], 2)
                a, b = sorted(random.sample(range(n), 2))
                child = [None]*n
                child[a:b] = p1[a:b]
                p2_rem = [x for x in p2 if x not in child]
                ptr = 0
                for i in range(n):
                    if child[i] is None: child[i] = p2_rem[ptr]; ptr += 1
                new_gen.append(child)
            pop = new_gen
        best = sorted(pop, key=self._fitness)[0]
        return [0] + best, self._fitness(best)

# ============================================================
# 4. Helper Logic
# ============================================================
def allocate_resources(total, pop_dict, order):
    alloc, rem = {z: 0 for z in pop_dict}, total
    for z in order:
        a = min(pop_dict[z], rem)
        alloc[z] = a
        rem -= a
    return alloc

def get_nid(name, nodes, named_nodes, graph):
    base = named_nodes[name]
    return min(graph.nodes, key=lambda n: (nodes[base][0]-nodes[n][0])**2 + (nodes[base][1]-nodes[n][1])**2)

# ============================================================
# 5. Page Config & Global CSS
# ============================================================
st.set_page_config(
    page_title="AIDFlow — Relief Command Center",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@400;500;600;700&family=Share+Tech+Mono&family=Exo+2:wght@300;400;600;800&display=swap');

/* ---- Base Reset ---- */
html, body, [class*="css"] {
    font-family: 'Exo 2', sans-serif;
    background-color: #070b12;
    color: #c8d8e8;
}

.stApp {
    background: #070b12;
    background-image:
        radial-gradient(ellipse 80% 60% at 50% -10%, rgba(0, 180, 255, 0.07) 0%, transparent 70%),
        linear-gradient(180deg, #070b12 0%, #0a1020 100%);
}

/* ---- Hide Streamlit chrome ---- */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1.5rem; padding-bottom: 2rem; max-width: 1400px; }

/* ---- Header Banner ---- */
.aidflow-header {
    position: relative;
    padding: 2.2rem 2.5rem 2rem;
    margin-bottom: 2rem;
    background: linear-gradient(135deg, #0d1829 0%, #091523 100%);
    border: 1px solid rgba(0, 180, 255, 0.2);
    border-left: 4px solid #00b4ff;
    border-radius: 4px;
    overflow: hidden;
}
.aidflow-header::before {
    content: "";
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: repeating-linear-gradient(
        0deg,
        transparent,
        transparent 39px,
        rgba(0,180,255,0.03) 39px,
        rgba(0,180,255,0.03) 40px
    );
    pointer-events: none;
}
.aidflow-header::after {
    content: "SYSTEM ACTIVE";
    position: absolute;
    top: 14px; right: 20px;
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.18em;
    color: #00ff88;
    opacity: 0.7;
}
.aidflow-title {
    font-family: 'Rajdhani', sans-serif;
    font-size: 2.4rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    color: #ffffff;
    line-height: 1;
    text-transform: uppercase;
    margin: 0;
}
.aidflow-title span { color: #00b4ff; }
.aidflow-subtitle {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.2em;
    color: #4a7a9b;
    margin-top: 0.5rem;
    text-transform: uppercase;
}
.status-pill {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    margin-top: 0.9rem;
    padding: 4px 12px;
    background: rgba(0, 255, 136, 0.08);
    border: 1px solid rgba(0, 255, 136, 0.25);
    border-radius: 2px;
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.15em;
    color: #00ff88;
    text-transform: uppercase;
}
.status-dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: #00ff88;
    box-shadow: 0 0 6px #00ff88;
    animation: pulse-dot 1.8s ease-in-out infinite;
}
@keyframes pulse-dot {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.4; transform: scale(0.7); }
}

/* ---- Section Headers ---- */
.section-header {
    display: flex;
    align-items: center;
    gap: 10px;
    margin: 1.8rem 0 0.9rem;
    padding-bottom: 8px;
    border-bottom: 1px solid rgba(0, 180, 255, 0.15);
}
.section-header-num {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.65rem;
    color: #00b4ff;
    letter-spacing: 0.1em;
    opacity: 0.6;
}
.section-header-title {
    font-family: 'Rajdhani', sans-serif;
    font-size: 1.05rem;
    font-weight: 600;
    letter-spacing: 0.12em;
    color: #d0e8f8;
    text-transform: uppercase;
}
.section-tag {
    margin-left: auto;
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.6rem;
    color: #2a4a6b;
    letter-spacing: 0.1em;
}

/* ---- Upload Zone ---- */
[data-testid="stFileUploader"] {
    background: rgba(0, 30, 60, 0.5) !important;
    border: 1px dashed rgba(0, 180, 255, 0.3) !important;
    border-radius: 4px !important;
    padding: 1rem !important;
    transition: border-color 0.2s;
}
[data-testid="stFileUploader"]:hover {
    border-color: rgba(0, 180, 255, 0.6) !important;
}

/* ---- Selectbox & Multiselect ---- */
[data-testid="stSelectbox"] > div > div,
[data-testid="stMultiSelect"] > div > div {
    background: rgba(0, 20, 45, 0.8) !important;
    border: 1px solid rgba(0, 180, 255, 0.2) !important;
    border-radius: 3px !important;
    color: #c8d8e8 !important;
    font-family: 'Exo 2', sans-serif !important;
}
[data-testid="stSelectbox"] > div > div:hover,
[data-testid="stMultiSelect"] > div > div:hover {
    border-color: rgba(0, 180, 255, 0.5) !important;
}

/* ---- Number Inputs ---- */
[data-testid="stNumberInput"] input {
    background: rgba(0, 20, 45, 0.8) !important;
    border: 1px solid rgba(0, 180, 255, 0.2) !important;
    border-radius: 3px !important;
    color: #c8d8e8 !important;
    font-family: 'Share Tech Mono', monospace !important;
}

/* ---- Labels ---- */
label, .stSelectbox label, .stMultiSelect label, .stNumberInput label {
    font-family: 'Rajdhani', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.8rem !important;
    letter-spacing: 0.12em !important;
    color: #4a7a9b !important;
    text-transform: uppercase !important;
}

/* ---- Compute Button ---- */
[data-testid="stButton"] > button {
    width: 100%;
    padding: 0.85rem 2rem;
    background: linear-gradient(135deg, #003d6b 0%, #005a99 100%);
    border: 1px solid rgba(0, 180, 255, 0.4) !important;
    border-radius: 3px;
    color: #ffffff !important;
    font-family: 'Rajdhani', sans-serif !important;
    font-size: 1rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.2em !important;
    text-transform: uppercase !important;
    transition: all 0.2s ease;
    box-shadow: 0 0 20px rgba(0, 100, 200, 0.15), inset 0 1px 0 rgba(255,255,255,0.05);
    position: relative;
    overflow: hidden;
}
[data-testid="stButton"] > button::before {
    content: "";
    position: absolute;
    top: 0; left: -100%;
    width: 100%; height: 100%;
    background: linear-gradient(90deg, transparent, rgba(0,180,255,0.15), transparent);
    transition: left 0.4s ease;
}
[data-testid="stButton"] > button:hover {
    border-color: rgba(0, 180, 255, 0.8) !important;
    box-shadow: 0 0 30px rgba(0, 140, 255, 0.3), 0 0 8px rgba(0, 180, 255, 0.2) !important;
    transform: translateY(-1px);
}
[data-testid="stButton"] > button:hover::before { left: 100%; }

/* ---- Metric Cards ---- */
[data-testid="stMetricValue"] {
    font-family: 'Share Tech Mono', monospace !important;
    font-size: 1.7rem !important;
    color: #00b4ff !important;
}
[data-testid="stMetricLabel"] {
    font-family: 'Rajdhani', sans-serif !important;
    font-size: 0.75rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.15em !important;
    color: #4a7a9b !important;
    text-transform: uppercase !important;
}
[data-testid="stMetric"] {
    background: rgba(0, 20, 45, 0.7) !important;
    border: 1px solid rgba(0, 180, 255, 0.15) !important;
    border-radius: 4px !important;
    padding: 1rem 1.2rem !important;
    position: relative;
    overflow: hidden;
}
[data-testid="stMetric"]::before {
    content: "";
    position: absolute;
    top: 0; left: 0;
    width: 3px; height: 100%;
    background: linear-gradient(180deg, #00b4ff, #0040a0);
}

/* ---- Alert Boxes ---- */
[data-testid="stSuccess"] {
    background: rgba(0, 60, 30, 0.5) !important;
    border: 1px solid rgba(0, 255, 136, 0.25) !important;
    border-left: 3px solid #00ff88 !important;
    border-radius: 3px !important;
    font-family: 'Share Tech Mono', monospace !important;
    font-size: 0.78rem !important;
    color: #a0ffcc !important;
}
[data-testid="stInfo"] {
    background: rgba(0, 40, 80, 0.5) !important;
    border: 1px solid rgba(0, 180, 255, 0.25) !important;
    border-left: 3px solid #00b4ff !important;
    border-radius: 3px !important;
    font-family: 'Share Tech Mono', monospace !important;
    font-size: 0.78rem !important;
    color: #a0d8ff !important;
}
[data-testid="stWarning"] {
    background: rgba(60, 40, 0, 0.5) !important;
    border: 1px solid rgba(255, 180, 0, 0.25) !important;
    border-left: 3px solid #ffb800 !important;
    border-radius: 3px !important;
    font-family: 'Share Tech Mono', monospace !important;
    font-size: 0.78rem !important;
    color: #ffe080 !important;
}
[data-testid="stError"] {
    background: rgba(80, 0, 0, 0.5) !important;
    border: 1px solid rgba(255, 60, 60, 0.25) !important;
    border-left: 3px solid #ff3c3c !important;
    border-radius: 3px !important;
    font-family: 'Share Tech Mono', monospace !important;
    font-size: 0.78rem !important;
    color: #ffaaaa !important;
}

/* ---- Divider ---- */
hr {
    border: none !important;
    border-top: 1px solid rgba(0, 180, 255, 0.1) !important;
    margin: 2rem 0 !important;
}

/* ---- Allocation Grid Cards ---- */
.alloc-card {
    background: rgba(0, 20, 45, 0.6);
    border: 1px solid rgba(0, 180, 255, 0.12);
    border-radius: 4px;
    padding: 0.9rem 1.1rem;
    margin-bottom: 0.6rem;
    display: flex;
    align-items: center;
    gap: 1rem;
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.75rem;
    transition: border-color 0.2s;
}
.alloc-card:hover { border-color: rgba(0, 180, 255, 0.3); }
.alloc-zone {
    font-family: 'Rajdhani', sans-serif;
    font-weight: 700;
    font-size: 0.9rem;
    color: #d0e8f8;
    letter-spacing: 0.05em;
    min-width: 140px;
}
.alloc-badge {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    padding: 2px 8px;
    border-radius: 2px;
    font-size: 0.68rem;
    letter-spacing: 0.05em;
}
.badge-food  { background: rgba(0,140,80,0.2);  border: 1px solid rgba(0,200,100,0.3);  color: #60e8a0; }
.badge-med   { background: rgba(0,100,200,0.2); border: 1px solid rgba(0,150,255,0.3);  color: #70c8ff; }
.badge-cloth { background: rgba(150,80,200,0.2);border: 1px solid rgba(180,100,255,0.3);color: #d0a0ff; }
.badge-pop   { background: rgba(100,100,100,0.2);border: 1px solid rgba(150,150,150,0.3);color: #a0b0c0; }

/* ---- Radio ---- */
[data-testid="stRadio"] label {
    font-family: 'Exo 2', sans-serif !important;
    font-size: 0.82rem !important;
    color: #8aaccc !important;
    text-transform: none !important;
    letter-spacing: 0 !important;
}
[data-testid="stRadio"] > div {
    gap: 1.5rem !important;
}

/* ---- Scrollbar ---- */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: #070b12; }
::-webkit-scrollbar-thumb { background: #1a3a5a; border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: #2a5a8a; }
</style>
""", unsafe_allow_html=True)

# ============================================================
# Header
# ============================================================
st.markdown("""
<div class="aidflow-header">
    <div class="aidflow-title">AID<span>FLOW</span></div>
    <div class="aidflow-subtitle">Optimized Multi-Stop Disaster Relief Routing &amp; Allocation System</div>
    <div class="status-pill">
        <div class="status-dot"></div>
        Command Center Online
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# File Upload
# ============================================================
st.markdown("""
<div class="section-header">
    <span class="section-header-num">01 //</span>
    <span class="section-header-title">Data Ingestion</span>
    <span class="section-tag">OSM_PBF_IMPORT</span>
</div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload .osm.pbf Map File", type=["pbf", "osm.pbf"])
if not uploaded_file:
    st.markdown("""
    <div style="padding: 1.2rem; background: rgba(0,180,255,0.04); border: 1px dashed rgba(0,180,255,0.15); 
    border-radius: 4px; font-family: 'Share Tech Mono', monospace; font-size: 0.72rem; color: #2a5a7a;
    letter-spacing: 0.08em; text-align: center;">
    ⬆ AWAITING MAP DATA — UPLOAD AN .OSM.PBF FILE TO INITIALIZE
    </div>
    """, unsafe_allow_html=True)
    st.stop()

with open("uploaded.osm.pbf", "wb") as f: f.write(uploaded_file.read())
nodes, named_nodes, osm_graph = parse_osm_pbf("uploaded.osm.pbf")

# ============================================================
# Clustering & Cluster Selection
# ============================================================
coords_arr = np.array([nodes[n] for n in named_nodes.values()])
clustering = DBSCAN(eps=0.001, min_samples=2).fit(coords_arr)
cluster_map = {}
for lbl, nid in zip(clustering.labels_, named_nodes.values()):
    if lbl != -1:
        names = [name for name, i in named_nodes.items() if i == nid]
        cluster_map.setdefault(lbl, []).extend(names)

available_clusters = list(cluster_map.keys())

st.markdown("""
<div class="section-header">
    <span class="section-header-num">02 //</span>
    <span class="section-header-title">Zone Configuration</span>
    <span class="section-tag">CLUSTER_SELECT</span>
</div>
""", unsafe_allow_html=True)

selected_cluster = st.selectbox(
    "Select Operational Cluster",
    options=available_clusters,
    format_func=lambda x: f"Cluster {x}  ·  {len(cluster_map[x])} nodes detected"
)
cluster_nodes = cluster_map[selected_cluster]

col_orig, col_dest = st.columns([1, 2])
with col_orig:
    origin = st.selectbox("Origin / Depot Node", options=cluster_nodes)
with col_dest:
    destinations = st.multiselect("Destination Nodes (selection defines manual order)", options=[n for n in cluster_nodes if n != origin])

if not origin or not destinations: st.stop()

# ============================================================
# Population & Resource Inputs
# ============================================================
st.markdown("""
<div class="section-header">
    <span class="section-header-num">03 //</span>
    <span class="section-header-title">Population &amp; Resource Parameters</span>
    <span class="section-tag">RESOURCE_ALLOC</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<p style="font-family: 'Share Tech Mono', monospace; font-size: 0.68rem; 
color: #2a5a7a; letter-spacing: 0.1em; margin-bottom: 0.8rem; text-transform: uppercase;">
▸ Population estimates per zone
</p>
""", unsafe_allow_html=True)

pop_per_zone = {}
pop_cols = st.columns(min(len(destinations), 4))
for i, z in enumerate(destinations):
    with pop_cols[i % len(pop_cols)]:
        pop_per_zone[z] = st.number_input(f"Pop · {z[:18]}", 1, 1000, 100, key=f"pop_{z}")

st.markdown("""
<p style="font-family: 'Share Tech Mono', monospace; font-size: 0.68rem; 
color: #2a5a7a; letter-spacing: 0.1em; margin: 1rem 0 0.6rem; text-transform: uppercase;">
▸ Total resource inventories
</p>
""", unsafe_allow_html=True)

res_col1, res_col2, res_col3 = st.columns(3)
with res_col1:
    t_food = st.number_input("🍱 Total Food Kits", value=500)
with res_col2:
    t_med = st.number_input("💊 Total Med Kits", value=200)
with res_col3:
    t_clothes = st.number_input("🧥 Total Clothes", value=300)

# ============================================================
# Compute Button
# ============================================================
st.markdown("<div style='margin: 1.8rem 0 0.5rem;'>", unsafe_allow_html=True)
run = st.button("⚡ COMPUTE & COMPARE ALL ROUTING METHODS")
st.markdown("</div>", unsafe_allow_html=True)

if run:
    orig_id = get_nid(origin, nodes, named_nodes, osm_graph)
    dest_name_map = {get_nid(d, nodes, named_nodes, osm_graph): d for d in destinations}
    dest_ids = list(dest_name_map.keys())
    all_pts = [orig_id] + dest_ids

    with st.spinner("Computing routes — running genetic optimizer..."):
        # 1. User Order
        u_dist = 0.0
        for i in range(len(all_pts)-1):
            try: u_dist += nx.shortest_path_length(osm_graph, all_pts[i], all_pts[i+1], weight='weight')
            except: u_dist += 1000.0

        # 2. Greedy
        unvisited = list(dest_ids); curr = orig_id; g_dist = 0; g_stops = [origin]
        while unvisited:
            try:
                nxt = min(unvisited, key=lambda x: nx.shortest_path_length(osm_graph, curr, x, weight='weight'))
                g_dist += nx.shortest_path_length(osm_graph, curr, nxt, weight='weight')
                g_stops.append(dest_name_map[nxt]); unvisited.remove(nxt); curr = nxt
            except:
                fallback = unvisited.pop(0); g_stops.append(dest_name_map[fallback]); g_dist += 1000.0

        # 3. Genetic
        ga = GeneticOptimizer(osm_graph, all_pts)
        ga_idx, ga_dist = ga.solve()
        ga_stops = [([origin] + destinations)[i] for i in ga_idx]

    # Allocation
    f_a = allocate_resources(t_food, pop_per_zone, destinations)
    m_a = allocate_resources(t_med, pop_per_zone, destinations)
    c_a = allocate_resources(t_clothes, pop_per_zone, destinations)

    def get_coords(path_ids):
        c = []
        for i in range(len(path_ids)-1):
            try:
                p = nx.shortest_path(osm_graph, path_ids[i], path_ids[i+1], weight='weight')
                c.extend([nodes[n] for n in (p if i==0 else p[1:])])
            except: continue
        return c

    st.session_state.update({
        'comp': True, 'f_a': f_a, 'm_a': m_a, 'c_a': c_a,
        'u_order': [origin] + destinations, 'u_dist': u_dist,
        'g_order': g_stops, 'g_dist': g_dist,
        'ga_order': ga_stops, 'ga_dist': ga_dist,
        'ga_coords': get_coords([all_pts[i] for i in ga_idx]),
        'u_coords': get_coords(all_pts),
        'map_loc': nodes[orig_id], 'origin_name': origin,
        'pop_per_zone': pop_per_zone, 'destinations': destinations
    })

# ============================================================
# Results
# ============================================================
if st.session_state.get('comp', False):
    _dest    = st.session_state['destinations']
    _pop     = st.session_state['pop_per_zone']
    _f_a     = st.session_state['f_a']
    _m_a     = st.session_state['m_a']
    _c_a     = st.session_state['c_a']
    _u_dist  = st.session_state['u_dist']
    _g_dist  = st.session_state['g_dist']
    _ga_dist = st.session_state['ga_dist']

    st.markdown("<hr/>", unsafe_allow_html=True)

    # ---- Metrics ----
    st.markdown("""
    <div class="section-header">
        <span class="section-header-num">04 //</span>
        <span class="section-header-title">Routing Performance Analysis</span>
        <span class="section-tag">ALGO_BENCHMARK</span>
    </div>
    """, unsafe_allow_html=True)

    mc1, mc2, mc3 = st.columns(3)
    mc1.metric("👤 Manual Route", f"{_u_dist/1000:.2f} km", delta=f"+{(_u_dist - _ga_dist)/1000:.2f} km vs GA")
    mc2.metric("⚡ Greedy Route", f"{_g_dist/1000:.2f} km", delta=f"+{(_g_dist - _ga_dist)/1000:.2f} km vs GA")
    mc3.metric("🧬 Genetic Optimized", f"{_ga_dist/1000:.2f} km", delta="Best Route")

    # ---- Route Orders ----
    st.markdown("""
    <div class="section-header" style="margin-top: 1.8rem;">
        <span class="section-header-num">05 //</span>
        <span class="section-header-title">Computed Visit Sequences</span>
        <span class="section-tag">ROUTE_DETAIL</span>
    </div>
    """, unsafe_allow_html=True)

    st.success(f"🧬 GENETIC OPTIMIZER  ·  {' → '.join(st.session_state['ga_order'])}  ·  {_ga_dist/1000:.2f} km")
    st.info(f"⚡ GREEDY OPTIMIZER  ·  {' → '.join(st.session_state['g_order'])}  ·  {_g_dist/1000:.2f} km")
    st.warning(f"👤 MANUAL ORDER  ·  {' → '.join(st.session_state['u_order'])}  ·  {_u_dist/1000:.2f} km")

    # ---- Allocation ----
    st.markdown("""
    <div class="section-header" style="margin-top: 1.8rem;">
        <span class="section-header-num">06 //</span>
        <span class="section-header-title">Individual Allocation Outcomes</span>
        <span class="section-tag">RESOURCE_MAP</span>
    </div>
    """, unsafe_allow_html=True)

    for z in _dest:
        st.markdown(f"""
        <div class="alloc-card">
            <div class="alloc-zone">{z}</div>
            <span class="alloc-badge badge-pop">👥 {_pop[z]} pop</span>
            <span class="alloc-badge badge-food">🍱 Food {_f_a[z]}</span>
            <span class="alloc-badge badge-med">💊 Med {_m_a[z]}</span>
            <span class="alloc-badge badge-cloth">🧥 Clothes {_c_a[z]}</span>
        </div>
        """, unsafe_allow_html=True)

    # ---- Deficit Alerts ----
    st.markdown("""
    <div class="section-header" style="margin-top: 1.8rem;">
        <span class="section-header-num">07 //</span>
        <span class="section-header-title">Resource Deficit Alerts</span>
        <span class="section-tag">SHORTAGE_SCAN</span>
    </div>
    """, unsafe_allow_html=True)

    any_shortage = False
    for z in _dest:
        shortages = []
        required = _pop[z]
        if _f_a[z] < required: shortages.append(f"Food Kits (Deficit: {required - _f_a[z]})")
        if _m_a[z] < required: shortages.append(f"Med Kits (Deficit: {required - _m_a[z]})")
        if _c_a[z] < required: shortages.append(f"Clothes (Deficit: {required - _c_a[z]})")
        if shortages:
            st.error(f"⚠ {z}  —  {', '.join(shortages)}")
            any_shortage = True

    if not any_shortage:
        st.success("✅ ALL DESTINATIONS FULLY SUPPLIED — No shortages detected.")

    st.markdown("<hr/>", unsafe_allow_html=True)

    # ---- Map ----
    st.markdown("""
    <div class="section-header">
        <span class="section-header-num">08 //</span>
        <span class="section-header-title">Route Visualization</span>
        <span class="section-tag">GEO_RENDER</span>
    </div>
    """, unsafe_allow_html=True)

    choice = st.radio(
        "Select route to visualize:",
        ["Genetic Algorithm Path (Optimized)", "User Manual Path"],
        horizontal=True
    )

    m = folium.Map(
        location=st.session_state['map_loc'],
        zoom_start=15,
        tiles="CartoDB dark_matter"
    )

    legend_html = f'''
    <div style="position: fixed; bottom: 50px; left: 50px; width: 190px;
    background: rgba(7,11,18,0.92); border: 1px solid rgba(0,180,255,0.3);
    border-left: 3px solid #00b4ff; z-index: 9999; font-size: 12px;
    padding: 12px 14px; font-family: monospace; color: #a0c8e8; border-radius: 3px;">
    <div style="font-weight:bold; color:#00b4ff; letter-spacing:0.1em; 
    font-size:10px; margin-bottom:8px; text-transform:uppercase;">Legend</div>
    <div style="margin-bottom:4px;">
    <span style="color:{'#00ff88' if 'Genetic' in choice else '#ffb800'}; font-weight:bold;">━</span>
    {'GA Optimized' if 'Genetic' in choice else 'Manual Route'}</div>
    <div style="margin-bottom:4px;"><span style="color:#00ff88;">⬟</span> Origin Depot</div>
    <div><span style="color:#00b4ff;">◉</span> Numbered Stops</div>
    </div>'''
    m.get_root().html.add_child(folium.Element(legend_html))

    active_coords = st.session_state['ga_coords'] if "Genetic" in choice else st.session_state['u_coords']
    active_stops  = st.session_state['ga_order'] if "Genetic" in choice else st.session_state['u_order']
    line_color    = '#00ff88' if "Genetic" in choice else '#ffb800'

    if active_coords:
        folium.PolyLine(
            active_coords,
            color=line_color,
            weight=4,
            opacity=0.85,
            dash_array=None
        ).add_to(m)

    # Origin marker
    folium.Marker(
        st.session_state['map_loc'],
        popup=folium.Popup(f"<b>DEPOT:</b> {st.session_state['origin_name']}", max_width=200),
        icon=folium.DivIcon(html=f"""
            <div style="
                width: 28px; height: 28px; background: #00ff88;
                border: 2px solid #ffffff; border-radius: 4px;
                display: flex; align-items: center; justify-content: center;
                font-weight: bold; font-size: 13px; color: #070b12;
                box-shadow: 0 0 12px rgba(0,255,136,0.6);">D</div>""")
    ).add_to(m)

    # Stop markers
    for i, stop_name in enumerate(active_stops[1:], 1):
        folium.Marker(
            nodes[named_nodes[stop_name]],
            popup=folium.Popup(f"<b>STOP {i}:</b> {stop_name}", max_width=200),
            icon=folium.DivIcon(html=f"""
                <div style="
                    width: 26px; height: 26px; background: #003d6b;
                    border: 2px solid #00b4ff; border-radius: 50%;
                    display: flex; align-items: center; justify-content: center;
                    font-family: monospace; font-weight: bold; font-size: 11px;
                    color: #00b4ff;
                    box-shadow: 0 0 10px rgba(0,180,255,0.5);">{i}</div>""")
        ).add_to(m)

    st_folium(m, width=1300, height=520)