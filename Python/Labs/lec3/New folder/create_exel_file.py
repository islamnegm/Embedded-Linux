import Xlsxwriter  

student_Xlx = Xlsxwriter.Workbook("student.Xlsx")

student_sheet = student_Xlx.add_worksheet()

student_sheet.write("A1","Student1")
student_sheet.write("B1","Student2")
student_sheet.write("C1","Student3")
student_sheet.write("D1","Student4")
student_sheet.write("E1","Student5")

student_Xlx.close()