import os  # to get the present working directory, create new directories, etc.
import datetime  # so we can add the date/time to the file; therefore, we don't overwrite existing files

# Get the name of the running python script so when we save the
# output we can easily identify what the output is from at a later date
this_script = os.path.basename(__file__)

pwd = os.getcwd()  # store the present working directory

output_dir_path = pwd + os.sep + this_script + "_output_files"  # make a path for where to store files

# check if the directory where the output files should go is an existing directory
# make the directory if it doesn't exist
if not os.path.isdir(output_dir_path):
    os.mkdir(output_dir_path)


# get date/time and combined with script name to make a file name for the output file
date_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")


# combined the output directory/date/time/script name to make a full file path for the output file
output_file = output_dir_path + os.sep + this_script + "_" + date_time +".txt"


def printandwrite(passed_string, passed_output_file):
    print(passed_string)
    with open(passed_output_file, 'a+') as file_to_write_to:
        file_to_write_to.write(passed_string + "\n")


# test the function
printandwrite("test_string", output_file)
