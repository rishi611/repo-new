wishlist={}
ttl_bgt=0

def add_item():
    while True:
        name=input("enter item name [enter exit/EXIT to exit]")
        name=name.lower()
        if(name=="exit"):
            break
        else:
            try:
                price=float(input("enter item price"))
                if price <= 0:
                    print("price must be positive")
                    continue
                website=input(f"enter a website name (amazon/flipkart/mantra/oth): ")
                website = website.lower()
                priority() = input(f"enter priority for purchase (high/medium/low):")
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

def view_all():
    print("\n~VIEW ALL ITEMS~")
    if len(wishlist)==0:
        print("no data available")
        return
    else:
        for i in wishlist:
            print(i,"- rs.",wishlist[i]['price'],"(",wishlist[i]['website'],") [",wishlist[i]['priority'],"] [",wishlist[i]['status'],"]")

def view_summary():
   print("/n~View All Items")
   if len(wishlist)==0:
      print("no data avalilable")
      return
   else:
       total_pending=0
       total_purchased=0
       pending_count=0

       for i in wishlist:
           if wishlist[i]['status']== 'pending':
               total_pending=total_pending + wishlist[i]['pending']
               pending_count = pending_count + 1
           else:
            total_purchased = total_purchased + wishlist[i]['price']
            purchased_count = purchased_count + 1

       total_items=len(wishlist)
       total_cost=total_pending + total_purchased

       print(f"total items:",total_items)
       print(f"pending items:,",pending_count)
       print("purchased items: ",purchased_count)
       print("pending cost: rs.",total_pending)
       print("purchased cost: rs.",total_purchased)
       print("total cost: rs.",total_cost)
def set_budget():
    print("\n==SET BUDGET==")
    try:
        global total_budget
        total_budget =float(input("enter shopping budget: "))
        if total_budget<=0:
            print("budget must be positive")
            total_budget= 0
            return
        print("budget set to rs.",total_budget)
    except ValueError:
        print("invalid input. please enter valid number")

def check_budget():
    print(f"\n~CHECK BUDGET~")
    if total_budget == 0:
        print(f"budget not set")
        return
    total_pending = 0
    for i in wishlist:
        if wishlist[i]['status'] == 'pending':
            total_pending = total_pending + wishlist[i]['price']
    remaining = total_budget - total_pending
    percentage = (total_pending / total_budget) * 100
    print(f"budget: rs.",total_budget)
    print(f"pending cost: rs.",total_pending)
    print(f"remaining budget: rs.",remaining)
    print(f"budget used:",round(percentage, 2),"%")
    if percentage > 100:
        print("warning: wishlist exceeds budget")
    elif percentage > 80:
        print("alert: close to budget limit")
