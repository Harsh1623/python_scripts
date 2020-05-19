import os
file_paths = []
#list of all text files inside a folder

input_path = input("enter folder path to copy from all text files inside it : \n")
output_path = input("enter a folder path to create txt file in it : \n")

for r,d,f in os.walk(input_path):
    for file in f:
        if ".txt" in file:
            file_paths.append(os.path.join(r,file))
for f_p in file_paths :
    with open(f_p, "r",encoding='utf8') as in_file:
        data = in_file.read()
        write_file = open(output_path+"\\write_file.txt","a")
        #file will be created with name "write_file.txt"
        write_file.write(data +"\n")
        write_file.close()
    in_file.close()
    
