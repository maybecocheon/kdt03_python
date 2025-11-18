class Student:
    def __init__(self, name, age, scores):
        self.name = name
        self.age = age
        self.scores = scores

    def average(self):
        return sum(self.scores) / len(self.scores)

    def show(self):
        print(f"{self.name}의 평균 점수는 {self.average():.1f}점입니다.")

    def is_passed(self):
        return self.average() >= 60

    def __str__(self):
        status = "합격" if self.is_passed() else "불합격"
        return f"{self.name} (나이: {self.age}) - 평균: {self.average():.1f}점, 결과: {status}"

if __name__ == "__main__":
    students = [
        Student("홍길동", 18, [80, 75, 90]),
        Student("김유신", 17, [55, 60, 58]),
        Student("유관순", 18, [95, 88, 92]),
        Student("강감찬", 19, [40, 50, 45])
    ]

    for s in students:
        print(s)
        s.show()
        print()