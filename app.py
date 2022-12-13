from PyPDF2 import PdfFileWriter, PdfFileReader
import os

# Create a folder that holds the generated single pdf files
here = os.path.dirname(os.path.realpath(__file__))
subdir = "2022-08_Single_salary_statements" 
os.mkdir(os.path.join(here, "2022-08_Single_salary_statements"))
save_path = ""
inputpdf = PdfFileReader(open("Payroll_2022_08_statements", "rb"))

for i in range(inputpdf.numPages):
    output = PdfFileWriter()
    single_page = inputpdf.getPage(i)
    output.addPage(single_page)
    text= single_page.extract_text()

    #Split out the last paragraph, which has the name of the person
    last_paragraph = text.split("XXXXX City\n", 1)[1]

    line_of_name = last_paragraph.split("\n")[0]
    last_name = line_of_name.split()[-1]
    first_name = line_of_name.split()[0]
    first_name_initial = list(first_name)[0]
    combined_name = first_name_initial + last_name
    name = combined_name.lower()

    # Give each single statement a filename that contains the name of the person
    with open(os.path.join(here, subdir, "Salary statement 2022_08-%s.pdf" % name), "wb") as outputStream:
        output.write(outputStream)
