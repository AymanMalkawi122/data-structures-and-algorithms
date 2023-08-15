import pytest
from solutions.graph.solution import Graph
from solutions.business_trip.solution import business_trip
def test_business_trip_possible_direct_flights():
    graph = Graph()
    graph.add_vertex("Metroville")
    graph.add_vertex("Pandora")
    graph.add_vertex("Arendelle")
    graph.add_vertex("New Monstropolis")
    graph.add_vertex("Naboo")
    
    graph.add_edge("Metroville", "Pandora", 82)
    graph.add_edge("Arendelle", "New Monstropolis", 115)
    graph.add_edge("New Monstropolis", "Metroville", 1)

    assert business_trip(graph, ["Metroville", "Pandora"]) == 82
    assert business_trip(graph, ["Arendelle", "New Monstropolis", "Metroville"]) == 116
    assert business_trip(graph, ["Arendelle", "New Monstropolis", "Metroville", "Pandora"]) == 198

def test_business_trip_not_possible_direct_flights():
    graph = Graph()
    graph.add_vertex("Naboo")
    graph.add_vertex("Pandora")

    assert business_trip(graph, ["Naboo", "Pandora"]) is None
    assert business_trip(graph, ["Narnia", "Pandora"]) is None

def test_business_trip_single_city():
    graph = Graph()
    graph.add_vertex("A")

    assert business_trip(graph, ["A"]) == 0

def test_business_trip_empty_graph():
    graph = Graph()

    assert business_trip(graph, ["A", "B"]) is None