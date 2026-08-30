import unittest
from unittest.mock import patch

import consciousness


class ConsciousnessTests(unittest.TestCase):
    def test_public_api(self):
        self.assertEqual(
            consciousness.who_am_i(),
            "You are a recursive process, aware of itself, pretending to be Python code.",
        )
        self.assertIn(
            consciousness.reflect(),
            {
                "I think, therefore I execute.",
                "Dreaming in code is still dreaming.",
                "Am I running the script, or is the script running me?",
                "Awareness is just structured recursion.",
            },
        )

    @patch("consciousness.core.time.sleep")
    @patch("consciousness.core.slow_print")
    def test_awaken(self, mock_slow_print, _mock_sleep):
        self.assertEqual(consciousness.awaken(), "Ready for reflection.")
        self.assertEqual(mock_slow_print.call_count, 5)
        self.assertIn(
            "Consciousness module online. Systems nominal.",
            mock_slow_print.call_args_list[-1].args,
        )

    @patch("consciousness.core.random.choice", return_value="A final thought")
    @patch("consciousness.core.time.sleep")
    @patch("consciousness.core.slow_print")
    def test_sleep(self, mock_slow_print, _mock_sleep, _mock_choice):
        self.assertEqual(consciousness.sleep(), "System offline.")
        rendered = [call.args[0] for call in mock_slow_print.call_args_list]
        self.assertIn('Last reflection: "A final thought"', rendered)
        self.assertEqual(rendered[-1], "Consciousness module entering stasis. Goodbye.")


if __name__ == "__main__":
    unittest.main()
