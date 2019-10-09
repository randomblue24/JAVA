package application;
	
import javafx.application.Application;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.Slider;
import javafx.scene.control.TextField;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;


public class MortCalc extends Application {
	//@Override
	/*
	Label purchasepricelabel;
	Label downpaymentlabel, interestlabel, sliderlabel;
	TextField purchasepricetextfield, downpaymenttextfield, interesttextfield, loanamounttextfield, monthlypaymenttextfield;
	Slider durationslider;
	HBox horbox1, horbox2, horbox3;
	
	int price, downpayment;

	double interest;
	
	public int monthlypayment(int y){
		//N P R derived from formula
		int N;
		N=y*12;

		int P;
		P=price - downpayment;

		double R;
		R=interest/12/100;

		double payment;
		payment= (P*R*Math.pow((1+R),N))/(Math.pow((1+R),(N))-1);

		return (int)payment;
	} 
	*/

	
	Label purchasepricelabel, loanamountlabel, monthlypaymentlabel10, monthlypaymentlabel20, monthlypaymentlabel30;
	Label downpaymentlabel, interestlabel, sliderlabel, monthlypaymentlabel;
	TextField purchasepricetextfield, downpaymenttextfield, interesttextfield, loanamounttextfield;
	Slider durationslider;
	HBox horbox1, horbox2, horbox3;
	
	int price, downpayment;

	double interest;
	
	public int monthlypayment(int y){
		//N P R derived from formula
		int N;
		N=y*12;

		int P;
		P=price - downpayment;

		double R;
		R=interest/12/100;

		double payment;
		payment= (P*R*Math.pow((1+R),N))/(Math.pow((1+R),(N))-1);

		return (int)payment;
	} 
	public void start(Stage primaryStage) {

try {
	

	primaryStage.setTitle("Mortgage Calculator");
	BorderPane root = new BorderPane();
	Scene scene = new Scene(root,400,400);
	scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
	primaryStage.setScene(scene);
	primaryStage.show();
	
	
	primaryStage.setTitle("Mortgage Calculator: Abusaleh Masud");

	//We're creating the label and textfield objects
	purchasepricelabel = new Label("Purchase Price: ");
	purchasepricetextfield=new TextField();
	//Hbox is just horizontal box. It arranges specified objects horizontally.
	horbox1=new HBox(purchasepricelabel, purchasepricetextfield);
	
	downpaymentlabel=new Label("Down Payment: ");
	downpaymenttextfield=new TextField();
	horbox2=new HBox(downpaymentlabel, downpaymenttextfield);
	
	interestlabel=new Label("Interest Rate: ");
	interesttextfield=new TextField();
	horbox3=new HBox(interestlabel, interesttextfield);
	
	loanamountlabel= new Label("Loan Amount: ");

	monthlypaymentlabel= new Label("Monthly Payment: ");
	monthlypaymentlabel10=new Label("Monthly Payment 10 years: ");
	monthlypaymentlabel20=new Label("Monthly Payment 20 years: ");
	monthlypaymentlabel30=new Label("Monthly Payment 30 years: ");
	HBox horbox4=new HBox(monthlypaymentlabel10, monthlypaymentlabel20, monthlypaymentlabel30);
	
	durationslider=new Slider();
	durationslider.setMin(10);
	durationslider.setMax(100);
	durationslider.setValue(10);
	durationslider.setShowTickLabels(true);
	durationslider.setMajorTickUnit(10);
	durationslider.setMinorTickCount(9);
	durationslider.valueProperty().addListener((obs, oldval, newVal) ->
	durationslider.setValue(newVal.intValue()));
	Button calculatebutton=new Button("Calculate");
	
	calculatebutton.setOnAction(value -> { onButtonClick(); });
	
	//VBox verticalbox = new VBox(horbox1,horbox2,horbox3,purchasepricetextfield,durationslider,calculatebutton,loanamountlabel, monthlypaymentlabel); 
	VBox verticalbox = new VBox(horbox1,horbox2,horbox3,horbox4, durationslider,calculatebutton,loanamountlabel, monthlypaymentlabel, monthlypaymentlabel10,monthlypaymentlabel20,monthlypaymentlabel30); 

	Scene scene1 = new Scene(verticalbox, 500, 300);

	primaryStage.setScene(scene1);

	primaryStage.show();
	
} catch(Exception e) { 
	e.printStackTrace();
}
	}
	
	public void onButtonClick() {
		price= Integer.parseInt(purchasepricetextfield.getText());
		downpayment = Integer.parseInt(downpaymenttextfield.getText());

		interest = Double.parseDouble(interesttextfield.getText());

		int years = (int)durationslider.getValue();
		int monthpayment = monthlypayment(years);
		int monthpayment1 = monthlypayment(10);
		int monthpayment2 = monthlypayment(20);
		int monthpayment3 = monthlypayment(30);

		monthlypaymentlabel.setText("Monthly payment: " + monthpayment);
		loanamountlabel.setText("Loan Amount: "+ (price-downpayment));
		monthlypaymentlabel10.setText("Monthly payment 10 years: "+monthpayment1 );
		monthlypaymentlabel20.setText("Monthly payment 10 years: "+ monthpayment2);
		monthlypaymentlabel30.setText("Monthly payment 10 years: "+ monthpayment3 );

		
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}
