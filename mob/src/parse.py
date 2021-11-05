from sly import Parser 
from .lexer import MobLexer

class MobParser(Parser):
	
	tokens = MobLexer.tokens

	precedence = (
		('left', '+', '-'),
		('left', '*', '/'),
		('right', 'UMINUS'),
	)

	def __init__(self):
		self.env = { }

	@_('')
	def statement(self, p):
		pass

	@_('var_assign')
	def statement(self, p):
		return p.var_assign

	@_('IDENTIFIER "=" expr')
	def var_assign(self, p):
		return ('var_assign', p.IDENTIFIER, p.expr)

	@_('IDENTIFIER "=" STRING')
	def var_assign(self, p):
		return ('var_assign', p.IDENTIFIER, p.STRING)

	@_('expr')
	def statement(self, p):
		return (p.expr)

	@_('expr "+" expr')
	def expr(self, p):
		return ('add', p.expr0, p.expr1)

	@_('expr "-" expr')
	def expr(self, p):
		return ('sub', p.expr0, p.expr1)

	@_('expr "*" expr')
	def expr(self, p):
		return ('mul', p.expr0, p.expr1)

	@_('expr "/" expr')
	def expr(self, p):
		return ('div', p.expr0, p.expr1)

	@_('"-" expr %prec UMINUS')
	def expr(self, p):
		return p.expr

	@_('VARIABLE IDENTIFIER')
	def expr(self, p):
		return ('var', p.IDENTIFIER)

	@_('INTEGER')
	def expr(self, p):
		return ('num', p.INTEGER)
