from fpdf import FPDF

# name=input("Name: ")
# pdf=FPDF(orientation="P" , unit="mm" , format="A4")
class PDF(FPDF):
    def header(self):
        self.image("../shirtificate.png" , )
