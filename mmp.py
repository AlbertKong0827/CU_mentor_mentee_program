import pandas as pd

pd.set_option('display.max_columns', None)
mentee = pd.read_csv("Mentee.csv")
mentor = pd.read_csv("Mentor.csv")
mentor = mentor.head(17)

CU_all_dept = ["HR","PR","MKT","BD","OP","PM"]

def find_mentee_college(mentor_name):
    mentor_college = pd.Series.to_string(mentor.loc[mentor["Name"] == mentor_name]["学院（College）"]).split("    ")[1]
    mentor_major = pd.Series.to_string(mentor.loc[mentor["Name"] == mentor_name]["专业（major+minor）"]).lower().split("    ")[1].lower()
    mentor_dept = pd.Series.to_string(mentor.loc[mentor["Name"] == mentor_name]["CU部门"]).split("    ")[1]
    print("Mentor姓名："+mentor_name)
    print("所在学院："+mentor_college)
    print("专业："+mentor_major)
    print("部门："+mentor_dept+"\n")

    for i in CU_all_dept:
        if i in mentor_dept:
            mentor_dept = i
        else:
            continue

    mentee_info = mentee[["CU的ID", "Name", "学院（College）", "专业（Major+Minor）", "感兴趣参加的CU部门"]]

    mentee_college_id = mentee_info.loc[mentee_info["学院（College）"]==mentor_college]
    print("与本mentor同学院的mentee如下：")
    print(mentee_college_id)
    print()

    mentee_major_id = mentee_info.loc[mentee_info["专业（Major+Minor）"].str.lower().str.contains(mentor_major)]
    print("与本mentor相似专业的mentee如下：")
    print(mentee_major_id)
    print()

    mentee_dept_id = mentee_info.loc[mentee_info["感兴趣参加的CU部门"].str.contains(mentor_dept)]
    print("想进本mentor部门的mentee如下：")
    print(mentee_dept_id)

find_mentee_college("孔令航")