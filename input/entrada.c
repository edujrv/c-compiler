int funcion();
void funcion2(int a);
int suma(int a, int b);

int main() {
    int i;

    for (i = 3; i <= 5; i++) {
        int x = 0;
    }


    int option = 2;
    int a;
    switch (option) {
        case 0:
            a = 0;
            break;
        case 2:
            a = 2;
        case 3:
            a = 3;
            break;
        default:
            a = 4;
    }

    int num = 7;
    if (num > 0) {
        int jaja = num + i;
    }

    int age = 18;
    if (age >= 18) {
        int r = 3 + 5 / 10 + 32;
    } else if (age >= 8) {
        int r = 6 + 5 / 10 - 32;
    }else{
        int r = 6 + 5 / 10;
    }
    return 0;
}

int suma(int a, int b){
  return a + b;
}
