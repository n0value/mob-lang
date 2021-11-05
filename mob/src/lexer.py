from sly import Lexer 

class MobLexer(Lexer): # extends Lexer
    tokens = { IDENTIFIER, INTEGER, STRING, VARIABLE }
    ignore = "\t "
    literals = { "=", "+", "-", "*", "/" }

    IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'
    VARIABLE = r'\$'
 


    @_(r'\d+')
    def INTEGER(self, t):
        t.value = int(t.value)
        return t

    @_(r'--.*')
    def COMMENT(self, t):
        pass 

    @_(r'\n+')
    def NEWLINE(self, t):
        self.lineo = t.value.count('\n')
