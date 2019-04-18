import java.util.Scanner;

public class CheckProtection {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		char check[]=new char[9];
		
		
		Scanner input=new Scanner(System.in);
		

		System.out.println("Enter the check amount: ");

		String inp=input.nextLine();
		
		
		/*
		//Converted the user input into string
		String inp1=Integer.toString(inp);
		*/
		
		//COnvertin String into an array;
		char[] inputToArray=inp.toCharArray();
	

		//Problem: If the converted array isn't 8 characters long, it won't work. 
		//5 character long array, and our 8 character long array. There is no A.
		//We want to go through the new char array and transfer the chars to a new 8 character array and then do the loop.
		
		//CAalculates the free spaces
		int calculate=9-inputToArray.length;
		
		char newArray[]=new char[9];
		int l=0;
		while(l<inputToArray.length) {
			newArray[l]=inputToArray[l];
			l++;
		}
		
		
		int m=newArray.length; 
		int n=inputToArray.length-1;
		
		while(n>=0) {
			for(int a=check.length-1; a>=0; a--) {
				check[a]=newArray[n];
				--n;
				if(n==-1) {
					break;
				}
			}
		}
		
		
		/*
		 * 		//Remember, an array can store 8 things, but index goes up to 7

		for(int i=inputToArray.length-1; i>=0; i--) {
			for(int a=check.length-1; a>=0; a--) {
				check[a]=inputToArray[i];
			}
		}
		*/
		
		//What I'm trying to do is check how many indexes haven't been filled.
		//How? x holds how long the array is. ANd we're entering chars into new array through the end.
		//Just take the x value and start from i=0 to x-1, and you have the places where there are no numbers
		int x=9-inputToArray.length;
		
		
		for(int i=0; i<x;i++) {
			check[i]='*';
		}
		
		System.out.print(check);
		
	}

}
