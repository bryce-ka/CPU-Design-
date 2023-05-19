"""
This program reads assembly code for a circut in logisim 

authors: Bryce Anthony Edward Shores 
"""

#dictionary of different functions
command_dict = {
  "input" : "04",
  "output" : "07",
  "jmp" : "0a",
  "load" : "0e",
  "inc" : "14",
  "mov" : "17",
  "add" : "1a",
  "halt" : "1d",
  "nop" : "1e",
}

def main():
  """
  """
  output_array = ["v2.0 raw\n"]
 
  command_file = input("Please enter the name of an input file: " )
  #fnf_error = print("Syntax Error")


  try:
    with open(command_file, "r") as in_file:
    
      command = in_file.read()
      command = command.lower()
      
  except(FileNotFoundError):
    raise Exception("File not found")


  command_list = command.split()
  print(command_list)

  for i in range(len(command_list)):

    if command_list[i] in command_dict:
      output_array.append(command_dict[command_list[i]])
      output_array.append("\n")

    if command_list[i-1] == "jmp" or command_list[i-1] == "load":
      if len(command_list[i]) > 2:
        print("Syntax error"+ str(i))
        exit()
      else:
        output_array.append(command_list[i])
        output_array.append("\n")

    #else:
      #raise Exception("Syntax Error")

  output_file = input("Please name the output file : " )

  out = open(output_file , "w")
  lines_of_file = output_array
  out.writelines(lines_of_file)
  out.close()


if __name__ == '__main__':
  main()