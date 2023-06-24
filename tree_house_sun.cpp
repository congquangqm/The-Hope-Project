// The Hope Project

#include <iostream>
#include <string>

using namespace std;

// Function Prototypes
void printQuote();
void printMission();
int calculateDonations(int, int);

// Main
int main()
{
	// Variables to store donors information 
	string name, country;
	int donationsAmount;

	// welocming
	cout << "Welcome to the Hope Project!" << endl;

	// Asking for user input
	cout << "What is your full name? ";
	getline(cin, name);
	cout << "\nWhere do you live? ";
	getline(cin, country);
	cout << "\nHow much would you like to donate? ";
	cin >> donationsAmount;

	// Printing quote
	printQuote();

	// Print mission
	printMission();

	// Calculating total donations
	int totalDonations = calculateDonations(donationsAmount, 1000);
	cout << "Thank you for your generous donation of $" << donationsAmount << " ";
	cout << "The total donations to the Hope Project are now $" << totalDonations << endl;

	return 0;
}

// print quote
void printQuote() 
{
	cout << "\"Remember not only to say the right thing in the right place, but far more difficult still, to leave unsaid the wrong thing at the tempting moment.\" - Benjamin Franklin" << endl;
}

// print mission
void printMission() 
{
	cout << "\nThe Hope Project is a charity dedicated to helping people living in poor and developing nations. We provide basic needs such as food, shelter, and healthcare to those who need it most." << endl;
}

// Calculating total donations
int calculateDonations(int donation, int existingDonations)
{
	return donation + existingDonations;
}