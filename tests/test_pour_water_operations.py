from factories.tank_factory import TankFactory


def test_should_return_correct_for_pour_water_operations():
    tank = TankFactory.produce('test_tank', 500)
    assert tank.water_volume == 0
    tank.pour_water(500)
    assert tank.water_volume == 500


def test_should_return_correct_for_pour_water_and_pour_out_water_operations():
    tank = TankFactory.produce('test_tank', 500)
    assert tank.water_volume == 0
    tank.pour_water(500)
    assert tank.water_volume == 500
    tank.pour_out_water(300)
    assert tank.water_volume == 200


def test_should_return_incorrect_for_wrong_calculations():
    tank = TankFactory.produce('test_tank', 500)
    assert tank.water_volume == 0
    tank.pour_water(500)
    assert tank.water_volume == 500
    tank.pour_out_water(200)
    assert tank.water_volume != 200


def test_should_return_incorrect_starting_volume_different_than_0():
    tank = TankFactory.produce('test_tank', 500)
    assert tank.water_volume != 50
