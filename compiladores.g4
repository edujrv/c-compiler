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

// NUMERO: DIGITO+ | '-' DIGITO+;
// NUMERO_DECIMAL: DIGITO+ PUNTO DIGITO+ | '-' DIGITO+ PUNTO DIGITO+;

NUMERO: 
  DIGITO+
  | MENOS DIGITO+
  | DIGITO+ PUNTO DIGITO+
  | MENOS DIGITO+ PUNTO DIGITO+
;
// NUMERO_DECIMAL: ('-')? DIGITO+ PUNTO DIGITO+;

ID: (LETRA | GUION_BAJO) (LETRA | DIGITO | '_')*;

programa: instrucciones EOF;

// compiladores: prototipado_funcion* instruccion+ ;

instrucciones: instruccion instrucciones |;

instruccion:
  declaracion_variable PYC
  | asignacion_variable PYC
  | COMENTARIO
  | operacion PYC
  | prototipado_funcion
  | bloques
  ;

bloques:
  bloque_if
  | declaracion_funcion 
  | bloque_if_else
  | bloque_for
  | bloque_while
  | bloque_do_while
  | bloque_switch
  // | bloque
;

declaracion_variable:
  tipo ID ASIGNACION (TEXTO | NUMERO | TRUE | FALSE | operacion)
  // tipo ID ASIGNACION (NUMERO | TRUE | FALSE | operacion)
  | tipo ID
  ;


tipo:
  INT | FLOAT | CHAR | BOOLEAN;

argumento:
  tipo ID;

prototipado_funcion:
  cabecera_funcion PYC
  ;

lista_argumento:
  argumento
  | argumento COMA lista_argumento
  ;

cabecera_funcion:
  (tipo | VOID) ID PAR_ABRE (lista_argumento | ) PAR_CIERRE;
  
declaracion_funcion:
  cabecera_funcion bloque
  ;

argumentos:
  ID
  | ID COMA argumentos
  | NUMERO COMA argumento 
  | NUMERO
  |
;

llamada_funcion:
  ID PAR_ABRE argumentos PAR_CIERRE PYC
  | ID ASIGNACION PAR_ABRE argumentos PAR_CIERRE PYC

;

asignacion_variable:
  // ID ASIGNACION (NUMERO )
  ID ASIGNACION (NUMERO | TEXTO)
  // | ID ASIGNACION (NUMERO | ID) (MAS | MENOS | ASTERISCO | BARRA) (NUMERO | ID)
  | ID ASIGNACION operacion
  ;

bloque:
  LLAVE_ABRE instrucciones return_func LLAVE_CIERRE
  | LLAVE_ABRE instrucciones  LLAVE_CIERRE
  ;

return_func:
  RETURN (ID | NUMERO | TRUE | FALSE) PYC
  | RETURN operacion PYC
  | RETURN PYC
  ;

condicion:
  ID (MENOR | MENOR_IGUAL | MAYOR | MAYOR_IGUAL | IGUALDAD | DISTINTO ) ID
  | NUMERO (MENOR | MENOR_IGUAL | MAYOR | MAYOR_IGUAL | IGUALDAD | DISTINTO) ID
  | ID (MENOR | MENOR_IGUAL | MAYOR | MAYOR_IGUAL | IGUALDAD | DISTINTO) NUMERO
  | NUMERO (MENOR | MENOR_IGUAL | MAYOR | MAYOR_IGUAL | IGUALDAD | DISTINTO) NUMERO
  | condicion AND condicion
  | condicion OR condicion
  | TRUE
  | FALSE
  | ID
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
  | (NUMERO | ID | bloque_operacional) ((MAS | MENOS | ASTERISCO | BARRA | PROCENTAJE) (NUMERO | ID | bloque_operacional))+
  // | ID ((MAS | MENOS | ASTERISCO | BARRA) (NUMERO | NUMERO_DECIMAL | ID))+
  // | (NUMERO | NUMERO_DECIMAL) ((MAS | MENOS | ASTERISCO | BARRA) (NUMERO | NUMERO_DECIMAL))+
  // | bloque_operacional
  ;

bloque_for:
  FOR PAR_ABRE (declaracion_variable | asignacion_variable)? PYC condicion? PYC operacion? PAR_CIERRE bloque
  | FOR PAR_ABRE (declaracion_variable | asignacion_variable) (COMA (declaracion_variable | asignacion_variable))* PYC 
                  condicion (COMA condicion)* PYC 
                  operacion (COMA operacion)* PAR_CIERRE bloque
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
  CASE NUMERO DOS_PUNTOS instruccion* (BREAK PYC)?
  | DEFAULT DOS_PUNTOS instruccion* (BREAK PYC)?
  ;

TEXTO:
  COMILLA_DOBLE (LETRA | DIGITO)* COMILLA_DOBLE
  | COMILLA_SIMPLE (LETRA | DIGITO)* COMILLA_SIMPLE
  ;

COMENTARIO: '//' ~[\r\n]* -> skip;