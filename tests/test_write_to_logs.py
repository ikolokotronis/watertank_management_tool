from unittest.mock import patch, mock_open
from classes.event_sourcer import EventSourcer
from enums.states import States
from factories.tank_factory import TankFactory


@patch("builtins.open", new_callable=mock_open)
def test_patch(mock_file):
    func = EventSourcer.write_to_logs
    tank = TankFactory.produce('some_tank_name', 500)
    sample_state = {
        "operation_name": 'some_operation_name',
        "tank": tank,
        "operation_type": 'refill',
        "water_volume": 500,
        "status": States.SUCCESS
    }
    assert_arg = f"Operation name: {'some_operation_name'}\n"\
    f"Operation status: {States.SUCCESS}\n"\
    f"Operation type: 'refill'\n"\
    f"Tank: {tank.name}\n"\
    f"Water volume: {500}\n"
    func_result = func(sample_state)
    mock_file.assert_called_with("../content/logs.txt", 'a')
    mock_file.return_value.write.assert_called_with(assert_arg)
    assert func_result == States.SUCCESS


def test_should_return_correct_for_sample_state():
    func = EventSourcer.write_to_logs
    tank = TankFactory.produce('some_tank_name', 500)
    sample_state = {
            "operation_name": 'some_operation_name',
            "tank": tank,
            "operation_type": 'refill',
            "water_volume": 500,
            "status": States.SUCCESS
        }

    assert func(sample_state)
