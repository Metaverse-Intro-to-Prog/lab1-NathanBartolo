# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 22:25:29 2023

@author: natha

You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.

•Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.

•Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.

•Print a second set of invitation messages, one for each person who is still in your list.

   

"""

guest =  ["ankol","kenlee","nayumi"]

name =guest[0].title()
print(f"{name},I am inviting you to dinner")

name =guest[1].title()
print(f"{name},Can u come tonight for dinner?")

name =guest[2].title()
print(f"{name},Dinner tonight?")

name = guest[1].title()
print(f"\nSorry, {name} can't make it to dinner.")

# Jack can't make it! Let's invite Gary instead.
del(guest[1])
guest.insert(1, 'leiko')

# Print the invitations again.
name = guest[0].title()
print(f"\n{name}, please come to dinner.")

name = guest[1].title()
print(f"{name}, please come to dinner.")

name = guest[2].title()
print(f"{name}, please come to dinner.")