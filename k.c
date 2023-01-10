#include <stdio.h>
#include <math.h>
int main()
{
    int a[10], i, j, temp, n;
    printf("Enter size: ");
    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }
    for (i = 0; i < pow(2, n); i++)
    {
        temp = i;
        printf("{");
        for (j = 0; j < n; j++)
        {
            if (temp % 2 == 1)
            {
                printf("%d", a[j]);
            }
            temp = temp / 2;
        }
        printf("}\t");
    }
    return 0;
}