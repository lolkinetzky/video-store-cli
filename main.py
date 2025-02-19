import requests
from video_store import Video_store

#URL = "http://localhost:5000"
URL = "https://retro-video-store-api.herokuapp.com"

def main():
    print(u"\u001b[34;1mWELCOME TO BRICKBUSTER\u001b[0m")
    #pass


if __name__ == "__main__":
    main()

def print_stars():
    
        print("______________________________________________________________________")
        print(u"\u001b[41m___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__")
        print("_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|")
        print("___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__")
        print("_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|\u001b[0m")
        
    
def houston_we():
            print("                                  _______                     ")
            print("         _________       .----''''       ''''----.            ")
            print("        :______.-':      :  .-----------------.  :             ")
            print("        | ______  |      | :                   : |             ")
            print("        |:______B:|      | |   Little Error:   | |             ")
            print("        |:______B:|      | |                   | |             ")
            print("        |:______B:|      | |  Item  not        | |             ")
            print("        |         |      | |  found.           | |             ")
            print("        |:_____:  |      | |                   | |             ")
            print("        |    ==   |      | :                   : |             ")
            print("        |       O |      :  '-----------------'  :             ")
            print("        |       o |      :'-----...______...-----'             ")
            print("        |       o |-._.-i_____/'             \._               ")
            print("        |'-.____o_|   '-.     '-...______...-'  `-._           ")
            print("        :_________:      `.____________________   `-.___.-.    ")
            print("                         .'.eeeeeeeeeeeeeeeeee.'.      :___:   ")
            print("            fsc        .'.eeeeeeeeeeeeeeeeeeeeee.'.            ")
            print("                      :____________________________:           ")


def list_options():
    options = {
        "1": "List all videos in stock", 
        "2": "Create a new video record",
        "3": "Select a video", 
        "4": "Update selected video", 
        "5": "Delete selected video", 
        "6": "Delete all videos in stock",
        "7": "List all options",
        "8": "Quit",
        "9": "Rent out a video",
        "10": "Return a video",
        "11": "List all customers", 
        "12": "Add a new customer",
        "13": "Update selected customer", 
        "14": "Delete selected customer",
        "15": "Select a customer"
        }

    print_stars()
    print(u"\u001b[34m                    Good to see You")
    print("          These are the actions you can perform\u001b[0m")
    print_stars()
    #houston_we()
    
    for choice_num in options:
        print(f"\u001b[34mOption {choice_num}. {options[choice_num]}\u001b[0m")

    print_stars()

    return options

def make_choice(options, video_store):
    valid_choices = options.keys()
    choice = None

    while choice not in valid_choices:
        print("What would you like to do? Select 7 to see all options again")
        choice = input("Make your selection using the option number: ")

    if choice in ['4','5'] and video_store.selected_video == None:
        print("You must select a video before updating or deleting it")
        print("Let's select a video!")
        choice = "3"

    elif choice in ['13', '14'] and video_store.selected_customer == None:
        print("You must select a customer before updating or deleting it")
        print("Let's select a customer!")
        choice = "15"

    return choice

def run_cli(play=True):

    video_store = Video_store(URL)
    
    options = list_options()

    while play==True:

        
        choice = make_choice(options, video_store)

        if choice=='1':
            print_stars()
            for video in video_store.list_videos():
                print(video)

        elif choice=='2':
            print("Great! Let's create a new video.")
            title=input("What is the name of the video? ")
            release_date=input("When was this movie released?")
            total_inventory=input("How many copies of this video are we adding?")
            response = video_store.create_video(title=title, release_date=release_date, total_inventory= total_inventory)

            print_stars()
            print("New video:", response)

        elif choice=='3':
            select_by = input("Would you like to select by? Enter title or id: ")
            if select_by=="title":
                title = input("Which title would you like to select? ")
                video_store.get_video(title=title)
            elif select_by=="id":
                video_id = input("Which video id would you like to select? ")
                if video_id.isnumeric():
                    video_id = int(video_id)
                    video_store.get_video(video_id=video_id)
            else:
                print("Could not select. Please enter id or title.")
            
            if video_store.selected_video:
                print_stars()
                print("Selected video: ", video_store.selected_video)
        
        elif choice=='4':
            print(f"Great! Let's update the movie: {video_store.selected_video}")
            title=input("What is the title of your new video? ")
            release_date=input("When was it released?")
            total_inventory=input("How many copies do you have available to add to stock?")
            response = video_store.update_video(title=title, release_date=release_date, total_inventory=total_inventory)

            print_stars()
            print("video:", response)

        elif choice=='5':
            video_store.delete_video()

            print_stars()
            print("Movie has been deleted.")

            print_stars()

        elif choice=='6':
            for video in video_store.list_videos():
                video_store.get_video(video_id=video['id'])
                video_store.delete_video()

            print_stars()
            print("Deleted all videos in stock. Out with the old.")

        elif choice=='7':
            list_options()

        elif choice=='8':
            play=False
            print("\nThanks!")

        elif choice =='9':
            customer_id = input("Which customer is renting today? (please provide customer id)")
            video_id = input("Which video would they like to rent? (please provide video id)" )
            response = video_store.check_out_video(int(customer_id), int(video_id))
            if response != 200:
                houston_we()
            print(response) 
            print_stars()

        elif choice =='10':
            customer_id = input("Which customer is returning today? (please provide customer id)")
            video_id = input("Which video are they returning? (please provide video id)")
            response = video_store.check_in_video(int(customer_id), int(video_id))
            print(response) 
            print_stars()

        
        elif choice =='11':
            print_stars()
            for customer in video_store.list_customers():
                print(customer)
        
        elif choice =='12':
            print("Great! Let's add a new customer.")
            name=input("What is the name of customer?")
            phone=input("Please add customer's phone number ->")
            postal_code=input("Please add customer's postal code ->")
            response = video_store.create_customer(name=name, phone=phone, postal_code= postal_code)

            print_stars()
            print("New customer:", response)
         
        elif choice =='13':
            print(f"Great! Let's update the customer {video_store.selected_customer}'s record")
            name=input("What is the new name of customer?")
            phone=input("Please add customer's new phone number ->")
            postal_code=input("Please add customer's new postal code ->")
            response = video_store.update_customer(name=name, phone=phone, postal_code= postal_code)

            print_stars()
            print("Customer:", response)
        
        elif choice == '14':
            video_store.delete_customer()

            print_stars()
            print("Customer has been deleted.")

            print_stars()

        elif choice == '15':
            select_by = input("Would you like to select your cutomer by? Enter name or id: ")
            if select_by=="name":
                title = input("Which customer would you like to select by name? ")
                video_store.get_customer(customer=customer)
            elif select_by=="id":
                customer_id = input("Which customer id would you like to select? ")
                if customer_id.isnumeric():
                    customer_id = int(customer_id)
                    video_store.get_customer(customer_id=customer_id)
            else:
                print("Could not select. Please enter id or name.")
            
            if video_store.selected_customer:
                print_stars()
                print("Selected customer: ", video_store.selected_customer)

        print_stars()


run_cli()

