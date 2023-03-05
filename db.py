import json


class StudentDB(object):
    def __init__(self):
        self.students = []
        self._load_students_data()

    def insert(self, student):
        self.students.append(student)
        print(self.students)

    def all(self):
        return self.students

    def delete_by_name(self, name):  # 删除数据
        for student in self.students:
            if name == student["name"]:
                self.students.remove(student)
                break
        else:
            return False
        return True

    # 查询
    def search_by_name(self, name):
        for student in self.students:
            if name == student["name"]:
                return student  # 姓名+成绩
        else:
            return False

    # 修改
    def update(self, stu):  # 修改数据
        name = stu["name"]
        for student in self.students:
            if name == student["name"]:
                student.update(stu)
                return True
        else:
            return False

    # 加载文件
    def _load_students_data(self):
        with open("students.txt", "r", encoding="utf-8") as f:
            text = f.read()
        if text:
            self.students = json.loads(text)

    # 保存数据
    def save_data(self):
        with open("students.txt", 'w', encoding="utf-8") as f:
            text = json.dumps(self.students, ensure_ascii=False)
            f.write(text)


db = StudentDB()