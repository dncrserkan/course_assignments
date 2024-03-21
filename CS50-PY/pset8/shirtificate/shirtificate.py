from fpdf import FPDF


text = input("Name: ").strip() + " took CS50"

pdf = FPDF(orientation="portrait", format="A4")
pdf.add_page()

pdf.set_font('helvetica', style="B", size=40)
pdf.cell(w=0, h=60, text="CS50 Shirtificate", align='C', center=True)
pdf.ln()

pdf.image("shirtificate.png", 0, 75, w=210)

pdf.set_font('helvetica', style="B", size=28)
pdf.set_text_color(255)
pdf.ln()
pdf.multi_cell(w=110, text=text, align="C", center=True)

pdf.output("shirtificate.pdf")
