int x; //(1) 
int y;
void a() //(2) 
{ //(3) 
    int x;
    x = 1;  // x resolves to current scope, not x in global scope
    y = 2;  // y is not found in current scope, but resolves in global
    { int y = x; } //(4) 
}
void b(int z) //(5) 
{ } //(6) 
