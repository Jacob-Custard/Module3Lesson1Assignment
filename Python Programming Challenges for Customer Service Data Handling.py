# Task 1 Customer Service Ticket Tracker: Demonstrate your ability to use nested collections and loops by creating a 
#system to track customer service tickets. Develop a program that: tracks customer service tickets, each with a unique ID,
#customer name, issue description, and status (open/closed). Implement funcitons to: open a new service ticket, update the
#status of an existing ticket, display all tickets or filter by status. Initialize with some sample tickets and include functionality
#for additional ticket entry.

def add_ticket(ticket_list, ticket, customer, issue):
    if ticket not in ticket_list:
        ticket_list[ticket] = {"Customer": customer, "Issue": issue, "Status": "open"}
        print(f"{ticket} has been created for {customer}")
    else:
        print(f"{ticket} already exits.")   
        
def status_update(ticket_list, ticket, status):
    if ticket in ticket_list:
        ticket_list[ticket].update({"Status": status})
        print(f"{ticket} status has been updated to {status}")
    else:
        print(f"{ticket} does not exits.")    

def display_tickets(ticket_lists, status):
    status = status.lower()
    if status == "all":
         for ticket, ticket_list in ticket_lists.items():
            print(f"{ticket}: {ticket_list}")
            
    elif status == "open":
         for ticket, ticket_list in ticket_lists.items():
             for catagory, info in ticket_list.items():
                if info == "open":
                    print(f"{ticket}: {ticket_list}") 

    elif status == "closed":
        for ticket, ticket_list in ticket_lists.items():
            for catagory, info in ticket_list.items():
                if info == "closed":
                    print(f"{ticket}: {ticket_list}")
    else:
        print("Status not recognized.") 

                                    
service_tickets = { "Ticket001": {"Customer": "Jacob", "Issue": "brakes squeak", "Status": "open"},
"Ticket002": {"Customer": "Lesli", "Issue": "check engine light", "Status": "open"},
"Ticket003": {"Customer": "John", "Issue": "squeaky belt", "Status": "closed"}}



while True:
    print("What would you like to do?\n1. Add new service ticket\n2. Update service ticket status\n3. Display service tickets\n4. Exit")
    choice =input("Please enter the number associated with the function you'd like to perform (1-4): ")

    if choice =="1":
        ticket_number = input("What is the ticket number of the ticket you're adding? (Ticket001, etc.): ")
        name = input("what is the name of the customer attached to this ticket?: ")
        info = input("What issue is the customer reporting?: ")
        add_ticket(service_tickets, ticket_number, name, info)
    elif choice == "2":
        ticket_number = input("What is the number of the ticket you would like to update?: ")   
        new_status = input("What is the new status of the ticket (open/closed)?: ")
        status_update(service_tickets, ticket_number, new_status)
    elif choice == "3":
        fliter_status = input("Which tickets would you like displayed (all/open/closed)?: ")   
        display_tickets(service_tickets, fliter_status)
    elif choice == "4":
        print("Now exiting the program.")
        break
    else:
        print("Entry not recognized. Please re-enter you're choice (1-4)")
             

    