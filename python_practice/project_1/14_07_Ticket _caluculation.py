
"""
# # Author Anilkumar
# # problem Statement:
# # input : for Male 
            for age<60 - fees_structure Rs500 
                age>60 
                    for government employee-  Rs100
                    for non-government employee- Rs200
            for children 
                    fees_structure-Rs25
            for Female
            for age<58 fees_structure - Rs400
            for age>58
                    for government employee-  Rs75
                    for non-government employee- Rs175
            for Foriegner 
                for male -Rs1500
                for female-Rs1000
            
             fees_structure - Rs400
                    
               
Ticket caliculation of prices

"""

#dict_1={Indian,Foreigner}  mistake of defining dictionary

fees_structure ={"Indian": {"Male":
                                 {"old_aged":{"government":100,
                                              "non_government":200},
                                  "normal_aged":500},
                            "Female":
                                 {"old_aged":{"government":75,
                                              "non_government":175},
                                  "normal_aged":400},
                             "Children":25
                             },
                "Foriegner":{"Male":1500,
                             "Female":1000,
                             "Children":1200}}

name = str(input("Enter the name of the person:"))
nationality = str(input("Enter the nationality of the person:"))
sex = str(input("Enter the sex of the person:"))
age = int(input("Enter the age of the person:"))
job_status = str(input("Enter the job_status of the person:"))


if nationality=="Indian":
    if sex=="Male":
        if age>60:
            if job_status=="government":
                fees = fees_structure["Indian"]["Male"]["old_aged"]["government"]
            elif job_status=="non_government":
                fees = fees_structure["Indian"]["Male"]["old_aged"]["non_government"]
            else :
                print(f"wrong input for {nationality} {sex} {age} {job_status}")
        else:
            fees = fees_structure["Indian"]["Male"]["normal_aged"]

    elif sex=="Female":
        if age>58:
            if job_status == "government":
                fees = fees_structure["Indian"]["Female"]["old_aged"]["government"]
            elif job_status == "non_government":
                fees = fees_structure["Indian"]["Female"]["old_aged"]["non_government"]
            else :
                print(f"wrong input for  {nationality} {sex} {age} {job_status}")
        else:
            fees = fees_structure["Indian"]["Female"]["normal_aged"]
    elif sex=="Children":
        fees = fees_structure["Indian"]["Children"]
    else:
        print(f"wrong input for {nationality} {sex}")
elif nationality=="Foriegner":
    if sex == "Male":
        fees = fees_structure["Foriegner"]["Male"]
    elif sex == "Female":
        fees = fees_structure["Foriegner"]["Female"]
    elif sex == "Children":
        fees = fees_structure["Foriegner"]["Children"]
    else:
        print(f"wrong input for {nationality} {sex}")
else:
    print(f"wrong input for {nationality}")







