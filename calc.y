%{
#include <stdio.h>
#include <math.h>
%}

%union { double f; }
%token <f> NUM
%token SQRT
%type <f> expr

%%
input : expr { printf("Resultado = %f\n", $1); }
      ;

expr  : SQRT '(' expr ')' { $$ = sqrt($3); }
      | NUM              { $$ = $1; }
      ;
%%

int main() { return yyparse(); }
int yyerror(char *s) { printf("Error: %s\n", s); return 0; }

