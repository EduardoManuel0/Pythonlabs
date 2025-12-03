import csv
from openpyxl import Workbook

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Converts CSV to XLSX.
    Use openpyxl or xlsxwriter.
    The first row of the CSV is the header.
    The sheet is called "Sheet1."
    Columns are auto-widthed to fit the text length (at least 8 characters).
    """
    try:
        # Crie um novo workbook e pegue a planilha ativa
        wb = Workbook()
        ws = wb.active
        ws.title = "Sheet1"

        # Abra o arquivo CSV e leia o conteúdo
        with open(csv_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                # Adicione cada linha do CSV à planilha
                ws.append(row)

        # Salve o workbook como um arquivo XLSX
        wb.save(xlsx_path)
        print(f"Successfully converted '{csv_path}' to '{xlsx_path}' using openpyxl.")

    except FileNotFoundError:
        print(f"Error: CSV File '{csv_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")
if __name__=="__name__":
        csv_to_xlsx("data/samples/cities.csv", "data/out/cities.xlsx")