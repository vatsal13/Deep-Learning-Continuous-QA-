

import subprocess
import os
import sys
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-imf", "--image_folder", help="Folder containing the images")
parser.add_argument("-beam", "--beam_size", help="Beam search size for sampling questions from RNN/LSTM")
args = parser.parse_args()

image_folder = "../images/" if args.image_folder is None else args.image_folder
beam_size = 10 if args.beam_size is None else args.beam_size

print image_folder
print beam_size

os.system("cd questions ; rm questions.txt")
os.system("cd images ; rm images.txt")
os.system("cd neuraltalk2 ; th eval.lua -model ../model/model_id.t7 -image_folder " + image_folder +" -sample_max 1 -beam_size "+ str(beam_size))

filenames = []
app_path = image_folder
with open("./images/images.txt","r") as read:
    line = read.readlines()
    filenames = line
    filenames = [x.split("\n")[0].split("/")[-1] for x in filenames]
    #print filenames


with open("./questions/questions.txt", 'r') as f:
    questions = f.readlines()
    questions = [x.split('/n')[0] for x in questions]


quest_file = {}
for i in range(0,len(filenames)):
    quest_file[filenames[i]] = questions[i*5: i*5+5]


for key in quest_file:
    file_name_str = "../answers/"+key.split(".jpg")[0]+".txt"
    if True: # not os.path.isfile("./"+file_name_str):
       # with open(file_name_str, 'w') as outfile:
        for i in range(0,5):
            #print "i : ", i
            #os.system("cd ./VQA_Demo;")
            arg2 = key
            arg4 = quest_file[key][i]
            #print arg2, " ", arg4
            os.system("pwd ;")
            #proc = subprocess.Popen(['python', './VQA_Demo/demo.py',  '-image_file_name ./images/snow_man -question "here is man"'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            #print proc.communicate()[0]
            #thread.spleep(100)
            #print "answer"
            os.system('cd VQA_Demo ; python demo.py -image_file_name '+app_path + arg2+' -question "'+arg4+'" >> '+file_name_str)
            #print 'cd VQA_Demo ; python demo.py -image_file_name '+app_path + arg2+' -question "'+arg4+'" >> '+file_name_str
            #sys.stdout = open(outfile, 'w')
            #outfile.write(ret)

