import json
import xml.etree.ElementTree as ET

from FileManager import FileManager
from Students import Student

class MainProgram:

    def obj_dict(self,obj):
        return obj.__dict__
    
    def object_to_xml(self, obj):
        root = ET.Element(obj.__class__.__name__)

        ET.SubElement(root, "name").text = str(obj.name)
        ET.SubElement(root, "email").text = str(obj.email)
        ET.SubElement(root, "exam").text = str(obj.exam)
        ET.SubElement(root, "note").text = str(obj.note)
        ET.SubElement(root, "grade").text = str(obj.grade)
        ET.SubElement(root, "group").text = str(obj.group)
        ET.SubElement(root, "shift").text = str(obj.shift)
        print(ET.tostring(root, encoding='unicode'))

    def example(self):
        test = FileManager()
        test.read_entire_file('example.txt', 'r')
        test.get_file_lines('example.txt', 'r')
        test.read_line_by_line('example.txt', 'r')
        #student = Student()
    
    def writting_example(self):
        test = FileManager()
        test.write_text('example2.txt', "test text")

    def object_to_json(self, obj):
        json_pretty = json.dumps(obj, default=self.obj_dict, indent=4)
        print(json_pretty)
        
    def create_dataset(self, path, mode): 
        test = FileManager()
        f_lines=test.get_file_lines(path, mode)[:]
        students=[]
        i = 0
        for tmpStudent in f_lines:
            if i>0:
                student = tmpStudent.split("|")
                student_obj=Student(
                    self.format_name(student[0]),
                    student [1].rstrip(),
                    student[2].strip(),
                    student[3].strip(),
                    "2","I","V"
                )
                students.append(student_obj)
            i=i+1
        return sorted(students, key=lambda p: p.name)
    
    def format_name(self, name_to_order):
        parts =name_to_order.rstrip().title().split(" ")
        if len(parts)== 3:
            return parts[1] + ' ' + parts[2] + ' ' + parts[0]
        else:
            
            return parts[2] + ' ' + parts[3] + ' ' + parts[0] + ' ' + parts[1]
        
    def create_csv(self,list):
        trxt = "name ,email,exam,note,gradegroup,,shift,\n"
        fm =FileManager()
        for student in list:
            text = text + f"{student.name},{student.email},{student.exam},{student.note},{student.grade,},{student.group},{student.shift},\n"
            fm.write_text("student.csv",text)

def create_ini(self, list):
    text = ""
    fm = FileManager()
    for i in range(len(list)):
        text = text + f"""[student:{i}]

name={student.name}
email={student.email}
exam={student.exam}
note={student.note}
grade={student.grade}
group={student.shift}\n"""
    fm.write_text("student.ini",text)
              

    
















student_list=[]
student=Student(
            "Franco Garcia David Alejandro",
            "david.franco.2025.tmp@mit.edu",
            5,1,2,"I","V")

student_list.append(student)

main = MainProgram()
list = main.create_dataset("2-J mit.txt","r")
#main.example()
#main.writting_example()
main.object_to_json(list)
#main.object_to_xml(student)        

