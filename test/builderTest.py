import os
import unittest

import buildEden


class MyTestCase(unittest.TestCase):

    def test_fill_with_content(self):
        result_dict = {}
        buildEden.fill_with_content(result_dict, os.getcwd(), ["Artifacts.xml"])

        self.art_asserts(result_dict)
        self.artifact_asserts(result_dict)
        self.spell_asserts(result_dict)

    def artifact_asserts(self, result_dict):
        result_artifact_content = result_dict["Artifacts.xml"]
        self.assertEqual(2, len(result_artifact_content))
        self.assertTrue("\nartifact" in result_artifact_content)
        self.assertTrue("" in result_artifact_content)

    def spell_asserts(self, result_dict):
        result_spell_content = result_dict["Spells.xml"]
        self.assertEqual(3, len(result_spell_content))
        self.assertTrue("\nspell1" in result_spell_content)
        self.assertTrue("\nspell2" in result_spell_content)
        self.assertTrue("" in result_spell_content)

    def art_asserts(self, result_dict):
        expected_png1 = os.path.join(os.getcwd(), "test.png")
        expected_png2 = os.path.join(os.getcwd(), "artifacts", "test.png")

        expected_aseprite = os.path.join(os.getcwd(), "test.aseprite")
        result_art = result_dict["art"]

        self.assertTrue(expected_png1 in result_art)
        self.assertTrue(expected_png2 in result_art)
        self.assertTrue(expected_aseprite in result_art)
        self.assertTrue(3 == len(result_art))


if __name__ == '__main__':
    unittest.main()
