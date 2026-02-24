class EligibilityRound:
    def __init__(self, percent_li):
        self.percent_li = percent_li
        self.total_round_li = []

    def get_total_round(self):
        for percent in self.percent_li:
            if percent <= 70:
                self.total_round_li.append('NA')
            elif percent > 70 and percent < 85:
                self.total_round_li.append('3R')
            elif percent >= 85 and percent <= 100:
                self.total_round_li.append('1R')
            else:
                self.total_round_li.append('Invalid percentage')
        return self.total_round_li


number_of_marks = int(input("Enter the number of students: "))
print("Enter", number_of_marks, "entries to calculate!")

percent_li = []
for i in range(number_of_marks):
    u_ip = float(input("Enter value: "))
    percent_li.append(u_ip)


eligibility_round = EligibilityRound(percent_li)
total_round_li = eligibility_round.get_total_round()

print("Final Round Details:", total_round_li)