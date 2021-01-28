package com.company;

import java.util.Scanner;

{
    public static void main(String[] args) {
        Scanner num = new Scanner (System.in);
        float f_1, f_2, TRA;
        
//        f_2 = 12
        
        System.out.print("F_1:");
        f_1 = num.nextFloat();
        
        System.out.print("F_2:");
        f_2 = num.nextFloat();
        
        TRA = f_1 + f_2;
        System.out.print("Result =" + TRA);
    }
}
