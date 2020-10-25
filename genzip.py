import csv
import shutil
source_dir = "/home/ubuntu/git/PrepasGP/internal/cert"
destination_dir = "/home/ubuntu/zips/UPR"
def generate_zip(input_csv_path, certifactes_path, output_dir_path):
    with open(input_csv_path) as csvfile:

        csvreader =csv.reader(csvfile)
        i = 0
        text_file = open("Error.txt", "w")
        dict = {}
        for row in csvreader:
            print(row[0])
            flag = dict.get(row[0], None)
            if not flag:
                print(f"GP Not found: {outname}", file=text_file)
                text_file.flush()
            else:
                dict[row[0]] = "Present"
            fname = certifactes_path + "/GP-"+row[0]+".pdf"
            outname = output_dir_path+ "/GP-"+row[0]+".pdf"
            print(fname)
            print(outname)
            try:
                shutil.copyfile(fname, outname)
            except:
                print(f"GP Not found: {outname}", file=text_file)
                text_file.flush()
            print("copied")
        text_file.flush()
        text_file.close()

if __name__== "__main__":
    generate_zip("UPR.csv", source_dir, destination_dir)