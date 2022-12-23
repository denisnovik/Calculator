import unittest


from Calculator import encode, sin_value, sin_mask, sin, cos_value, cos_mask, cos, plusminus, e_value, e_mask, exponenta, log_value, log_mask, logarifm, sqrt_value, sqrt_mask, koren, calc

class Calculator_tests(unittest.TestCase):

    def test_calculator_encode(self):
        self.assertEqual(encode("жжжж"), "ж")

    def test_calculator_sin_value(self):
        self.assertEqual(sin_value("sin(1)+1", 0), "0.8414709848078965")

    def test_calculator_sin_mask(self):
        self.assertEqual(sin_mask("sin(1)+1", 0, "0.8414709848078965"), "0.8414709848078965+1")

    def test_calculator_sin(self):
        self.assertEqual(sin("sin(1)+1"), "0.8414709848078965+1")

    def test_calculator_cos_value(self):
        self.assertEqual(cos_value("cos(1)+1", 0), "0.5403023058681398")

    def test_calculator_cos_mask(self):
        self.assertEqual(cos_mask("cos(1)+1", 0, "0.5403023058681398"), "0.5403023058681398+1")

    def test_calculator_cos(self):
        self.assertEqual(cos("cos(1)+1"), "0.5403023058681398+1")

    def test_calculator_plusminus(self):
        self.assertEqual(plusminus("--1+2"), "+1+2")

    def test_calculator_e_value(self):
        self.assertEqual(e_value("e^2+1", 0), "7.38905609893065")

    def test_calculator_e_mask(self):
        self.assertEqual(e_mask("e^2+1", 0, "7.38905609893065"), "7.38905609893065+1")

    def test_calculator_exponenta(self):
        self.assertEqual(exponenta("e^2+1"), "7.38905609893065+1")

    def test_calculator_log_value(self):
        self.assertEqual(log_value("log2(8)+1", 0), "3.0")

    def test_calculator_log_mask(self):
        self.assertEqual(log_mask("log2(8)+1", 0, "3.0"), "3.0+1")

    def test_calculator_logarifm(self):
        self.assertEqual(logarifm("log2(8)+1"), "3.0+1")

    def test_calculator_sqrt_value(self):
        self.assertEqual(sqrt_value("sqrt(4)+1", 0), "2.0")

    def test_calculator_sqrt_mask(self):
        self.assertEqual(sqrt_mask("sqrt(4)+1", 0, "2.0"), "2.0+1")

    def test_calculator_koren(self):
        self.assertEqual(koren("sqrt(4)+1"), "2.0+1")
        
    def test_calculator_minus_calc(self):
        self.assertRaises(TypeError, calc, "", "")

    def test_calculator_minus_encode(self):
        self.assertRaises(TypeError, encode, "жжжж", "бб")

    def test_calculator_minus_sin_value(self):
        self.assertRaises(TypeError, sin_value, "sin(1)+1", "0.8414709848078965+1")

    def test_calculator_minus_cos_value(self):
        self.assertRaises(TypeError, cos_value, "cos(1)+1", "0.5403023058681398+1")

    def test_calculator_minus_exponenta(self):
        self.assertRaises(TypeError, exponenta, "e^2+1", "322")

    def test_calculator_minus_logarifm(self):
        self.assertRaises(TypeError, logarifm, "log2(8)+1", "2345")

if __name__ == "__main__":
    unittest.main()
