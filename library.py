import sys
import csv
import re
from collections import Counter

class Fine:
    def __init__(self,title,email,days_overdue):
        self.title=title
        self.email=email
        self.days_overdue=days_overdue
    @property
    def amount(self):
       amt=int(self.days_overdue)*(0.25)
       return min(amt,10)

    def __str__(self):
        return f"{self.email}'s copy of {self.title} owes ${self.amount:.2f}"        

def total_fines(fines):
         total=0
         for fine in fines:
           total+=fine   
         return f"The Total Fines of the Library is ${total:.2f}"

def main():
    with open("report.txt","w") as report:
        fines=[]
        emails=[]
        try:
            if len(sys.argv)!=2:
                print("Python Filename Usage",file=sys.stderr)
                sys.exit(1)
            with open(sys.argv[1]) as file:
                    text=csv.DictReader(file)
        except FileNotFoundError:
            print("File Not Found")
            sys.exit(1)

        with open(sys.argv[1]) as file:
            text=csv.DictReader(file)
            for row in text:
                        valid=re.search(r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9_.]+\.(com|net|gov|edu)$",row["borrower_email"])
                        if not valid:
                            print(f"{row["borrower_email"]} is not valid",file=sys.stderr)
                            continue
                        try:
                            if int(row["days_overdue"])>=0:
                                clean_days=int(row["days_overdue"])
                            
                            elif int(row["days_overdue"])<0:
                                clean_days=0
                                            
                        except ValueError:
                            clean_days=0
                            

                        fine=Fine(row["title"],row["borrower_email"],clean_days)
                        fines.append(fine.amount)
                        print(fine,file=report);print(fine)
                        emails.append(fine.email)

        counts=Counter(emails)
        borrower=counts.most_common(1)
        print(borrower,file=report); print(borrower)
        
        print(total_fines(fines),file=report) ;print(total_fines(fines))
        

    
        

                   
        



if __name__=="__main__":
    main()        