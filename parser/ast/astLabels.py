#!/usr/bin/python

#AST_TOKENS
AST_ROOT = 'ROOT';                                    #New scope
AST_PROT_OBJ_NAME = 'PROT_OBJ_NAME';                  #INTERMEDIATE
AST_ENDPOINT_ALIAS_SECTION = 'ALIAS_SECTION';         
#traces
AST_TRACE_SECTION = 'TRACE_SECTION';
AST_TRACE_BODY_SECTION = 'TRACE_BODY_SECTION';        #INTERMEDIATE
AST_TRACE_ITEM = 'TRACE_ITEM';
AST_TRACE_LINE = 'TRACE_LINE';

#shared
AST_SHARED_SECTION = 'SHARED_SECTION';                #New scope
AST_SHARED_BODY_SECTION = 'SHARED_BODY_SECTION';      #INTERMEDIATE
AST_ANNOTATED_DECLARATION = 'ANNOTATED_DECLARATION';

#endpoint
AST_ENDPOINT = 'ENDPOINT';
AST_ENDPOINT_BODY_SECTION = 'ENDPOINT_BODY_SECTION';
AST_ENDPOINT_GLOBAL_SECTION = 'ENDPOINT_GLOBAL_SECTION';
AST_ENDPOINT_FUNCTION_SECTION = 'ENDPOINT_FUNCTION_SECTION'; #New scope...names get added to scope before bodies.


#functions
##function types
AST_PUBLIC_FUNCTION = 'PUBLIC_FUNCTION';
AST_FUNCTION = 'FUNCTION';
AST_MSG_SEND_FUNCTION = 'MSG_SEND_FUNCTION';
AST_MSG_RECEIVE_FUNCTION = 'MSG_RECEIVE_FUNCTION';

AST_ONCREATE_FUNCTION = 'ONCREATE_FUNCTION';


##function helpers
AST_FUNCTION_BODY = 'FUNCTION_BODY'; #provides new scope
AST_FUNCTION_DECL_ARGLIST = 'FUNCTION_DECL_ARGLIST';
AST_FUNCTION_DECL_ARG = 'FUNCTION_DECL_ARG';
AST_FUNCTION_ARGLIST = 'FUNCTION_ARGLIST';
AST_FUNCTION_BODY_STATEMENT = 'FUNCTION_BODY_STATEMENT';



##conditional expressions
AST_CONDITION_STATEMENT = 'CONDITION_STATEMENT';
AST_IF_STATEMENT = 'IF_STATEMENT';
AST_ELSE_IF_STATEMENTS = 'ELSE_IF_STATEMENTS';
AST_ELSE_IF_STATEMENT = 'ELSE_IF_STATEMENT';
AST_ELSE_STATEMENT = 'ELSE_STATEMENT';
AST_SINGLE_OR_MULTILINE_CURLIED_BLOCK = 'SINGLE_OR_MULTILINE_BLOCK';
AST_BOOLEAN_CONDITION = 'BOOLEAN_CONDITION';
AST_NOT_EXPRESSION = 'NOT_EXPRESSION';

AST_PRINT = 'PRINT';
AST_BRACKET_STATEMENT = 'BRACKET';

##boolean expressions
AST_AND = 'AND';
AST_OR  = 'OR';
AST_BOOL_EQUALS = '==';
AST_BOOL_NOT_EQUALS = '!=';
AST_GREATER_THAN = '>';
AST_GREATER_THAN_EQ = '>='
AST_LESS_THAN = '<';
AST_LESS_THAN_EQ = '<='

##arithmetic
AST_PLUS = '+';
AST_MINUS = '-';
AST_MULTIPLY = '*';
AST_DIVIDE = '/';

AST_FUNCTION_CALL = 'FUNCTION_CALL';
AST_ASSIGNMENT_STATEMENT = 'ASSIGNMENT_STATEMENT';
AST_DECLARATION = 'DECLARATION';
AST_STRING = 'STRING_LITERAL';
AST_NUMBER = 'NUMBER_LITERAL';
AST_BOOL = 'BOOL_LITERAL';
AST_TYPE = 'TYPE';
AST_IDENTIFIER = 'IDENTIFIER';
AST_EMPTY = 'EMPTY';

AST_SEND_STATEMENT = 'SEND_STATEMENT';
AST_MESSAGE_LITERAL = 'MESSAGE_LITERAL';
AST_MESSAGE_LITERAL_ELEMENT = 'MESSAGE_LITERAL_ELEMENT';
AST_TYPED_SENDS_LINE = 'TYPED_SENDS_LINE';
AST_TYPED_SENDS_STATEMENT = 'TYPED_SENDS_STATEMENT';

AST_RETURN_STATEMENT = 'RETURN_STATEMENT';


TYPE_BOOL = 'TrueFalse';
TYPE_NUMBER = 'Number';
TYPE_STRING = 'Text';
TYPE_NOTHING = 'Nothing';
TYPE_OUTGOING_MESSAGE = 'OutgoingMessage';
TYPE_INCOMING_MESSAGE = 'IncomingMessage';
TYPE_MESSAGE_LITERAL = 'MessageLiteral';

TYPE_MSG_SEND_FUNCTION = 'MsgSendFunc';
TYPE_MSG_RECEIVE_FUNCTION = 'MsgRecvFunc';

