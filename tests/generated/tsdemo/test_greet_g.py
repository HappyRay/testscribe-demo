from tsdemo.greet import Greeter


def test_greet():
    instance = Greeter(my_name='Bob')
    result = instance.greet(to='Alice')
    assert result == 'Hello Alice. My name is Bob'
