to_do_list=["buy groceries","pay bills","cook the food"]
## adding a task
to_do_list.append("do exercise")
to_do_list.append("go for run")
##removing tasks
to_do_list.remove("buy groceries")
## checking if a task is in the list
if "pay bills" in to_do_list:
  print("don't forget to pay bills")
  print(to_do_list)
