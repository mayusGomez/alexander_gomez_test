import pytest
from unittest import mock

from datetime import datetime, timedelta

from ...trlu_cache_server.model.tlru_cache import TLRU_Cache
from ...trlu_cache_server.model.node import Node
from ...trlu_cache_server.use_cases.tlru_interact import TLRU_Interaction
from ...trlu_cache_server.use_cases.response import Response


@pytest.fixture
def load_cache():
    tlru = TLRU_Cache()

    node_3 = Node(
        key='z',
        time_stamp= datetime.now(), 
        due_date= datetime(2019,1,1,0,30,0,00000), 
        value=1, 
        next_node=None, 
        previous_node=None
    )

    node_2 = Node(
        key='y',
        time_stamp= datetime.now(), 
        due_date= datetime(2019,1,1,0,30,0,00000), 
        value=1, 
        next_node=None, 
        previous_node=None
    )

    node_1 = Node(
        key='x',
        time_stamp= datetime.now(), 
        due_date= datetime(2019,1,1,7,30,0,00000), 
        value=1, 
        next_node=None, 
        previous_node=None
    )

    node_1.next_node = node_2
    node_2.previous_node = node_1
    node_2.next_node = node_3
    node_3.previous_node = node_2

    tlru.setters = {
        node_1.key: node_1,
        node_2.key: node_2,
        node_3.key: node_3
    }

    tlru.head = node_1
    tlru.tail = node_3

    return tlru


def test_get_item_with_re_order_data_success(load_cache):
    data = mock.Mock()
    data.get_tlru_cache.return_value = load_cache

    tlru_use_case = TLRU_Interaction(data)
    response = tlru_use_case.get_node('z')

    # tlru_use_case = TLRU_Interaction(data)
    list_keys = tlru_use_case.list_keys(max_iter=10)

    assert response.type_response == Response.SUCCESS
    assert response.value.value == 1
    assert list_keys == ['x','z','y']


def test_get_item_with_re_order_data_fail(load_cache):
    data = mock.Mock()
    data.get_tlru_cache.return_value = load_cache

    tlru_use_case = TLRU_Interaction(data)
    response = tlru_use_case.get_node('m')

    assert response.type_response == Response.FAIL


def test_set_items(load_cache):
    data = mock.Mock()
    data.get_tlru_cache.return_value = load_cache
    tlru_use_case = TLRU_Interaction(data)
    response = tlru_use_case.get_node(
        key='a', 
        time_stamp=datetime.now(), 
        due_date=datetime(2019,1,1,7,30,0,00000), 
        value=45
    )

    
