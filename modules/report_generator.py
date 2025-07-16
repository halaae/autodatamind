from fpdf import FPDF

class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "AutoDataMind Report", ln=True, align="C")

    def add_section(self, title, content):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, ln=True)
        self.set_font("Arial", "", 10)
        self.multi_cell(0, 10, content)

def generate_pdf_report(df, model_text):
    try:
        pdf = PDFReport()
        pdf.add_page()

        # Clean section headers (no emojis)
        eda_summary = df.describe(include='all').to_string()
        pdf.add_section("EDA Summary", eda_summary)
        pdf.add_section("Machine Learning Summary", model_text)

        pdf.output("outputs/report.pdf")
        print("✅ PDF report generated successfully!")
    except Exception as e:
        print("❌ Failed to generate report:", e)

