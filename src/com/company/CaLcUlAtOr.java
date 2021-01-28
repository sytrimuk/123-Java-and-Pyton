package com.company;

import java.util.Scanner;

public class CaLcUlAtOr

{
    private static byte B;
    private static double f_1;
    private static double f_2;
    private static double f_3;
    private static double k;
    private static double f;
    private static byte C;
    private static byte A;
    private static byte D;

    public static void main(String[] args) {

        /* //не знаю зачем)) */
    char s, x, e, i, p, w;
        s = '+';
        e = '-';
        i = '*';
        p = '/';
        w = '%';        
        x = '=';

        Scanner num_1 = new Scanner(System.in);
        //byte A, D;

        Scanner num_2 = new Scanner(System.in);
        //double f_2;

        // выбор чисел 1 и 2
        System.out.print("F_1 = ");
        f_1 = num_2.nextDouble();
        System.out.print("F_2 = ");
        f_2 = num_2.nextDouble();

        // будет 2 или 3 числа
        // если 0 - два числа
        // если 1 - три числа
        // и чему будет равно 3 число(если оно есть)
        System.out.print("\n--Сколько будет чисел 2 или 3\n--если 0 - два числа\n--если 1 - три числа и чему будет равно 3 число\nB = ");
        B = num_1.nextByte();
        System.out.print("You choosed(B): " + B + "\n");
        if(B == 0){
            f_3 = 0;
        }
        else{
            System.out.print("\nF_3 = ");
            f_3 = num_2.nextFloat();
        }

        System.out.print("\nYou have a choice of what A equals:\n1(+), 2(-), 3(*), 4(/), 5(%)\n");

        // какое будет 1 действие
        System.out.print("A = ");
        A = num_1.nextByte();
        System.out.print("You choosed(A): " + A + "\n");
        switch (A) {
            case 1:
                f = f_1 + f_2;
                //System.out.print(f_1 + s + f_2 + x + f);
                break;

            case 2:
                f = f_1 - f_2;
                //System.out.print(f_1 + e + f_2 + x + f);
                break;

            case 3:
                f = f_1 * f_2;
                //System.out.print(f_1 + i + f_2 + x + f);
                break;

            case 4:
                f = f_1 / f_2;
                //System.out.print(f_1 + p + f_2 + x + f);
                break;

            case 5:
                f = f_1 % f_2;
                //System.out.print(f_1 + w + f_2 + x + f);
                break;
        }

        
        // какое будет 2 действие(если оно есть)
        byte С;
        switch(B){
            case 0:
                System.out.print("\nУ вас нет второг действия\n");
            break;

            case 1:
                System.out.print("\nFirst action value = " + f + "\n");
//               System.out.print("\nкакое будет 2 действие(если первое в скобках)\n0(=), 1(+), 2(-), 3(*), 4(/)\nкакое будет 2 действие(если первое не в скобках)\n5(+), 6(-), 7(*), 8(/)");
                System.out.print("С = ");
                С = num_1.nextByte();
                System.out.print("You choosed(D): " + С + "\n");
                switch(C){
                    case 1:
                        System.out.print("\nкакое будет 2 действие(первое в скобках)\n0(=), 1(+), 2(-), 3(*), 4(/)\n");
                        System.out.print("D = ");
                        D = num_1.nextByte();
                        System.out.print("You choosed(D): " + D + "\n");
                        switch (D) {
                            case 0:
                                k = f;
                            break;

                            case 1:
                                k = f + f_3;
                            break;

                            case 2:
                                k = f - f_2;
                            break;

                            case 3:
                             k = f * f_3;
                            break;

                            case 4:
                                k = f / f_3;
                            break;
                        }

                    case 2:
                    System.out.print("\nкакое будет 2 действие(первое не в скобках)\n0(=), 1(+), 2(-), 3(*), 4(/)\n");
                        switch(D) {
                            case 0:
                                k = f;
                            break;

                            case 1:
                                k = f + f_3;
                            break;

                            case 2:
                                k = f - f_2;
                            break;

                            case 3:
                             k = f * f_3;
                            break;

                            case 4:
                                k = f / f_3;
                            break;
                        }
                    break;
                }

        }

        // если одно действие - 0
        // если два то - 1
        switch (B) {
            case 0:
                System.out.print("\nResult = " + f);
                break;

            case 1:
                System.out.print("\nResult = " + k);
                break;
        }
    }

}

// ниже МУСОР(да-да мусор)))
/*                 if (D == 0){
                    k = f;
                }

                else if(D == 1){
                    k = f + f_3;
                }

                else if (D == 2){
                    k = f - f_2;
                }

                else if (D == 3){
                    k = f * f_3;
                }

                else{
                    k = f / f_3;
                } */
//C,

/*
private static char s;
private static char x;
private static char e;
private static char i;
private static char p;
private static char w;
*/

/*         switch (B) {
            case 0:
                f_3 = 0;
                break;

            case 1:
                System.out.print("\nF_3 = ");
                f_3 = num_2.nextFloat();
        } */
