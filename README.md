# Algorithm for file updates in Python

Esto es parte de una actividad llevaba a cabo en el curso de [_Google Cybersecurity Professional Certificate_](https://www.coursera.org/professional-certificates/google-cybersecurity) y mas concretamente en el módulo de [_Automate Cybersecurity Tasks with Python_](https://www.coursera.org/learn/automate-cybersecurity-tasks-with-python?specialization=google-cybersecurity).

## Scenario

Review the following scenario. Then complete the step-by-step instructions.

You are a security professional working at a health care company. As part of your job, you're required to regularly update a file that identifies the employees who can access restricted content. The contents of the file are based on who is working with personal patient records. Employees are restricted access based on their IP address. There is an allow list for IP addresses permitted to sign into the restricted subnetwork. There's also a remove list that identifies which employees you must remove from this allow list.

Your task is to create an algorithm that uses Python code to check whether the allow list contains any IP addresses identified on the remove list. If so, you should remove those IP addresses from the file containing the allow list.

## Supporting material

- allow_list.txt, una lista de IP inventadas para el proposito de este ejercicio.
- default_allow_list.txt is a copy of allow_list.txt made as backup in case script doesnt work as expected or the user want to try it again.

If you want to reset allow_list, just call the script `reset.sh`

## Summary

In summary, the script ` main.py` is designed to update the `allow_list.txt`file by removing any IP addresses that are found in the`remove_list`. It does this by reading the file, modifying the list of allowed IP addresses, and then writing the updated list back to the file.

This script performs the following tasks:

1. It imports the `os` module and uses the `os.system` function to execute a shell script named `reset.sh`. This shell script resets the contents of the `allow_list.txt` file.
2. It assigns the filename "allow_list.txt" to the variable `import_file`, which is the file containing the list of allowed IP addresses.
3. It defines a `remove_list` containing IP addresses that are no longer allowed.
4. It opens the `import_file` ("allow_list.txt") in read mode and reads its contents into the `allow_list_file` variable.
5. It splits the `allow_list_file` into a list called `allow_list` using the newline character "\n" as the separator. This list contains the original list of allowed IP addresses.
6. It then iterates through each IP address in the `remove_list`. For each IP address in the `remove_list`, it checks if that IP address is present in the `allow_list`. If it is, it removes the IP address from the `allow_list`.
7. The script converts the modified `allow_list` back into a single string called `parse_allow_list` by joining the IP addresses with newline characters.
8. It opens the `import_file` again, this time in write mode ("w"), which truncates the file and opens it for writing.
9. It writes the `parse_allow_list` string (containing the updated list of allowed IP addresses) back to the `allow_list.txt` file, effectively overwriting the old contents.
