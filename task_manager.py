
#NOTE: In order for to complete the parts of this code where i have to check if a task is 
#      overdue or not i had to change the formats of the dates given in the first 2 example 
#      tasks in the tasks.txt file.
#      i wasnt sure how i could compare '20 oct 2019' to the date given by the datatime module
#      as it is in the format YYYY-MM-DD, so had to change all the dates of tasks to be in the form
#      YYYY-MM-DD, i hope this is okay
#      So in order for code to work all dates must be in the form of YYYY-MM-DD, i have instructed
#      the user to do this when adding new tasks so i hope it makes sense. 

#      Also, in the tasks file, in order for a new task to be printed on a new line, the file must
#     already have a blank line at the bottom, so for instance if there are 8 tasks in tasks.txt, the file 
#     must have tasks on lines 1-8 then have a line 9 left blank, just so you (code reviewer) are aware.
#     As in my code when adding a new task, '\n' is at the end of the task added, not at the beginning.
#
#     This is to take into account that if tasks.txt was completely blank (i.e has no tasks), that when
#     the first task is added it is printed on line 1 and then prints '\n' so that line 2 is where
#     the next task is added
#
#     Hope that all makes sense.
# 
# #=====importing libraries===========

# Import date class from datetime module
from datetime import date
from pyparsing import stringStart
 
# Returns the current local date
today = date.today()
print(today)

#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
#function to register new user and check if username entered already exists
def reg_user(new_username):
    
    if new_username in correct_unames:
        print(f'The username "{new_username}" already exists.')
            
    else:
        new_password=input("Enter a new password: ")
        password_confirmation=input("Confirm your password: ")
            
        if new_password == password_confirmation:
            
            with open ('user.txt','a') as f: 
                f.write("\n"+new_username + "," + " " + new_password)
                print("\nNew user " + new_username + " has been registered.")
            f.close()
            
        else:
            print("Passwords do not match, please try again. ")   
#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
#function adding a new task to task.txt
def add_task(new_task):
    #full details of 'new task' is determined later om in the code
    with open("tasks.txt","a") as f:
        #writing new task to task file
        f.write(new_task)
        print("\nNew task as been added.")
    f.close()
#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
#functino printing out every task 
def view_all():
    print('''\nThese are all of the tasks:
____________________________\n''')
    with open("tasks.txt","r") as f:
        for line in f.readlines():
            print(line)
    f.close()
#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
#View all of the tasks assigned to the logged in user
def view_mine():
    #creating list of tasks for user logged in
    user_tasks = []

    print("\nThese are your tasks:\n")
    with open("tasks.txt","r") as f:
        for line in f.readlines():
            line = line.strip().split(',')
            
            # only extracting tasks from file if they contain the users username
            if line[0] == username:

                #creating easy to read display of tasks
                task = (f'''------------------------------------------------------------------------------------------------------------------------------------
        TASK:          |{line[1]}|
        ASSIGNED TO:   |{line[0]}|
        DATE ISSUED:   |{line[3]}|
        DUE DATE:      |{line[4]}|
        DESCRIPTION:   |{line[2]}|
        COMPLETE?:     |{line[5]}|
------------------------------------------------------------------------------------------------------------------------------------
        \n''')
        #adding tasks to user_task list so we can find and edit specific tasks by index point later
                user_tasks.append(task)
        
        for i in range(len(user_tasks)):

            #Giving tasks numbers so user can select task they want to edit easily
            print(f'''--------
•Task {i + 1}•
--------''')
            print(user_tasks[i])
