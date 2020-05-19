import os
file_paths = []
for r,d,f in os.walk(r"E:\ASP_New\EncryptYaraRulesFileApp\Debug\encrypted_rules"):
    for file in f:
        if ".yar" in file:
            file_paths.append(os.path.join(r,file))

for f_p in file_paths :
    with open(f_p, "r") as in_file:
        data = in_file.read()
        write_file = open(r"E:\ASP_New\EncryptYaraRulesFileApp\all_rules.yar","a")
        write_file.write(data +"\n")
        write_file.close()
    in_file.close()
