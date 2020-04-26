import os
import unittest

import buildEden

repo_path = os.path.join(os.getcwd(), "repo")
out_path = os.path.join(os.getcwd(), "out")
workshop_path = os.path.join(os.getcwd(), "out_steam")
workshop_mod_path = os.path.join(os.getcwd(), "out_steam", "2046492427")

input_png1 = os.path.join(repo_path, "test.png")
input_png2 = os.path.join(repo_path, "artifacts", "test2.png")
input_aseprite = os.path.join(repo_path, "test.aseprite")
expected_png1 = os.path.join(out_path, "test.png")
expected_png2 = os.path.join(out_path, "test2.png")
expected_aseprite = os.path.join(out_path, "test.aseprite")
expected_artifact = "artifact"
expected_spell1 = "spell1"
expected_spell2 = "spell2"

expected_artifact_xml = os.path.join(out_path, "Artifacts.xml")
expected_spells_xml = os.path.join(out_path, "Spells.xml")
expected_workshop_xml = os.path.join(out_path, "WorkshopItemInfo.xml")


class MyTestCase(unittest.TestCase):

    def test_fill_with_content(self):
        result_dict = {}

        buildEden.fill_with_content(result_dict, repo_path, ["Artifacts.xml"])

        self.assertEqual(5, len(result_dict))
        self.assertEqual(0, len(result_dict["Artifacts.lua"]))
        self.workshop_asserts(result_dict["WorkshopItemInfo.xml"])
        self.art_asserts(result_dict)
        self.artifact_asserts(result_dict)
        self.spell_asserts(result_dict)

    def workshop_asserts(self, result_workshop):
        self.assertTrue(8, len(result_workshop))
        self.assertTrue(r"<PublishedFileId>2046492427</PublishedFileId>" in result_workshop)
        self.assertTrue(r"<Name>MyMod</Name>" in result_workshop)
        self.assertTrue(r"<Description>testing modding</Description>" in result_workshop)
        self.assertTrue(r"<IconFileName>workshopIcon.png</IconFileName>" in result_workshop)
        self.assertTrue(r"<Tags/>" in result_workshop)
        self.assertTrue(r"<Priority>0</Priority>" in result_workshop)
        self.assertTrue(r"<ModVersion>0</ModVersion>" in result_workshop)
        self.assertTrue(r"<GameVersion>1.1</GameVersion>" in result_workshop)

    def artifact_asserts(self, result_dict):
        result_artifact_content = result_dict["Artifacts.xml"]
        self.assertEqual(1, len(result_artifact_content))
        self.assertTrue(expected_artifact in result_artifact_content)

    def spell_asserts(self, result_dict):
        result_spell_content = result_dict["Spells.xml"]
        self.assertEqual(2, len(result_spell_content))
        self.assertTrue(expected_spell1 in result_spell_content)
        self.assertTrue(expected_spell2 in result_spell_content)

    def art_asserts(self, result_dict):
        expected_png1 = os.path.join(repo_path, "test.png")
        expected_png2 = os.path.join(repo_path, "artifacts", "test2.png")
        expected_aseprite = os.path.join(repo_path, "test.aseprite")
        result_art = result_dict["art"]

        self.assertTrue(expected_png1 in result_art)
        self.assertTrue(expected_png2 in result_art)
        self.assertTrue(expected_aseprite in result_art)
        self.assertTrue(3 == len(result_art))

    def test_process_art(self):
        art_files = [input_png2, input_png1, input_aseprite]

        buildEden.process_art(art_files, out_path)

        self.assertTrue(os.path.exists(expected_aseprite))
        self.assertTrue(os.path.exists(expected_png1))
        self.assertTrue(os.path.exists(expected_png2))
        os.remove(expected_png1)
        os.remove(expected_png2)
        os.remove(expected_aseprite)

    def test_build_to_workshop(self):
        expected_png1 = os.path.join(workshop_mod_path, "test.png")
        expected_png2 = os.path.join(workshop_mod_path, "test2.png")
        expected_aseprite = os.path.join(workshop_mod_path, "test.aseprite")

        expected_artifact_xml = os.path.join(workshop_mod_path, "Artifacts.xml")
        expected_spells_xml = os.path.join(workshop_mod_path, "Spells.xml")
        expected_workshop_xml = os.path.join(workshop_mod_path, "WorkshopItemInfo.xml")

        buildEden.build_workshop(workshop_path)

        self.assertTrue(os.path.exists(expected_aseprite))
        self.assertTrue(os.path.exists(expected_png1))
        self.assertTrue(os.path.exists(expected_png2))
        os.remove(expected_png1)
        os.remove(expected_png2)
        os.remove(expected_aseprite)

        self.assertTrue(os.path.exists(expected_artifact_xml))
        self.assertTrue(os.path.exists(expected_spells_xml))
        self.assertTrue(os.path.exists(expected_workshop_xml))
        os.remove(expected_artifact_xml)
        os.remove(expected_spells_xml)
        os.remove(expected_workshop_xml)

    def test_build_to_local(self):
        expected_png1 = os.path.join(out_path, "test.png")
        expected_png2 = os.path.join(out_path, "test2.png")
        expected_aseprite = os.path.join(out_path, "test.aseprite")

        expected_artifact_xml = os.path.join(out_path, "Artifacts.xml")
        expected_spells_xml = os.path.join(out_path, "Spells.xml")
        expected_workshop_xml = os.path.join(out_path, "WorkshopItemInfo.xml")

        buildEden.build_local(out_path)

        self.assertTrue(os.path.exists(expected_aseprite))
        self.assertTrue(os.path.exists(expected_png1))
        self.assertTrue(os.path.exists(expected_png2))
        os.remove(expected_png1)
        os.remove(expected_png2)
        os.remove(expected_aseprite)

        self.assertTrue(os.path.exists(expected_artifact_xml))
        self.assertTrue(os.path.exists(expected_spells_xml))
        self.assertTrue(os.path.exists(expected_workshop_xml))
        os.remove(expected_artifact_xml)
        os.remove(expected_spells_xml)
        os.remove(expected_workshop_xml)

    def test_workshop(self):
        workshop_info = [r"<PublishedFileId>2046492427</PublishedFileId>"]
        expected_path = os.path.join(out_path, "2046492427")

        result = buildEden.workshop(workshop_info, out_path)

        self.assertEqual(expected_path, result)

    def test_workshop(self):
        workshop_info = [r""]
        failed = False
        try:
            buildEden.workshop(workshop_info, out_path)
        except Exception as e:
            failed = True
            print(e)
        self.assertTrue(failed)

if __name__ == '__main__':
    unittest.main()