#_____________________________________________________________________________________________________
    #TASK EDIT - give user option to pick which task they want to edit or return to main menu
    task_number = int(input("Enter the task number you would like to make a change to, or enter '-1' to return to main menu: "))
    
    if task_number == -1:
        print("\nNo task chosen, returning to main menu")
    
    #displaying the chosen task and givinguser further options to edit the task
    else:
        print(f'''\nYou have chosen to edit task {task_number}.
{user_tasks[task_number-1]}''')
        edit_option = input(f'''Would you like to...
        a - mark task {task_number} as complete
        b - edit username and/or due date of task {task_number}
        
        a/b?: ''')

        #formatting chosen task into same fromat it is in the task file
        task_to_edit = (user_tasks[task_number-1])
        task_split = task_to_edit.replace("\n","").split('|')
        print(f'''\ntask to edit:
        {task_to_edit}''')

        user1 = task_split[3]
        task1 = task_split[1]
        description = task_split[9] #removing the blank spaces from start of description(not sure how they got there)
        issue_date1 = task_split[5]
        due_date1 = task_split[7]
        complete1 = task_split[11]

        task = f'{user1},{task1},{description},{issue_date1},{due_date1},{complete1}'

     #OPTION A ______________________________________________________________________________   
        #changing task complete value from No to Yes, by accessing index positon
        if edit_option == 'a':
            changed_task = f'{user1},{task1},{description},{issue_date1},{due_date1}, Yes'
            all_tasks = []
            all_tasks_ = []
                
            with open("tasks.txt","r") as f:
                all_tasks = f.readlines()
                f.close()
                #formatting task from list to match task in text file so it can be identified and replaced   
                for i in range(0, len(all_tasks)):
                    all_tasks_.append(all_tasks[i].replace("\n",""))

                task_idx = all_tasks_.index(task)
                all_tasks_[task_idx] = changed_task
                
                print("Upadted List of all tasks:\n")
                for i in range(0, len(all_tasks_)):
                    print(all_tasks_[i])
                
                #overwritting whole task file with new list of updated tasks
                with open('tasks.txt','w') as f:
                    for line in all_tasks_:
                        f.write(f'{line}\n')
                f.close()

                print("\nTask has now been marked as complete.")
               
            f.close()
    #OPTION B____________________________________________________________________________________________ 
        # User choice to edit the task
        elif edit_option == 'b':

            #if statement checking if task has been marked as complete, as a complete task cant be edited
            if complete1 == ' No':

                #USER OR DATE EDIT__________________________
                edit_choice = input('''Would you like to...
                a - change the user that that task is assigned to
            or  b - Change the due date of the task
            
                a/b?: ''')
                
                #EDIT TASK USER____________________________________________
                if edit_choice == 'a':
                    new_task_user = input("Enter that the new username that task is assigned to: ")
                    changed_task = f'{new_task_user},{task1},{description},{issue_date1},{due_date1},{complete1}'
                    all_tasks = []
                    all_tasks_ = []

                    with open("tasks.txt","r") as f:
                        all_tasks = f.readlines()
                        f.close()
                        #formatting task from list to match task in text file so it can be identified and replaced  
                        for i in range(0, len(all_tasks)):
                            all_tasks_.append(all_tasks[i].replace("\n","")) 

                        task_idx = all_tasks_.index(task)
                        all_tasks_[task_idx] = changed_task

                        print("Updated list of all tasks:\n:")
                        for i in range(0, len(all_tasks_)):
                            print(all_tasks_[i])

                        #overwritting whole task file with new list of updated tasks
                        with open('tasks.txt','w') as f:
                            for line in all_tasks_:
                                f.write(f'{line}\n')
                        f.close()

                        print(f'\nTask has user has now been updated to {new_task_user}')

                #EDIT TASK DUE DATE _________________________________________
                #I pretty much just copy and pasted the previous code for option a and changed it to new due date from new user
                #same logic as before

                elif edit_choice == 'b':
                    new_due_date = input("Enter the new due date of the task (in format YYYY-MM-DD): ")
                    changed_task = f'{user1},{task1},{description},{issue_date1}, {new_due_date},{complete1}'
                    all_tasks = []
                    all_tasks_ = []

                    with open("tasks.txt","r") as f:
                        all_tasks = f.readlines()
                        f.close()
                        #formatting task from list to match task in text file so it can be identified and replaced  
                        for i in range(0, len(all_tasks)):
                            all_tasks_.append(all_tasks[i].replace("\n","")) 

                        task_idx = all_tasks_.index(task)
                        all_tasks_[task_idx] = changed_task

                        print("Updated list of all tasks:\n:")
                        for i in range(0, len(all_tasks_)):
                            print(all_tasks_[i])
                        #overwritting whole task file with new list of updated tasks
                        with open('tasks.txt','w') as f:
                            for line in all_tasks_:
                                f.write(f'{line}\n')
                        f.close()

                        print(f'\nTask due date has now been updated to {new_due_date}')
                else:
                    print('Invalid option selected')
            else:
                print("Can not edit task if it is already completed")
        else:
            print("invalid option selected")
        #all if else statments above to account for user error handling
        # im not sure if i should be using 'try/except' instead to do this but i personally prefer
        # just to use if else statements instead. 
