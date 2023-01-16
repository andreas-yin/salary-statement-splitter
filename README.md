# Salary Statement Splitter
This custom application was developed to automate two HR tasks related to the payroll of a German company.

## The problem 
### Split into one-page pdf files (January - November)
Every month, the HR department gets a multipage pdf file that contains the salary statements of all their employees. Previously, they had to manually extract each person's salary statement (one page), save it as a single pdf file and give it a filename that includes the person's name. The task took about 90 minutes to complete. 

### Split  into two-page pdf files (December)
End of December, they get a special multipage pdf file that not only contains all their employees' salary statements (first half of pdf), but also their certificates of wage tax deduction (second half of pdf). On top of the usual monthly task, HR also had to manually extract each employee's certificate of wage tax deduction from the multipage pdf and add it to that person's salary statement. So the single pdf files consisted of two pages: The salary statement was on page 1, the certificate of wage tax deduction was on page 2. The whole task took about 110 minutes to complete.

## The solution
Thanks to this application, these tasks have now been automated and take seconds only.

## Prerequisites
1. [Python](https://www.python.org/downloads/) version ≥ 3.10.8
2. [pip](https://pypi.org/project/pip/) version ≥ 22.3.1
3. Install a package called [PyPDF2](https://pypi.org/project/PyPDF2/) by running the following command on the command line:
```
pip install pypdf2
```
4. Ensure that the name of the input pdf file matches the name specified in [app.py](/app.py):
```
inputpdf = PdfFileReader(open("Payroll_2022_08_statements", "rb"))
```
5. Ensure that the name of the folder to be generated indicates the correct year/month:
```
subdir = "2022-08_Single_salary_statements" 
os.mkdir(os.path.join(here, "2022-08_Single_salary_statements"))
````
6. Ensure that the naming schema for the output pdf files indicates the correct year/month:
````
with open(os.path.join(here, subdir, "Salary statement 2022_08-%s.pdf" % name), "wb") as outputStream:``
````

## Run the application
Run the following command on the command line:
```
python app.py
```
If you have installed Python 3 under 'python3', please run the following command instead:
```
python3 app.py
```