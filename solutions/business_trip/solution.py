def business_trip(graph, city_names):
    """
    Determine whether a trip is possible with direct flights between cities and calculate the total cost.

    Args:
        graph (Graph): The graph representing cities and their direct flights.
        city_names (list): An array of city names in the order of the planned trip.

    Returns:
        int or None: The total cost of the trip if it's possible with direct flights, or None if not possible.
    """
    total_cost = 0

    for i in range(len(city_names) - 1):
        current_city = city_names[i]
        next_city = city_names[i + 1]

        neighbors = graph.vertices_map.get(current_city)
        if neighbors and next_city in neighbors:
            total_cost += neighbors[next_city]
        else:
            return None

    return total_cost