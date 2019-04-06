import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.Random;
import java.util.Scanner;


public class generator
{

    public static void main(String[] args)
    {
        ArrayList <String> adj=new ArrayList(10);
        ArrayList <String> noun=new ArrayList(10);

        adj.add("Cool ");
        adj.add("Well-Formed ");
        adj.add("Smooth ");
        adj.add("Benevolent ");
        adj.add("Nice");
        adj.add("GLORIOUS");
        adj.add("Illuminating ");
        adj.add("Interesting ");
        adj.add("Entertaining");
        adj.add("Enticing");
        adj.add("Charming");

        noun.add("Pineapple ");
        noun.add("Human ");
        noun.add("Meatball ");
        noun.add("Shirt ");
        noun.add("Teeth");
        noun.add("piñata ");
        noun.add("hair ");
        noun.add("Face ");
        noun.add("samosa ");
        noun.add(" ");
        noun.add("Series of tubes ");
        noun.add("Horse ");

        String[] items;
        items=new String[2];

        generator obj = new generator();
        generator obj2 = new generator();


        Scanner inp=new Scanner(System.in);

        System.out.println("Welcome to the Compliment GENERATOR! Press 1 to enter a new compliment or 2 to receive an compliment:  ");

        int n0=inp.nextInt();

        if(n0==1){
            obj2.complimentAdder(adj, noun, n);

        }

        /*
        System.out.println("Enter how many times you wish to be complimented: ");
        int n=inp.nextInt();
        */

        obj.getCompliment(adj,noun);
    }

    public void complimentAdder(ArrayList <String> noun, ArrayList<String> adj, int n)
    {
        String[] items;
        items=new String[2];

        Scanner inp=new Scanner(System.in);

        System.out.print("Do you want to add compliments to the GLORIOUS Generator?: Enter a yes or no ");
        String x=inp.nextLine().toLowerCase();

        if(x=="y"||x=="yes"){
            System.out.println("Enter a 2 word compliment: ");
            x=inp.nextLine();
            items = x.split(" ");
            adj.add(items[0]);
            noun.add(items[1]);
        }
        //array to store split string;
    }


    public void getCompliment(ArrayList<String> x1, ArrayList <String> x2) {
        Scanner inp=new Scanner(System.in);
        System.out.println("How many times do you wish to be humored? ");

        int n=inp.nextInt();

        Random rand = new Random();
        int int1 = rand.nextInt(x1.size());
        int int2 = rand.nextInt(x2.size());

        int x = 0;

        while (x != n) {
            int1 = rand.nextInt(x1.size());
            int2 = rand.nextInt(x2.size());
            System.out.println(x1.get(int1).toUpperCase() + x2.get(int2).toUpperCase()+"!");
            x++;
        }
    }

}


