class TestExample:
    def test_check_math(self):
        a = 5
        b = 9
        expected_sum = 14
        assert a+b == expected_sum, f"Ожидаемая сумма не равна {expected_sum}"

    def test_check_math2(self):
        a = 5
        b = 9
        expected_sum = 11
        assert a+b == expected_sum, f"Ожидаемая сумма не равна {expected_sum}"