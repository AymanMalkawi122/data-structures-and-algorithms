import pytest
from solutions.graph.solution import Graph

def test_add_vertex():
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")

    assert graph.get_vertices() == ["A", "B", "C"]

def test_add_edge():
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_edge("A", "B", 2)

    assert graph.get_neighbors("A") == {"B": 2}
    assert graph.get_neighbors("B") == {"A": 2}

def test_get_vertices():
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")

    assert graph.get_vertices() == ["A", "B", "C"]

def test_get_neighbors():
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_edge("A", "B", 2)

    assert graph.get_neighbors("A") == {"B": 2}
    assert graph.get_neighbors("B") == {"A": 2}

def test_size():
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")

    assert graph.size() == 3

def test_single_vertex_and_edge():
    graph = Graph()
    graph.add_vertex("A")
    graph.add_edge("A", "A", 5)

    assert graph.get_vertices() == ["A"]
    assert graph.get_neighbors("A") == {"A": 5}
    assert graph.size() == 1