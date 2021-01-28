package com.company;

import java.util.Scanner;
 
public class KvadratnoeUravnenie {
 
    public static void main(String[] args)
    {

        byte a, b, c;
        long D;

        System.out.println("Программа решает квадратное уравнение вида:");
        System.out.println("ax^2 + bx + c = 0");
        System.out.println("Введите a, b и c:");

        //Чему роно "a" 
        Scanner PIT = new Scanner(System.in);
        System.out.println("a = ");
        a = (byte) PIT.nextDouble();

        //Чему роно "b"
        Scanner PIU = new Scanner(System.in);
        System.out.println("b = ");
        b = (byte) PIU.nextDouble();

        //Чему роно "c"
        Scanner PIO = new Scanner(System.in);
        System.out.println("c = ");
        c = (byte) PIO.nextDouble();

        D = b ^(2) - 4 * a * c;
        if (D > 0) {
            double x1, x2;
            x1 = (-b - Math.sqrt(D)) / (2 * a);
            x2 = (-b + Math.sqrt(D)) / (2 * a);
            System.out.println("Корни уравнения: x1 = " + x1 + ", x2 = " + x2);
        }
        else if (D == 0) {
            double x;
            x = -b / (2 * a);
            System.out.println("Уравнение имеет единственный корень: x = " + x);
        }
        else {
            System.out.println("Уравнение не имеет действительных корней!");
        }
    }
}