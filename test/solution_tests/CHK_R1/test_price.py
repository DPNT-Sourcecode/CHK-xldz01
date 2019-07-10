from lib.solutions.CHK import checkout_solution


class TestSum:
    def test_checkout(self):
        assert checkout_solution.checkout("AAA") == 130
        assert checkout_solution.checkout("BB") == 45
        assert checkout_solution.checkout("") == 0
        assert checkout_solution.checkout("a") == -1


