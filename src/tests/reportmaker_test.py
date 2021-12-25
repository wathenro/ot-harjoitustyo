import unittest
import os
from PIL import Image
from loaders.report_maker import ReportMaker

class TestLocLoader(unittest.TestCase):
    def setUp(self):
        self.report=ReportMaker()
        img = Image.new("RGB", (512, 512))
        img.save("temp_track_pic.jpg")

    def test_make_pdf_report(self):
        image_removed=True
        report_created=False
        self.report.make_pdf_report("Test-Track-Report",1007007,1007)
        if os.path.exists("temp_track_pic.jpg"):
            image_removed=False
        if os.path.exists("data/reports/RD_Test-Track-Report.pdf") or\
            os.path.exists("src/data/reports/RD_Test-Track-Report.pdf"):
            report_created=True
            try:
                os.remove("data/reports/RD_Test-Track-Report.pdf")
            except:
                os.remove("src/data/reports/RD_Test-Track-Report.pdf")
        
        self.assertEqual(image_removed,True)
        self.assertEqual(report_created,True)
    