import PyPDF2 
import os

merger = PyPDF2.PdfMerger()

archive_list = os.listdir("archive")
archive_list.sort
print(archive_list)

for archive in archive_list:
    if ".pdf" in archive:
        merger.append(f"archive/{archive}")
merger.write("PDF Final PDF")