#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
# function to find all individual statistics about a specific user
def user_info(user):

    #defining lists to contain statistical number
    user_tasks = []
    completed_user_tasks = []
    uncompleted_user_tasks = []
    overdue_user_tasks = []

    # Finding all of users completed and uncompleted tasks
    with open('tasks.txt','r') as f:
        for line in f:
            line = line.split(',')
            #print(line)
            if line[0] == (user):
                user_tasks.append(line)
                if line[5] == ' Yes\n':
                    completed_user_tasks.append(line)
                else:
                    uncompleted_user_tasks.append(line)
    f.close()
    
    # Finding if tasks is over due by comparing the due date to 'today's date from datetime module.
    # I did this by just comparing each individual number in the date but i looked
    # up online a simpler way to do this by simply comparing if 'date1'<'date2' but i couldnt
    # manage to get it working, i will look further into how to use the datetime module more efficiently
    # in the future.

    with open('tasks.txt','r') as f:
        for new_line in f:
            linex = new_line.split(', ')
            if linex[0] == (user):
                date_due = linex[4]
                dd = str(date_due).split('-')
                t = str(today).split('-')
                if dd[0] < t[0]:
                    overdue_user_tasks.append(linex[4])
                else:
                    if dd[1] < t[1]:
                        overdue_user_tasks.append(linex[4])
                    else:
                        if dd[2] < t[2]:
                            overdue_user_tasks.append(linex[4]) 
        
        # finding tasks that are both uncomplete and over due 
        overdue_uncomplete_user_tasks = []

        for i in uncompleted_user_tasks:
            str_i = str(i)
            str_i_split = str_i.split("', ' ")
            for due_date in overdue_user_tasks:
                if due_date == str_i_split[-2]:
                    overdue_uncomplete_user_tasks.append(due_date)   


    f.close()

    # defining values for all nessecary user statistical data
    num_of_user_tasks = len(user_tasks)
    percent_of_total_tasks_assigned_to_user = round((num_of_user_tasks/total_num_of_tasks)*100,1)
    num_of_completed_user_tasks = len(completed_user_tasks)
    number_of_overdue_user_tasks = len(overdue_user_tasks)
    number_of_uncomplete_user_tasks = len(uncompleted_user_tasks)
    number_of_overdue_uncomplete_user_tasks = len(overdue_uncomplete_user_tasks)

    #accounting for division by 0 error. Percentage only calculated if user has more than 0 tasks
    # if user has no tasks assigned they will not be given statistical data as there is none
    if num_of_user_tasks > 0:
        percentage_completed_tasks = round((num_of_completed_user_tasks/num_of_user_tasks)*100,1)
        percent_uncomplete = 100 - percentage_completed_tasks
        percent_overdue_uncomplete = (number_of_overdue_uncomplete_user_tasks/num_of_user_tasks)*100

        users_info = (f'''\n{user} has: 
        {num_of_user_tasks} tasks assigned to them, 
        which is {percent_of_total_tasks_assigned_to_user}% of all of the tasks,
        {percentage_completed_tasks}% of {user}'s task have been completed,
        {percent_uncomplete}% must still be completed,
        {percent_overdue_uncomplete}% of this users task are overdue''')
        
        user_info_list.append(users_info)
        
    else:
        users_info = (f'\n{user} has {num_of_user_tasks} tasks assigned to them')
        user_info_list.append(users_info)

    
