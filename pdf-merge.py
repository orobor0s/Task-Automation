from PyPDF2 import PdfFileMerger

# make sure to put r before each path to ensure they are read correctly
pdfs = [r"C:\Users\br00\Downloads\The_Mindful_Twenty-Something_Life_Skills_to_Handle..._----_(Introduction).pdf",
        r"C:\Users\br00\Downloads\The_Mindful_Twenty-Something_Life_Skills_to_Handle..._----_(Part_1_Getting_Ready).pdf"]

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("") # name of new file
merger.close()

print('complete')
