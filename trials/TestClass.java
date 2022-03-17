import java.io.*;
import java.util.*;

public class TestClass {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter wr = new PrintWriter(System.out);
        int T = Integer.parseInt(br.readLine().trim());
        for(int t_i = 0; t_i < T; t_i++)
        {
            int N = Integer.parseInt(br.readLine().trim());
            String[] arr_A = br.readLine().split(" ");
            int[] A = new int[N];
            for(int i_A = 0; i_A < arr_A.length; i_A++)
            {
                A[i_A] = Integer.parseInt(arr_A[i_A]);
            }
            String[] arr_B = br.readLine().split(" ");
            int[] B = new int[N];
            for(int i_B = 0; i_B < arr_B.length; i_B++)
            {
                B[i_B] = Integer.parseInt(arr_B[i_B]);
            }

            long out_ = solve(N, A, B);
            System.out.println(out_);
            
         }

         wr.close();
         br.close();
    }
    class Node{
        Node left ;
        Node.right;
        int v:
        Node(int v){
            this.v=v
        }
    }
    void assignNode(Node p,  Node c){
        if(p.v>c.v){
            if(p.left==null){
                p.left=c;
            }else{
                assignNode(p.left,c);
            }
        }else{
            if(p.right==null){
                p.right=c;
            }else{
                assignNode(p.right,c);
            }
        }
    }
    static Node createTree(int[] a, N){
        Node r=new Node(a[0])
        i=1
        while(true){
            Node n = new Node(a[i])
            assignNode(r,n)
            i++
        }
        return r;
    }
    xcv(int v, Node a){
        if(a.v>v){
            if(a.left !=null){
                xcv(v, a.left);
            }else{

            }
        }    
    }
    static long solve(int N, int[] A, int[] B){
        Node a=createTree(A,N);
        Node b=createTree(B,n):
        
       /*
       N : size of A & B
       A : First Array
       B : Second Array
       */

       
        long result = 0;

        return result;
    
    }
}