#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
#====LOGIN - SECTION====
#create 2 empty lists to store usernames and passwords
correct_unames = []
correct_pwords = []

print('''
====================SYSTEM LOG-IN===================''')


with open("user.txt","r") as f:
    
    #for loop to add usernames and pwords from user.txt to lists
    #correct_unames[0] will be the user name for correct_pwords[0] to make password matches username
    for line in f:

            #formatting data to remove spaces and \n.
            #i tried using '.strip()' to remove the space but it wasnt working for some reason
            #so i just used replace instead which worked
            line = line.replace(" ","").replace("\n","").split(",") 
            correct_unames.append(line[0])
            correct_pwords.append(line[1])

    #while loop to all log in attempts
    while True:

        #only take 'username' input first to determine if user exists         
        username = input("\nEnter username: ")
                
        if username in correct_unames:
                uname_idx = correct_unames.index(username)
                password = input("Enter password: ")
                
                if password == correct_pwords[uname_idx]: #making sure password matches the username rather than any password
                        print("\nLog-in successful!")
                        break
                else:
                        print("\nWrong password for that username")
        
        elif username not in correct_unames:
                print("\nUsername not recognised, try again:") #while loop allows user to attempt until successful log in

#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
                    
#successful log in
#creating user menu   
             
while True:
    menu = input('''
========================= USER-MENU ===============================
      ••• Select one of the following options below: •••

         |r - reg a user|            |a - add a task|

|va - view all tasks|  |vm - view my task|   |gr - generate reports|

      |ds - display statistics|         |e - exit program|

Enter option: ''')

#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
#registering a new user and adding to txt file
    if menu == 'r':
            
        if username == "admin": #making sure only the admin can register new user
            new_username = input("\nEnter the new username: ")
            reg_user(new_username)
      
        
        
#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
#adding a new task to task file         
    elif menu == 'a':

        #take in all task info
        user = input("\nEnter the user the task is assigned to: ")
        title = input("Enter the title of the task: ")
        description = input("Enter a description of the task: ")
        due_date = input("Enter the date the task is due(YYYY-MM-DD): ")
        date_assigned = str(today)
        
        new_task = (f'{user}, {title}, {description}, {date_assigned}, {due_date}, No\n')

        add_task(new_task)
   
#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
#view all tasks
    elif menu == 'va':
        view_all()
#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
#view specific task for user
    elif menu == 'vm':
        view_mine()
