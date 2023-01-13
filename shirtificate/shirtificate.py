from fpdf import FPDF

# name=input("Name: ")
# pdf=FPDF(orientation="P" , unit="mm" , format="A4")
class PDF():
    def __init__(self, name):
        

    def save(self , name):
        self._pdf.output(name)

name=input("Name: ")
pdf=PDF(name)
pdf.save("shirtificate.pdf")