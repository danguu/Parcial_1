%{
#include "calc.tab.h"
%}

%%
[0-9]+(\.[0-9]+)?   { yylval.f = atof(yytext); return NUM; }
"sqrt"              { return SQRT; }
[ \t\n]             ;
.                   ;
%%

