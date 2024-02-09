// Ex. x=3, m=7, modular inverse of x mod m is 5, since (3*5) mod 7=1

int main() {
    int x, m;
    scanf (" %d %d", &x, &m);
    for (int i=1; n<m; n++) {
        if ((x*n)%m == 1) {
            printf("%d\n", n);
            return 0;
        }
    }
    printf("No such integer exists.");
    return 0;
}