from fpdf import FPDF

# name=input("Name: ")
# pdf=FPDF(orientation="P" , unit="mm" , format="A4")
class PDF():
    def __init__(self, name):
        self._pdf=FPDF()
        self._pdf.add_page()
        self._pdf.set_font("helvetica", "B", 16)
        self._pdf.cell()

    def save(self , name):
        self._pdf.output(name)

name=input("Name: ")
pdf=PDF(name)
pdf.save("shirtificate.pdf")