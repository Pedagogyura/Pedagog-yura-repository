import sign
import poems
from poems import POEM_ONE, POEM_TWO

author_name = "Юрій Дерішов"

format_data = sign.HOMEWORK_OWNER.format(name=author_name)
print(format_data)

wishes = "Поглиблене розуміння Python\nПрактичні завдання для реального досвіду"
print(wishes)

line = "**************************************************************************"
print(line)
print(POEM_ONE)
print(line)
print(POEM_TWO)
print(line)
