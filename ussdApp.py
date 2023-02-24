options = {"1.":"Data Plans", "2.":"Social Bundles", "3.":"Balance Check", "4.":"Roaming/Int'l"}

option_data_plans = {"1.":{"Daily":{"1.":"N50 for 40MB", "2.":"N100 for 100MB", "3.":"N100 for 350MB(IG/TIKTOK/Youtube)"}},                 "2.":{"Weekly":{"1.":"N200 for 1GB(IG/TikTok/Youtube ONLY)", "2.":"N300 for 350MB", "3.":"N500 for 1.5GB"}},              "3.":{"Monthly":{"1.":"N1,000 for 1.5GB", "2.":"N1,200 for 2GB", "3.":"N1,500 for 3GB"}}}

option_social_bundles = {"1.":{"Whatsapp":{"1.":"Daily @ N25 for 25MB", "2.":"Weekly @ N50 for 50MB", "3.":"Monthly @ N150 for 150MB"}},       "2.":{"Facebook":{"1.":"Daily @ N25 for 25MB", "2.":"Weekly @ N50 for 50MB", "3.":"Monthly @ N150 for 150MB"}},       "3.":{"Instagram":{"1.":"N100 for 250MB/1 day", "2.":"N100 for 250MB", "3.":"N200 for 1GB"}}}

option_roaming = {"1.":{"TravelPass Plans":{"1.":"7days TravelPass @N5000", "2.":"14days TravelPass @N10000", "3.":"7days TravelPass (Data) @N5000"}},                                                                                                                                  "2.":{"Data Hybrid":{"1.":"Eligible Bundles", "2.":"Eligible Destinations"}},                                                                                                                            "3.":{"Inflight Roaming Data":{"1.":"50MB @N2,000", "2.":"View Airlines"}}}

code = input("Please enter USSD code: ")

[daily_plan, weekly_plan, monthly_plan] = option_data_plans.values()
[a, b, c] = option_data_plans.keys()
[whatsapp_plan, facebook_plan, instagram_plan] = option_social_bundles.values()
[travelpass_plans, data_hybrid, inflight_roaming_data] = option_roaming.values()

while code != "*131#":
    code = input("Invalid entry, please try again: ")
while code == "*131#":
    for x,y in options.items():
        print(x,y)
    print("0. Cancel")
    user_option = input("Select an option: ")
    if user_option == "0":
        break
    elif user_option == "1" or user_option == "2" or user_option == "3" or user_option == "4":
        while user_option == "1":
            for x, y in daily_plan.items():
                print(a, x)
            for u, v in weekly_plan.items():
                print(b, u)
            for e, f in monthly_plan.items():
                print(c, e)
            print("0. back")
            user_option_data_plans = input("Select a data plan: ")
            if user_option_data_plans == "0":
                    break
            else:
                while user_option_data_plans == "1":
                    for m, n in y.items():
                        print(m,n)
                    print("0. back")
                    user_option_data_plans = input("Select data amount: ")
                    if user_option_data_plans == "0":
                        break
                while user_option_data_plans == "2":
                    for m, n in v.items():
                        print(m,n)
                    print("0. back")
                    user_option_data_plans = input("Select data amount: ")
                    if user_option_data_plans == "0":
                        break
                while user_option_data_plans == "3":
                    for m, n in f.items():
                        print(m,n)
                    print("0. back")
                    user_option_data_plans = input("Select data amount: ")
                    if user_option_data_plans == "0":
                        break
        while user_option == "2":
            for x, y in whatsapp_plan.items():
                print(a, x)
            for u, v in facebook_plan.items():
                print(b, u)
            for e, f in instagram_plan.items():
                print(c, e)
            print("0. back")
            user_option_data_plans = input("Select social media: ")
            if user_option_data_plans == "0":
                    break
            else:
                while user_option_data_plans == "1":
                    for m, n in y.items():
                        print(m,n)
                    print("0. back")
                    user_option_data_plans = input("Select data amount: ")
                    if user_option_data_plans == "0":
                        break
                while user_option_data_plans == "2":
                    for m, n in v.items():
                        print(m,n)
                    print("0. back")
                    user_option_data_plans = input("Select data amount: ")
                    if user_option_data_plans == "0":
                        break
                while user_option_data_plans == "3":
                    for m, n in f.items():
                        print(m,n)
                    print("0. back")
                    user_option_data_plans = input("Select data amount: ")
                    if user_option_data_plans == "0":
                        break
        while user_option == "4":
            for x, y in travelpass_plans.items():
                print(a, x)
            for u, v in data_hybrid.items():
                print(b, u)
            for e, f in inflight_roaming_data.items():
                print(c, e)
            print("0. back")
            user_option_data_plans = input("Select a plan: ")
            if user_option_data_plans == "0":
                    break
            else:
                while user_option_data_plans == "1":
                    for m, n in y.items():
                        print(m,n)
                    print("0. back")
                    user_option_data_plans = input("Select option: ")
                    if user_option_data_plans == "0":
                        break
                while user_option_data_plans == "2":
                    for m, n in v.items():
                        print(m,n)
                    print("0. back")
                    user_option_data_plans = input("Select option: ")
                    if user_option_data_plans == "0":
                        break
                while user_option_data_plans == "3":
                    for m, n in f.items():
                        print(m,n)
                    print("0. back")
                    user_option_data_plans = input("Select option: ")
                    if user_option_data_plans == "0":
                        break
    else:
        while user_option != "1" and user_option != "2" and user_option != "3" and user_option != "4":
            user_option = input("Invalid entry, try again: ")