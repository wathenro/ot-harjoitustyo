import os
from fpdf import FPDF

class ReportMaker():
    """PDF report making class

    Attributes:
        None
    """

    def __init__(self) -> None:
        pass

    def make_pdf_report(self,track,population,length):
        """Creates a pdf report to data/reports of the optimized track

        Args:
            track: The route of optimized track as a string
            population: Population along the track
            length: Length of the optimized track

        Returns:
            Nothing
        """
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size = 20)
        pdf.cell(w=0,h = 25, txt = 'Railroad Designer', ln = 1,align = 'C')
        pdf.set_font("Arial", size = 12)
        pdf.cell(w=0,h = 18, txt = "Track: "+track, ln = 1,align = 'L')
        pdf.cell(w=0,h = 18, txt = "Length: "\
            +str(length)+"km", border = 0, ln = 1,align = 'L')
        pdf.cell(w=0,h = 18, txt = "Population: "\
            +str(population), border = 0, ln = 1,align = 'L')
        pdf.image("temp_track_pic.jpg")
        if os.path.exists("temp_track_pic.jpg"):
            os.remove("temp_track_pic.jpg")
        try:
            pdf.output("data/reports/RD_"+track+".pdf").encode('latin-1')
        except FileNotFoundError:
            pdf.output("src/data/reports/RD_"+track+".pdf").encode('latin-1')
