import csv
import shutil
source_dir = "/home/ubuntu/git/PrepasGP/internal/cert"
destination_dir = "/home/ubuntu/zips/UAGM"
def generate_zip(input_csv_path, certifactes_path, output_dir_path):
    with open(input_csv_path) as csvfile:
        csvreader =csv.reader(csvfile)
        for row in csvreader:
            print(row[0])
            fname = certifactes_path + "/GP-"+row[0]+".pdf"
            print(fname)
            shutil.copy(fname, output_dir_path)
            print("copied")

if __name__== "__main__":
    generate_zip("UAGM.csv", source_dir, destination_dir)