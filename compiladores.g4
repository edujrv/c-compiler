grammar compiladores;

fragment LETRA : [A-Za-z];
fragment DIGITO : [0-9];

// NUMERO : DIGITO+ ;

// CARACTERES ESPECIALES
PUNTO: '.';
COMA: ',';
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
BOOLEAN: 'bool';
CHAR: 'char';
// STRING: 'string';
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
TRUE: 'true';
FALSE: 'false';

//BLOQUES
IF: 'if';
ELSE: 'else';
WHILE: 'while';
FOR: 'for';
SWITCH: 'switch';
DEFAULT: 'default';
DO: 'do';
CASE: 'case';

NUMERO: DIGITO+ | '-' DIGITO+;
NUMERO_DECIMAL: DIGITO+ PUNTO DIGITO+ | '-' DIGITO+ PUNTO DIGITO+;

// NUMERO: ('-')? DIGITO+;
// NUMERO_DECIMAL: ('-')? DIGITO+ PUNTO DIGITO+;

ID: (LETRA | GUION_BAJO) (LETRA | DIGITO | '_')*;

compiladores: prototipado_funcion* statement+ ;

statement:
  declaracion_variable PYC
  // | declaracion_funcion 
  | asignacion_variable PYC
  | COMENTARIO
  | operacion
  | bloques
  // | bloque_if
  // | bloque_if_else
  // | bloque_for
  // | bloque_while
  // | bloque_do_while
  // | bloque_switch
  // | prototipado_funcion
  ;
bloques:
  bloque_if
  | bloque_if_else
  | bloque_for
  | bloque_while
  | bloque_do_while
  | bloque_switch
  | declaracion_funcion
  ;

declaracion_variable:
  tipo ID ASIGNACION (TEXTO | NUMERO | NUMERO_DECIMAL | TRUE | FALSE | operacion+)
  | tipo ID
  ;


tipo:
  INT | FLOAT | CHAR | BOOLEAN;

atributos:
  tipo ID;

prototipado_funcion:
  // (tipo | VOID) ID PAR_ABRE lista_parametro? PAR_CIERRE PYC
  id_funcion PYC
  ;

// lista_parametro:
//   atributos (COMA atributos)*
//   ;
  
lista_parametro: 
	  tipo ID COMA lista_parametro
	| tipo ID lista_parametro
	| tipo COMA lista_parametro
	| tipo lista_parametro
	;	

id_funcion:
  (tipo | VOID) ID PAR_ABRE lista_parametro? PAR_CIERRE
;

declaracion_funcion:
// (tipo | VOID) ID PAR_ABRE lista_parametro? PAR_CIERRE bloque
  id_funcion bloque
  ;

asignacion_variable:
  ID ASIGNACION (TEXTO | NUMERO | NUMERO_DECIMAL)
  | ID ASIGNACION (NUMERO | NUMERO_DECIMAL | ID) (MAS | MENOS | ASTERISCO | BARRA) (NUMERO | NUMERO_DECIMAL | ID)
  ;

bloque:
  LLAVE_ABRE statement* return_func? LLAVE_CIERRE
  ;

return_func:
  RETURN (ID | NUMERO | NUMERO_DECIMAL | TRUE | FALSE) PYC
  | RETURN operacion PYC
  ;

condicion:
  ID (MENOR | MENOR_IGUAL | MAYOR | MAYOR_IGUAL | IGUALDAD | DISTINTO) ID
  | (NUMERO | NUMERO_DECIMAL) (MENOR | MENOR_IGUAL | MAYOR | MAYOR_IGUAL | IGUALDAD | DISTINTO) ID
  | ID (MENOR | MENOR_IGUAL | MAYOR | MAYOR_IGUAL | IGUALDAD | DISTINTO) (NUMERO | NUMERO_DECIMAL)
  | (NUMERO | NUMERO_DECIMAL) (MENOR | MENOR_IGUAL | MAYOR | MAYOR_IGUAL | IGUALDAD | DISTINTO) (NUMERO | NUMERO_DECIMAL)
  | condicion AND condicion
  | condicion OR condicion
  | TRUE
  | FALSE
  ;

bloque_if:
  IF PAR_ABRE condicion PAR_CIERRE bloque
  ;

bloque_if_else:
  bloque_if ELSE bloque
  | bloque_if ELSE bloque_if_else
  ;

bloque_operacional:
  PAR_ABRE operacion PAR_CIERRE
;
operacion:
  ID SUMA_UNITARIA
  | ID RESTA_UNITARIA
  // | ID ((MAS | MENOS | ASTERISCO | BARRA) ID)+
  | (NUMERO | NUMERO_DECIMAL | ID | bloque_operacional) ((MAS | MENOS | ASTERISCO | BARRA | PROCENTAJE) (NUMERO | NUMERO_DECIMAL | ID | bloque_operacional))+
  // | ID ((MAS | MENOS | ASTERISCO | BARRA) (NUMERO | NUMERO_DECIMAL | ID))+
  // | (NUMERO | NUMERO_DECIMAL) ((MAS | MENOS | ASTERISCO | BARRA) (NUMERO | NUMERO_DECIMAL))+
  // | bloque_operacional
  ;

bloque_for:
  FOR PAR_ABRE (declaracion_variable | asignacion_variable)? PYC condicion? PYC operacion? PAR_CIERRE bloque
  ;

bloque_while:
  WHILE PAR_ABRE condicion PAR_CIERRE bloque
  ;

bloque_do_while:
  DO bloque WHILE PAR_ABRE condicion PAR_CIERRE PYC
  ;

bloque_switch:
  SWITCH PAR_ABRE ID PAR_CIERRE LLAVE_ABRE (bloque_case | DEFAULT)+ LLAVE_CIERRE
  ;

bloque_case:
  CASE (NUMERO | '1') DOS_PUNTOS statement* (BREAK PYC)?
  | DEFAULT DOS_PUNTOS statement* (BREAK PYC)?
  ;

TEXTO:
  COMILLA_DOBLE (LETRA | DIGITO)* COMILLA_DOBLE
  | COMILLA_SIMPLE (LETRA | DIGITO)* COMILLA_SIMPLE
  ;

// NUMERO: ('-')? DIGITO+;
// NUMERO_DECIMAL: ('-')? DIGITO+ PUNTO DIGITO+;

COMENTARIO: '//' ~[\r\n]* -> skip;
