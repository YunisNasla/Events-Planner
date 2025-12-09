from Date import *
from Event import *

def overlap_check(event_list, new_event):
    for event in event_list:
        if event.event_date == new_event.event_date:
            if not (event.end_hour <= new_event.start_hour or new_event.end_hour <= event.start_hour):
                print(f"\nThere is an overlap with event: {event.event_name}")
                return True
        
    return False

def main():
    event_list = []
    while True:
        
        choice = input("\nEnter 1) to Add an Event to the list, 2) Cancel an Event, 3) View all Events, 4) to Quit: ")

        if choice == "1":
            day = int(input("Day of event (1-31): "))
            month = int(input("Month of event (1-12): "))
            year = int(input("Year (ex. 2025): "))

            start_hour = int(input("Start hour (0-23): "))
            end_hour = int(input("End hour (0-23): "))
            
            event_name = input("Event name: ")

            event_date = Date(day, month, year)

            new_event = Event(event_date, event_name, start_hour, end_hour)

            if overlap_check(event_list, new_event):
                print("Event not added due to overlap.")
            else:
                event_list.append(new_event)
                print("New event added.")

        elif choice == "2":
            name = input("Enter the name of the canceled event: ").lower()
            found_event = None

            for event in event_list:
                if event.event_name.lower() == name:
                    found_event = event
                    break

            if found_event:
                event_list.remove(found_event)
                print(f"Event '{name}' has been canceled.")
            else:
                print(f"Cannot Cancel. {name} not in event list!")

        elif choice == "3":
            if not event_list:
                print("There are no events scheduled.")
            else:
                print("Scheduled Events:\n")
                for event in event_list:
                    print(event)
                
        elif choice == "4":
            break

main()