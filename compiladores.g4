grammar compiladores;

fragment LETRA : [A-Za-z] ;
fragment DIGITO : [0-9] ;

// NUMERO : DIGITO+ ;

// CARACTERES ESPECIALES
PUNTO: '.';
COMA:',';
PYC: ';';
DOS_PUNTOS: ':';
LLAVE_ABRE: '{';
LLAVE_CIERRE: '}';
PAR_ABRE: '(';
PAR_CIERRE: ')';
CORCH_ABRE: '[';
CORCH_CIERRE: ']';
BARRA_INVERSA: '\\';
BARRA_RECTA: '|';
ANDPERSAND: '&';
PROCENTAJE: '%';
COMILLA_SIMPLE: '\'';
COMILLA_DOBLE: '"';
GUION_BAJO: '_';

WS: [ \t\n\r] -> skip;

// TIPOS DE VARIABLES
INT: 'int';
FLOAT: 'float';
DOUBLE: 'double';
BOOLEAN: 'bool'; //TODO: VER SI ES BOOL O BOOLEAN
CHAR: 'char';
STRING: 'string';
VOID: 'void';

//OPERADORES
ASIGNACION: '=';
IGUALDAD: '==';
DISTINTO: '!=';
MAS: '+';
MENOS: '-';
SUMA_UNITARIA: '++';
RESTA_UNITARIA: '--';
MAYOR: '>';
MAYOR_IGUAL: '>=';
MENOR: '<';
MENOR_IGUAL: '<=';
ASTERISCO: '*';
BARRA: '/';
AND: '&&';
OR: '||';

// PALABRAS RESERVADAS
NEW: 'new';
RETURN: 'return';
BREAK: 'break';
CONTINUE: 'continue';
STATIC: 'static';

//BLOQUES
IF: 'if';
ELSE: 'else';
WHILE: 'while';
FOR: 'for';
SWITCH: 'switch';
DEFAULT: 'default';
DO: 'do';


NUMERO:
	DIGITO+
	| MENOS DIGITO+;
	
NUMERO_DECIMAL:
  DIGITO+ PUNTO DIGITO+
  | MENOS DIGITO+ PUNTO DIGITO+;


ID: (LETRA | GUION_BAJO) (LETRA | DIGITO | '_')*;


declaracion_variable:
  (STRING) ID ASIGNACION PYC //TODO: VER QUE ONDA CON EL CHAR
  // (STRING) ID ASIGNACION TEXTO+ PYC //TODO: VER QUE ONDA CON EL CHAR
  | (FLOAT | DOUBLE) ID ASIGNACION NUMERO_DECIMAL PYC
  | (FLOAT | DOUBLE | INT) ID ASIGNACION NUMERO PYC;

tipo:
  INT | FLOAT | STRING | CHAR | BOOLEAN; 

atributos:
  tipo ID;

declaracion_funcion:
  (tipo | VOID) ID PAR_ABRE ((atributos COMA) | atributos)* PAR_CIERRE bloque;

asignacion_variable:
  ID ASIGNACION (NUMERO_DECIMAL | NUMERO) |PYC
  // ID ASIGNACION ( TEXTO+ | NUMERO_DECIMAL | NUMERO) |PYC
  |ID ASIGNACION ( NUMERO_DECIMAL | NUMERO) (MAS | MENOS | ASTERISCO | BARRA) ( NUMERO_DECIMAL | NUMERO) PYC;

comentario:
  // BARRA{2} (TEXTO)+
  // BARRA BARRA (TEXTO)+
  BARRA BARRA

;

sentencia:
  declaracion_variable+
  | declaracion_funcion
  | asignacion_variable+
  | comentario+
  | operacion 
  | bloque_if_else+
;

return_func:
  RETURN (ID | NUMERO | NUMERO_DECIMAL) PYC;

bloque:
  LLAVE_ABRE sentencia* return_func LLAVE_CIERRE
  | LLAVE_ABRE sentencia* LLAVE_CIERRE
  ;

condicion:
  ID (MENOR | MENOR_IGUAL | MAYOR | MAYOR_IGUAL | IGUALDAD | DISTINTO) ID
  | (NUMERO | NUMERO_DECIMAL) (MENOR | MENOR_IGUAL | MAYOR | MAYOR_IGUAL | IGUALDAD | DISTINTO) ID
  | ID (MENOR | MENOR_IGUAL | MAYOR | MAYOR_IGUAL | IGUALDAD | DISTINTO) (NUMERO | NUMERO_DECIMAL)
  | (NUMERO | NUMERO_DECIMAL) (MENOR | MENOR_IGUAL | MAYOR | MAYOR_IGUAL | IGUALDAD | DISTINTO) (NUMERO | NUMERO_DECIMAL)
  | condicion AND condicion
  | condicion OR condicion
 ;

bloque_if:
  IF PAR_ABRE condicion PAR_CIERRE bloque;

bloque_if_else:
  bloque_if
  | bloque_if ELSE bloque
  // | bloque_if (ELSE bloque_if)*
  | bloque_if ELSE bloque_if
  | bloque_if ELSE bloque_if_else
  ;


operacion:
  ID SUMA_UNITARIA
  | ID RESTA_UNITARIA
  | ID (MAS | MENOS | ASTERISCO | BARRA) ID
  | ID (MAS | MENOS | ASTERISCO | BARRA) (NUMERO | NUMERO_DECIMAL)
;

bloque_for:
  FOR PAR_ABRE ((declaracion_variable | asignacion_variable) COMA*)+ PYC condicion PYC operacion PAR_CIERRE bloque
;

// TEXTO:
//   LETRA+
//   | DIGITO+
//   | WS+ LETRA+ WS+
//   | WS+ DIGITO+ WS+;