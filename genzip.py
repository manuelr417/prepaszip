import csv
import shutil
source_dir = "/home/ubuntu/git/PrepasGP/internal/cert"
destination_dir = "/home/ubuntu/zips/UPR"
def generate_zip(input_csv_path, certifactes_path, output_dir_path):
    with open(input_csv_path) as csvfile:
        csvreader =csv.reader(csvfile)
        i = 0
        for row in csvreader:
            print(row[0])
            fname = certifactes_path + "/GP-"+row[0]+".pdf"
            outname = output_dir_path+ "/GP-"+row[0]+".pdf"
            print(fname)
            print(outname)
            shutil.copyfile(fname, outname)
            print("copied")

if __name__== "__main__":
    generate_zip("UPR.csv", source_dir, destination_dir)