#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
    elif menu == 'gr':

        print('''\nOverview Reports "task_overview.txt" and "user_overview.txt" have now been generated.
Statistical data from these report files can be view by selected option "ds".''')
        #TASK OVERVIEW_______________________________________________________________________________
        total_task_list = []
        with open('tasks.txt','r') as f:
            for line in f:
                total_task_list.append(line)
        f.close()
        total_num_of_tasks = len(total_task_list)
        #________________________________________________________________________________________
        total_completed_task_list = []
        total_uncompleted_task_list = []

        with open('tasks.txt','r') as f:
            for line in f:
                line = line.split(',')
                if line[-1] == ' Yes\n':
                    total_completed_task_list.append(line)
                else:
                    total_uncompleted_task_list.append(line)
        f.close()
        #________________________________________________________________________________________
        #OVERDUE TASKS
        overdue_tasks = []
        with open('tasks.txt','r') as f:
            for line in f:
                line = line.split(', ')
                date_due = line[-2]
                dd = str(date_due).split('-')
                t = str(today).split('-')
                if dd[0] < t[0]:
                    overdue_tasks.append(line[-2])
                else:
                    if dd[1] < t[1]:
                        overdue_tasks.append(line[-2])
                    else:
                        if dd[2] < t[2]:
                            overdue_tasks.append(line[-2])
        f.close()
        
        overdue_uncomplete_tasks = []
        #print(overdue_tasks)
        #print(total_uncompleted_task_list)
        for i in total_uncompleted_task_list:
            str_i = str(i)
            str_i_split = str_i.split("', ' ")
            for due_date in overdue_tasks:
                if due_date == str_i_split[-2]:
                    overdue_uncomplete_tasks.append(due_date)   
      
    
        #__________________________________________________________________________________________
        #defining values for all nesecary statistical data
        total_tasks = len(total_task_list)
        total_num_completed_tasks = len(total_completed_task_list)
        total_num_uncompleted_tasks = len(total_uncompleted_task_list)
        total_overdue_tasks = len(overdue_tasks)
        percentage_uncomplete_tasks = round((total_num_uncompleted_tasks/total_num_of_tasks)*100,1)
        percentage_overdue_tasks = round((total_overdue_tasks/total_num_of_tasks)*100,1)
        total_overdue_uncomplete_tasks = len(overdue_uncomplete_tasks)
        #__________________________________________________________________________________________
        #writing task data to task overview file
        taskf = open('task_overview.txt','w')
        taskf.write(f'''The total number of tasks is {total_tasks},
Total num of completed tasks is {total_num_completed_tasks}.
Total num of uncompleted tasks is {total_num_uncompleted_tasks}.
Percentage of uncomplete tasks is {percentage_uncomplete_tasks}%.
The percentage of tasks that are overdue is {percentage_overdue_tasks}%
The total number of overdue tasks is {total_overdue_tasks}
The total number of overdue and uncomplete tasks is {total_overdue_uncomplete_tasks}''')
        taskf.close()

        #USER OVERVIEW________________________________________________________________________________
        total_user_list = []
        total_task_list = []
        list_of_users = []
        #Finding total number of users______________________________________________________________
        with open('user.txt','r') as f:
            for line in f:
                total_user_list.append(line)
        f.close()
        total_num_of_users = len(total_user_list) 
        #Total number of tasks_________________________________________________________________
        with open('tasks.txt','r') as f:
            for line in f:
                total_task_list.append(line)
        f.close()
        total_num_of_tasks = len(total_task_list)
        #__________________________________________________________________________________________
        #__________________________________________________________________________________________        
        with open('user.txt','r') as f:
            for line in f:
                line = line.split(',')
                list_of_users.append(line[0])
        f.close()

        user_info_list = []
        
        # writing user statistical data found by user_info function to user overview file
        for name in list_of_users:
            user = name
            user_info(user)

        userf = open('user_overview.txt','w')
        userf.write(f'''Total numebr of users is {total_num_of_users}.
Total number of tasks is {total_num_of_tasks}.''')
        for info in user_info_list:
            userf.write(info)

        userf.close()

#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
    # displaing new statistics from overview files
    elif menu == 'ds':
        
        try:
            print('\n===========TASK OVERVIEW===========\n')
            with open('task_overview.txt','r') as f:
                for line in f:
                    print(line)
            f.close()

            print('\n==========USER OVERVIEW============\n')
            with open('user_overview.txt','r') as f:
                for line in f:
                    print(line)
            f.close()

        except FileNotFoundError as error:
            print('\nOverview files have not been generated, please select "gr" first before displaying statistics')

#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
#final option to fully exit program
    elif menu == 'e':
        break

#••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
#accounting for user error
    else:
        print("\nInvalid option selected, try again.")
            
                    
        


























                

