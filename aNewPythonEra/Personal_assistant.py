## PERSONAL ASSISTANT CONSOLE APP....

import random   #Used to randomly pick a motivational quote.
import datetime 

quotes=[
    "Keep going, you're doing great!",
    "Stay positive and work hard.",
    "Success is a journey, not a destination.",
    "Believe in yourself!",
    "Every day is a second chance."
]


def greeet_user():
    name =print(input("👋 Hello! What's your name?"))
    print(f"Welcome ,{name} ! I am your personal assistant ")
    return name
def show_quote():
    print("💡 Quote of the Day:")
    print(random.choice(quotes))
    
def show_dateNtime():
    now = datetime.datetime.now()
    print("📅 Current Date and Time:", now.strftime("%d-%m-%y:%H-%M-%S"))
    
def take_note():
    try:
        note = input("📝 Write your note: ")
        with open("notes.txt" ,"a") as file:
            file.write(note+"\n")
        print("✅ Note saved successfully!")
    except Exception as e:
         print("⚠️ Error saving note:", e)

def read_notes():
    try:
        with open("notes.txt","r") as file:
            if content.strip():
                print("📓 Your Notes:\n" + content)
            else:
                print("No notes yet")
    except FileNotFoundError:
        print("⚠️ No notes file found.")
        
        
        
        
        
        
        
        
        quotes = [
    "Believe you can and you're halfway there.",
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "Don't watch the clock; do what it does. Keep going."
]
def show_date_time():
    now = datetime.datetime.now()
    print("📅 Current Date and Time:", now.strftime("%Y-%m-%d %H:%M:%S"))
def show_quote():
    print("💡 Quote of the Day:")  # Step 1: Print a header
    print(random.choice(quotes))   # Step 2: Print a random quote
def take_note():
    try:
        note = input("📝 Write your note: ")
        with open("notes.txt", "a") as file:
            file.write(note + "\n")
        print("✅ Note saved successfully!")
    except Exception as e:
        print("⚠️ Error saving note:", e)
def read_notes():
    try:
        with open("notes.txt", "r") as file:
            content = file.read()
            if content.strip():
                print("📓 Your Notes:\n" + content)
            else:
                print("🗒️ No notes yet.")
    except FileNotFoundError:
        print("⚠️ No notes file found.")


public static boolean isPrime(int n) {
    if (n <= 1) return false;
    for (int i = 2; i <= Math.sqrt(n); i++) {
        if (n % i == 0) return false;
    }
    return true;
}
public static boolean isPrime(int n) {
    if (n <= 1) return false;
    for (int i = 2; i <= Math.sqrt(n); i++) {
        if (n % i == 0) return false;
    }
    return true;
}
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, world!");
    }
}
public static int factorial(int n) {
    return (n <= 1) ? 1 : n * factorial(n - 1);
}
public static String reverse(String str) {
    return new StringBuilder(str).reverse().toString();
}
public static boolean isPalindrome(String str) {
    int i = 0, j = str.length() - 1;
    while (i < j) {
        if (str.charAt(i++) != str.charAt(j--)) return false;
    }
    return true;
}
public static void bubbleSort(int[] arr) {
    for (int i = 0; i < arr.length - 1; i++) {
        for (int j = 0; j < arr.length - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}
public static void printFibonacci(int n) {
    int a = 0, b = 1;
    for (int i = 0; i < n; i++) {
        System.out.print(a + " ");
        int temp = a + b;
        a = b;
        b = temp;
    }
}
import java.util.Scanner;

Scanner scanner = new Scanner(System.in);
System.out.print("Enter your name: ");
String name = scanner.nextLine();
System.out.println("Hello, " + name);
public static int largest(int a, int b, int c) {
    return Math.max(a, Math.max(b, c));
}







