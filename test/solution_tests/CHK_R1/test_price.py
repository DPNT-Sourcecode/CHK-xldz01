from lib.solutions.CHK import checkout_solution


class TestSum:
    def test_checkout(self):
        assert checkout_solution.checkout("AAA") == 130
        assert checkout_solution.checkout("BB") == 45
        assert checkout_solution.checkout("") == 0
        assert checkout_solution.checkout("a") == -1
        assert checkout_solution.checkout("B") == 30
        assert checkout_solution.checkout("ABCD") == 115
        assert checkout_solution.checkout("ABCDE") == 155
        assert checkout_solution.checkout("ACDEE") == 165
        assert checkout_solution.checkout("ACDEEBBA") == 245
        assert checkout_solution.checkout("ACDEEBBAA") == 275
        assert checkout_solution.checkout("AAAAACDEEBB") == 345
        assert checkout_solution.checkout("EEEEBB") == 160
        assert checkout_solution.checkout("AAAAAAAAA") == 380
        assert checkout_solution.checkout("AAAAAAAA") == 330
        assert checkout_solution.checkout("AAAAAAAA") == 330
        assert checkout_solution.checkout("FF") == 20
        assert checkout_solution.checkout("FFF") == 20
        assert checkout_solution.checkout("FFFF") == 30
        assert checkout_solution.checkout("F") == 10
        assert checkout_solution.checkout("FFFFFF") == 40
        assert checkout_solution.checkout("XXX") == 45
        assert checkout_solution.checkout("YYY") == 45
        assert checkout_solution.checkout("SSS") == 45
        assert checkout_solution.checkout("TTT") == 45
        assert checkout_solution.checkout("ZZZ") == 45
        assert checkout_solution.checkout("X") == 17
        assert checkout_solution.checkout("Y") == 20
        assert checkout_solution.checkout("Z") == 21
        assert checkout_solution.checkout("S") == 20
        assert checkout_solution.checkout("XXXS") == 62

