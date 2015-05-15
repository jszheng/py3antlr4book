int f(int x, float y) {
    g();   // forward reference is ok
    i = 3; // no declaration for i (error)
    g = 4; // g is not variable (error)
    return x + y; // x, y are defined, so no problem
}

void g() {
    int x = 0;
    float y;
    y = 9; // y is defined
    f();   // backward reference is ok
    z();   // no such function (error)
    y();   // y is not function (error)
    x = f; // f is not a variable (error)
}
