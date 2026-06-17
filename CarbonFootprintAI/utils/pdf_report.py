from fpdf import FPDF


def create_pdf(score):

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=16)
    pdf.cell(200, 10, txt="Carbon Footprint Report", ln=True)

    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Carbon Score: {score}", ln=True)

    pdf.output("carbon_report.pdf")