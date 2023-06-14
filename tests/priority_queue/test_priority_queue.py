from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    """Aqui irá sua implementação"""
    priority = PriorityQueue()
    priority.enqueue({"qtd_linhas": 3})
    priority.enqueue({"qtd_linhas": 2})
    priority.enqueue({"qtd_linhas": 10})
    priority.enqueue({"qtd_linhas": 4})
    assert priority.dequeue() == {"qtd_linhas": 3}
    assert priority.search(0) == {"qtd_linhas": 4}
    with pytest.raises(IndexError):
        priority.search(1)
