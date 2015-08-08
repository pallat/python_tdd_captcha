class Captcha:
	def __init__(self, pattern, leftOperand, operator, rightOperand):
		self.pattern = pattern
		self.leftOperand = leftOperand
		self.operator = operator
		self.rightOperand = rightOperand
		self.map_number = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 0:"zero"}

	def left_operand(self):
		operandObj = Operand(self.pattern, self.leftOperand)
		return operandObj.toString()

	def right_operand(self):
		operandObj = Operand(self.pattern, self.rightOperand)
		return operandObj.toString()

	def operator_flag(self):
		operObj = Operator(self.operator)
		return operObj.toString()


class Operator:
	def __init__(self, operator):
		self.operator = operator
		self.map_operator = {1:"+", 2:"*", 3:"-"}

	def toString(self):
		return self.map_operator[self.operator]

class Operand:
	def __init__(self,pattern,operand):
		self.pattern = pattern
		self.operand = operand
		self.map_number = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 0:"zero"}

	def toString(self):
		if self.pattern == 2:
			return self.map_number[self.operand]
		return str(self.operand)