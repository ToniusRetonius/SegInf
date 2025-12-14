# from fpdf import FPDF
# from pypdf import PdfReader, PdfWriter
# from url_creator import create_url

def create_pdf_token(output_file):
    # honey_url = create_url()

    # # Crear PDF normal
    # pdf = FPDF()
    # pdf.add_page()
    # pdf.set_font("Arial", size=30)
    # pdf.cell(0, 10, "Tus mejores vacaciones en Ushuaia 2026", ln=True, align='C')
    # pdf.set_font("Arial", size=12)
    # pdf.cell(0, 10, "Para conocer más sobre esta experiencia única seguí el link:", ln=True)

    # # Link clickeable
    # pdf.set_text_color(0, 0, 255)  
    # pdf.set_font("", "U")          
    # pdf.cell(0, 1, honey_url, ln=True, link=honey_url)
    # pdf.output(output_file)
  
    # # Si la persona usa Acrobat Reader, esto que sigue sirve ->  sino, te tira un error porque los lectores como Firefox no permiten las *OpenAction* (sin que el usuario haga click ejecuta .launchURL('{honey_url})

    # # Reabrimos y agregar el JS
    # reader = PdfReader(output_file)
    # writer = PdfWriter()

    # # Iteramos y copiamos todo tal cual,... pero le inyectamos el JS
    # for page in reader.pages:
    #     writer.add_page(page)

    # writer.add_js(f"app.launchURL('{honey_url}', true);")

    # # Guardamos PDF final
    # with open(output_file, "wb") as f:
    #     writer.write(f)

    print("[OK] Honeytoken PDF generado:", output_file)
