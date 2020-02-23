# Python Exercise

Modus Create's Python coding exercise.

- [Modus Create](#modus-create)
- [Licensing](#licensing)

# Introduction

You've just been assigned to a new Engineering Team at Acme Corp. This team is responsible for
Python development. The Project manager (PM) has a number of tasks he would like you to complete
in Python and Django.

The first thing you will need to do, in order to help the PM is get your development environment setup.

# Getting Started

The I.T department brings you over your new machine. You will need to:

1. Setup a Python 3 based environment using a virtual env. All the code must be developed in Python 3.
2. Ensure you have pip installed for Python 3.
3. Unzip the contents of this archive.
4. Note that it's a git repository. Use it accordingly :)

Your Team Lead stops by to introduce herself. She also reminds you that you should edit the `.gitignore` file and add the exclusions for the types of files, you typically find in a python and Django project but don't want to commit. This is to avoid those files ending up in GitHub.

Once you have completed these steps, you will be ready to start the project and meet with the PM for your task list.

# Background - Meeting with the PM

The PM tells you we want to build a proof of concept application that consists of a command line tool
for generating some of the files needed by a new project and also the skeleton files for a Django website.

One of the junior engineers on the team started the project but didn't get very far!  The DevOps team members also don't have time to work on this either, so it looks like it is down to you.

Eventually the team would like to host this in AWS, although worrying about deploying it to the Cloud is a problem for another day. However, there is a feature the DevOps team would like you to add to the tool for converting YAML to JSON.

The PM having gathered the various requirements and current state of the application lets you know that the command line tools will take care of important tasks such as:

1. Checking if the project name is a palindrome (a requirement of the departments project naming convention)
2. Providing help to the user
3. Converting YAML into JSON, just in case our engineers prefer to use JSON cloud formation templates for AWS deployment in the future.
4. Building out all the basic skeleton files of a Django site

The PM asks you to start with Part 1 of the project, which is the command line tools. He pulls up the details on
screen and begins to explain them.


# Part 1

In this task we will be using the `part1` directory as a project to experiment with the
command line and file manipulation in order to show a PoC for generating Django projects.

Your first task will be to figure out how to install the cloned `part1` directory via `pip` in your virtual environment.

Once this is done, the PM lets you know you can move onto developing each of these.

## Requirement 1


Once the command line module is executed, it should print out the message:

```
This is our Django project generator tool set.
```

The project manager noticed something isn't right, but the junior engineer who built this isn't sure why it isn't working.

Your first task is to fix this. The message is there, but something isn't working as expected!


## Requirement 2

We now need to add some flags to our project to handle user input from the command line.

First we want to add a help flag. When the user parses in the help flag it should print the following message

```
Thank you for asking for help. These tools are used to generate a Django project and convert CloudFormation code from YAML to JSON.
```

This should help users of the tool know what it is for. The PM doesn't mind how you handle the flag, just use one of the best tools available in Python for the job.


## Requirement 3

The PM has been told by management, that all projects going forward should have names that are palindromes. This is now department policy. He thought it might be helpful to allow engineers to check if the project name is a palindrome before creating it.

He's decided to call this project `tacocat`.

Add in a new flag that handles this requirement and displays true or false if the project name is/isn't a palindrome.

## Requirement 4

The DevOps team spoke to the PM and mentioned that in the future, they would like to host this project on AWS. It's not a huge concern right now, but some DevOps engineers have complained that they prefer to use JSON rather than YAML, and would like projects to have the ability to convert YAML files to JSON if requested.

There is a YAML file in this repository containing a snippet of Cloud Formation (CF) code for testing with. We now want to add a flag that takes this YAML file as input.

Once the file is input it should convert the contents into a JSON object and output it to a new file
called `tacocat_cf.json`

You can use the following document as a guide to what the output might look like in JSON format:

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-ec2.html

## Requirement 5

We can now check if our project is a palindrome. We've also got the basics for converting YAML to JSON (just in case we want to maintain our CF templates as JSON rather than YAML).

We now need to add a command line task, to create a new Django project skeleton called `tacocat` in the `part2` folder.

So go ahead and add this, and make sure it generates a new project called `tacocat`! You might want to pass in the project name from the commandline, and maybe even re-use your palindrome function, to see if it is a valid name! The Project manager is leaving up those implementation details to you.

Once done, all the basic files needed to start a Django project should be present in the part2/tacocat folder (where tacocat is the project name)

This is deliverable 1. The PM is excited you have made so much progress. It's now time to build out a basic site.


# Part 2.

After lunch you meet back with the PM to discuss setting up Django. Your command line tool now generates all the skeleton files needed for a new Django project.

The PM now asks for a demo and has a list of requirements.

## Requirement 1

You should be able to execute the `runserver` command to show the PM that the project works.

The PM asks if you can create a new README.md file in the `part2` directory and paste a copy of the `runserver` output into it. This will help other junior engineers know what to look for when they start working on the project.

He reminds you to add and commit this to code base, when you are perdiodically pushing you code back up to the fork.


## Requirement 2

As part of the `tacocat` project, the PM needs an app called `seven`.

Your next tasks is going to be to use the `startapp` command to add in the `seven` app skeleton files.


## Requirement 3

The application `seven` needs to take an input via a web form in a View. It should only accept a comma
separated list of integers, for example:

```
1,3,2,1,4,5,3,2,6,2,67,21,6,3
```

How you handle non-integers is up to you!

## Requirement 4

The View needs to be accessible from a URL called `seven/`


## Requirement 5

The PM now wants you to add in some functionality to process the user input.

The list of integers needs to be processed to do the following:

1. Split the integers out of the list
2. Return a unique set of all integer pairs in the list that add up to 7
3. Make sure this runs in linear time.

The View should display the integer pairs in the list that up to 7.

Once this is complete, you are done!


# Project Wrap up

The PM is impressed with your new PoC web app. He asks you to please commit all the code, make a zipfile (or tarball) of the respository. Make sure your name is part of the name of the zipfile (or tarball)

Once ready, you can then email you HR contact at Modus to let them know you have completed the task.

If you found out a mistake and want to send it again, you may do so. Just add something like v1.1 to the tarball and send per email again. If we did not correct yet the excersise, we will use the latest version.


# Modus Create

[Modus Create](https://moduscreate.com) is a digital product consultancy. We use a distributed team of the best talent in the world to offer a full suite of digital product design-build services; ranging from consumer facing apps, to digital migration, to agile development training, and business transformation.

<a href="https://moduscreate.com/?utm_source=labs&utm_medium=github&utm_campaign=python-exercise"><img src="https://res.cloudinary.com/modus-labs/image/upload/h_80/v1533109874/modus/logo-long-black.svg" height="80" alt="Modus Create"/></a>
<br />

