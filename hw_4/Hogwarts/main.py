from Hogwarts import *

spell = Spell('Expelliarmus','Дизармирование противника', 10)
spell1 = Spell('Stupefy','Оглушение противника', 30)
spell2 = Spell('Avada Kedavra','Смертельное ранение', 70)
spell3 = Spell('Protego','отражающий заклинания', 20)
spell4 = Spell('Petrificus Totalus','Полная парализация противника', 40)
spell5 = Spell('Lumos','Создание источника света ', 10)
spell6 = Spell('Expecto Patronum','Призывание патронуса', 60)

student1 = HogwartsStudent('Harry','Grifendor', 50)
student2 = HogwartsStudent('Malfoy ','Slytherin', 50)

hogwarts = Hogwarts()
hogwarts.enroll_student(student1)
hogwarts.enroll_student(student2)

hogwarts.teach_spell(spell)
hogwarts.teach_spell(spell1)

student1.learn_spell(spell,hogwarts)
student1.learn_spell(spell1,hogwarts)

student2.learn_spell(spell,hogwarts)
student2.learn_spell(spell1,hogwarts)


hogwarts.simulate_duel(student1,student2)