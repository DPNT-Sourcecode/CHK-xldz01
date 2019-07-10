from lib.solutions.CHK import checkout_solution


class TestSum:
    def test_checkout(self):
        assert checkout_solution.checkout("AAA") == 130
        assert checkout_solution.checkout("BB") == 130

