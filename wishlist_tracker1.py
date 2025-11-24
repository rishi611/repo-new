wishlist={}
ttl_bgt=0

def add_item():
    while True:
        name=input("enter item name: [enter exit/EXIT to exit]")
        name=name.lower()
        if(name=="exit"):
            break
        else:
            try:
                price=float(input("enter item price:"))
                if price <= 0:
                    print("price must be positive")
                    continue
                website=input(f"enter a website name (amazon/flipkart/mantra/oth): ")
                website = website.lower()
                priority = input(f"enter priority for purchase (high/medium/low): ")
                priority = priority.lower()

                itm={}
                itm['price']=price
                itm['website']=website
                itm['status']='pending'

                wishlist[name] = itm
                print("item added succesfully")
            except ValueError:
                print("Invalid input, please enter a valid number")

def mark_purchased():
    print(f'\n~Mark as purchased~')
    if len(wishlist)==0:
        print(f'no data available')
        return
    name = input(f'enter item name:')
    name=name.lower()
    if name in wishlist:
        wishlist[name]['status'] = 'purchased'
        print("marked as purchased")
    else:
        print("item not found")
wishlist = {}
total_budget = 0.0


def add_item():
    while True:
        name = input("enter item name [enter exit/EXIT to exit]:")
        name = name.lower()
        if name == "exit":
            break
        try:
            price = float(input("enter item price:"))
            if price <= 0:
                print("price must be positive")
                continue
        except ValueError:
            print("Invalid input, please enter a valid number")
            continue

        website = input("enter a website name (amazon/flipkart/mantra/oth): ")
        website = website.lower()
        priority = input("enter priority for purchase (high/medium/low):")
        priority = priority.lower()

        itm = {"price": price, "website": website, "priority": priority, "status": "pending"}
        wishlist[name] = itm
        print("item added successfully")


def mark_purchased():
    print('\n~Mark as purchased~')
    if len(wishlist) == 0:
        print('no data available')
        return
    name = input('enter item name:')
    name = name.lower()
    if name in wishlist:
        wishlist[name]['status'] = 'purchased'
        print('marked as purchased')
    else:
        print('item not found')


def view_all():
    print('\n~VIEW ALL ITEMS~')
    if len(wishlist) == 0:
        print('no data available')
        return
    for i in wishlist:
        item = wishlist[i]
        print(i, '- rs.', item['price'], '(', item['website'], ') [', item['priority'], '] [', item['status'], ']')


def view_summary():
    print('\n~View Summary~')
    if len(wishlist) == 0:
        print('no data available')
        return

    total_pending = 0.0
    total_purchased = 0.0
    pending_count = 0
    purchased_count = 0

    for i in wishlist:
        if wishlist[i]['status'] == 'pending':
            # each wishlist entry stores its price under the 'price' ke
            total_pending += wishlist[i]['price']
            pending_count += 1
        else:
            total_purchased += wishlist[i]['price']
            purchased_count += 1

    total_items = len(wishlist)
    total_cost = total_pending + total_purchased

    print('total items:', total_items)
    print('pending items:', pending_count)
    print('purchased items:', purchased_count)
    print('pending cost: rs.', total_pending)
    print('purchased cost: rs.', total_purchased)
    print('total cost: rs.', total_cost)


def set_budget():
    global total_budget
    print('\n==SET BUDGET==')
    try:
        total_budget = float(input('enter shopping budget: '))
        if total_budget <= 0:
            print('budget must be positive')
            total_budget = 0
            return
        print('budget set to rs.', total_budget)
    except ValueError:
        print('invalid input. please enter valid number')


def check_budget():
    print('\n~CHECK BUDGET~')
    if total_budget == 0:
        print('budget not set')
        return

    total_pending = 0.0
    for i in wishlist:
        if wishlist[i]['status'] == 'pending':
            total_pending += wishlist[i]['price']

    remaining = total_budget - total_pending
    percentage = (total_pending / total_budget) * 100 if total_budget else 0

    print('budget: rs.', total_budget)
    print('pending cost: rs.', total_pending)
    print('remaining budget: rs.', remaining)
    print('budget used:', round(percentage, 2), '%')
    if percentage > 100:
        print('warning: wishlist exceeds budget')
    elif percentage > 80:
        print('alert: close to budget limit')


def search_item():
    print('\n~~Search Item~~')
    if len(wishlist) == 0:
        print('no data available')
        return
    name = input('enter item name:')
    name = name.lower()
    if name in wishlist:
        item = wishlist[name]
        print(name, '-rs', item['price'], '(', item['website'], ')[', item['status'], ']')
    else:
        print('item not found')


def delete_item():
    print('\n~~Delete Item~~')
    if len(wishlist) == 0:
        print('no data available')
        return
    name = input('enter item name: ')
    name = name.lower()
    if name in wishlist:
        confirm = input('are you sure? (yes/no): ')
        if confirm == 'yes':
            del wishlist[name]
            print('deleted successfully')
        else:
            print('cancelled')
    else:
        print('item not found')


def clear_data():
    print('\n==CLEAR ALL DATA==')
    confirm = input('clear all data? (yes/no): ')
    if confirm == 'yes':
        wishlist.clear()
        global total_budget
        total_budget = 0
        print('all data cleared')
    else:
        print('cancelled')


def filter_by_priority():
    print('\n~Filter by Priority~')
    if len(wishlist) == 0:
        print('no data available')
        return
    choice = input('show (h)igh, (m)edium or (l)ow priority?:')
    choice = choice.lower()
    if choice == 'h':
        print('\nHIGH PRIORITY Items:')
        for i in wishlist:
            if wishlist[i]['priority'] == 'high':
                print(i, '- rs.', wishlist[i]['price'])
    elif choice == 'm':
        print('\nMEDIUM PRIORITY Items:')
        for i in wishlist:
            if wishlist[i]['priority'] == 'medium':
                print(i, '- rs.', wishlist[i]['price'])
    elif choice == 'l':
        print('\nLOW PRIORITY Items:')
        for i in wishlist:
            if wishlist[i]['priority'] == 'low':
                print(i, '- rs.', wishlist[i]['price'])
    else:
        print('invalid input')


def main():
    while True:
        print('\n**MENU**')
        print('enter 1 to add item')
        print('enter 2 to mark as purchased')
        print('enter 3 to view all items')
        print('enter 4 to view summary')
        print('enter 5 to set budget')
        print('enter 6 to check budget')
        print('enter 7 to search item')
        print('enter 8 to delete item')
        print('enter 9 to clear all data')
        print('enter 10 to filter by priority')
        print('enter 11 to exit')
        choice = input('enter choice (1-11): ')
        if choice == '1':
            add_item()
        elif choice == '2':
            mark_purchased()
        elif choice == '3':
            view_all()
        elif choice == '4':
            view_summary()
        elif choice == '5':
            set_budget()
        elif choice == '6':
            check_budget()
        elif choice == '7':
            search_item()
        elif choice == '8':
            delete_item()
        elif choice == '9':
            clear_data()
        elif choice == '10':
            filter_by_priority()
        elif choice == '11':
            break
        else:
            print('\ninvalid input')


if __name__ == '__main__':
    main()

