from PyPDF2 import PdfFileWriter, PdfFileReader
import os

#Create folder that will hold the single pdf files
here = os.path.dirname(os.path.realpath(__file__))
subdir = "2022-12_Single_salary_statements_incl_wage_tax_deduction"
os.mkdir(os.path.join(here, subdir))

inputpdf = PdfFileReader(open("Payroll_2022_12_statements", "rb"))

#Create dictionary with employee name as key and array of page numbers as value
dict = {}

for i in range(inputpdf.numPages):    
    page = inputpdf.getPage(i)
    pageContent = page.extract_text()

    #Get employee name for filename
    last_paragraph = pageContent.split("XXXXX City\n", 1)[1]
    line_of_name = last_paragraph.split("\n")[0]
    last_name = line_of_name.split()[-1]
    first_name = line_of_name.split()[0]
    first_name_initial = list(first_name)[0]
    combined_name = first_name_initial + last_name
    name = combined_name.lower()

    if name not in dict:
        dict[name] = [i]
    else:
        dict[name].append(i)


#Generate split pdf files
for name, pages in dict.items():
    output = PdfFileWriter()
    with open(os.path.join(here, subdir, "Salary statement 2022_12-%s.pdf" % name), "wb") as outputStream:
        for page in pages:
            output.addPage(inputpdf.getPage(page))
        output.write(outputStream)
        outputStream.close()
      