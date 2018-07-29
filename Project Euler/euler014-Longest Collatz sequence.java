import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner in = new Scanner(System.in);
        List<Integer> solutions = getMajors((long) 5000000);
        int tests = in.nextInt();
        for(int i = 0; i<tests; i++){
            int n = in.nextInt();
            System.out.println(solutions.get(n-1));
        }
    }
    
    static List<Integer> getMajors(long n){
        List<Integer> solutions = new ArrayList<Integer>();
        List<Integer> majors = new ArrayList<Integer>();
        int major = 0; 
        int candidate = 1;
        for(int i = 1; i<=n; i++){
            cont = 0;
            getSequence(i,majors);
            majors.add(cont);
            if(cont>=major){
                candidate = i;
                major = cont;
            }
            solutions.add(candidate);
        }
        return solutions;
    }
    
    public static int cont = 0;
    static void getSequence(long n, List<Integer> solutions){       
        if(n!=1){
            if(solutions.size()>=n){
                cont += solutions.get((int) n-1);
            }else{
                if(n%2==0){
                    cont++;
                    getSequence(n/2,solutions);
                 }else{
                    cont++;
                    getSequence((3*n)+1,solutions);
                 }
            }        
        }
    }
    
}