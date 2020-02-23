import sys
import argparse
from .convertfile import convert_yaml_to_json
from .palindrome import is_palindrome
from .django_gen import create_project

def main():

    flags = argparse.ArgumentParser(description='This is our Django project generator tool set.',add_help=False)

    # aruments for help
    flags.add_argument('-h','--help',
    help='Thank you for asking for help. These tools are used to generate a Django project and convert CloudFormation code from YAML to JSON.',
    action='help', dest='help_command')

    flags.add_argument('-na','--name',
    help='The project name',
    dest='project_name', type=str, required=False)

    flags.add_argument('-pa','--path',
    help='Project name must be a palindrome string ex: `tacocat`',
    dest='project_path', type=str, required=False)

    flags.add_argument('-cn','--checkname',
    help='Check if the project name is a palindrome, returns True or False',
    dest='check_name', type=str, required=False)

    flags.add_argument('-inf', '--inputfile',
    help='Converts YAML file formate to a JSON file formate called tacocat_cf.json',
    dest='input_file', type=str, required=False)

    args = flags.parse_args()

    #calls convert_yaml_to_json function with args yaml file
    if(args.input_file):
        convert_yaml_to_json(args.input_file)
    #Creates project skeleton
    elif(args.project_path):
        if (is_palindrome(args.project_name)):
            create_project(args.project_name, path=args.project_path)
        else:
            print('Please provide project name with respect to palindrome')
    # checks if palindrome is True or False
    elif(args.check_name):
        if (is_palindrome(args.check_name)):
            print('True')
        else:
            print('False')

if __name__ == '__main__':
    main()
