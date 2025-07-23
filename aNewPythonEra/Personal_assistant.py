## PERSONAL ASSISTANT CONSOLE APP....

import random   #Used to randomly pick a motivational quote.
import datetime 
import os

quotes=[
    "Keep going, you're doing great!",
    "Stay positive and work hard.",
    "Success is a journey, not a destination.",
    "Believe in yourself!",
    "Every day is a second chance."
]


def greet_user():
    name =input("👋 Hello! What's your name?")
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
            content = file.read()
            if content.strip():
                print("📓 Your Notes:\n" + content)
            else:
                print("No notes yet")
    except FileNotFoundError:
        print("⚠️ No notes file found.")

def delete_saved_file():
    import os
    try:
        if os.path.exists("notes.txt"):
           os.remove("notes.txt")
           print("🗑️ Notes file deleted successfully.")
        else:
            print("⚠️ No notes file to delete.")
    except Exception as e:
        print("⚠️ Error deleting notes:", e)
        
def show_menu():
    print("\n📌 What would you like to do?")
    print("1. Get a motivational quote")
    print("2. View current date and time")
    print("3. Write a note")
    print("4. Read saved notes")
    print("5. Deleting the Saved file")
    print("6. Exit")
    
user = greet_user()
print(f"Welcome ,{user} ! I am your personal assistant")
while True:
    show_menu()
    choice= input("enter your choice from (1 to 5):-> ")
    
    if choice =="1":
        show_quote()
    elif choice == "2":
        show_dateNtime()
    elif choice == "3":
        take_note()
    elif choice == "4":
        read_notes()
    elif choice == "5":
        delete_saved_file()
    elif choice == "6":
        print(f"👋 Goodbye, {user}! Have a great day!")
        break
    else:
        print("❌ Invalid choice. Try again.")



        
        
        
        
        
        
#         quotes = [
#     "Believe you can and you're halfway there.",
#     "Success is not final, failure is not fatal: it is the courage to continue that counts.",
#     "Don't watch the clock; do what it does. Keep going."
# ]
# def show_date_time():
#     now = datetime.datetime.now()
#     print("📅 Current Date and Time:", now.strftime("%Y-%m-%d %H:%M:%S"))
# def show_quote():
#     print("💡 Quote of the Day:")  # Step 1: Print a header
#     print(random.choice(quotes))   # Step 2: Print a random quote
# def take_note():
#     try:
#         note = input("📝 Write your note: ")
#         with open("notes.txt", "a") as file:
#             file.write(note + "\n")
#         print("✅ Note saved successfully!")
#     except Exception as e:
#         print("⚠️ Error saving note:", e)
# def read_notes():
#     try:
#         with open("notes.txt", "r") as file:
#             content = file.read()
#             if content.strip():
#                 print("📓 Your Notes:\n" + content)
#             else:
#                 print("🗒️ No notes yet.")
#     except FileNotFoundError:
#         print("⚠️ No notes file found.")


# public static boolean isPrime(int n) {
#     if (n <= 1) return false;
#     for (int i = 2; i <= Math.sqrt(n); i++) {
#         if (n % i == 0) return false;
#     }
#     return true;
# }
# public static boolean isPrime(int n) {
#     if (n <= 1) return false;
#     for (int i = 2; i <= Math.sqrt(n); i++) {
#         if (n % i == 0) return false;
#     }
#     return true;
# }
# public class HelloWorld {
#     public static void main(String[] args) {
#         System.out.println("Hello, world!");
#     }
# }
# public static int factorial(int n) {
#     return (n <= 1) ? 1 : n * factorial(n - 1);
# }
# public static String reverse(String str) {
#     return new StringBuilder(str).reverse().toString();
# }
# public static boolean isPalindrome(String str) {
#     int i = 0, j = str.length() - 1;
#     while (i < j) {
#         if (str.charAt(i++) != str.charAt(j--)) return false;
#     }
#     return true;
# }
# public static void bubbleSort(int[] arr) {
#     for (int i = 0; i < arr.length - 1; i++) {
#         for (int j = 0; j < arr.length - i - 1; j++) {
#             if (arr[j] > arr[j + 1]) {
#                 int temp = arr[j];
#                 arr[j] = arr[j + 1];
#                 arr[j + 1] = temp;
#             }
#         }
#     }
# }
# public static void printFibonacci(int n) {
#     int a = 0, b = 1;
#     for (int i = 0; i < n; i++) {
#         System.out.print(a + " ");
#         int temp = a + b;
#         a = b;
#         b = temp;
#     }
# }
# import java.util.Scanner;

# Scanner scanner = new Scanner(System.in);
# System.out.print("Enter your name: ");
# String name = scanner.nextLine();
# System.out.println("Hello, " + name);
# public static int largest(int a, int b, int c) {
#     return Math.max(a, Math.max(b, c));
# }
Scanner scanner = new Scanner(System.in);
System.out.print("Enter your name: ");
String name = scanner.nextLine();
System.out.println("Hello, " + name);
public static int largest(int a, int b, int c) {
    return Math.max(a, Math.max(b, c));
}


Scanner scanner = new Scanner(System.in);
System.out.print("Enter your name: ");
String name = scanner.nextLine();
System.out.println("Hello, " + name);
public static int largest(int a, int b, int c) {
    return Math.max(a, Math.max(b, c));
}




def show_date_time():
    now = datetime.datetime.now()
    print("📅 Current Date and Time:", now.strftime("%Y-%m-%d %H:%M:%S"))
def show_quote():
    print("💡 Quote of the Day:")  # Step 1: Print a header
    print(random.choice(quotes))   # Step 2: Print a random quote
def take_note():
    try:
        
        
public static int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}
public static int reverseInt(int num) {
    int rev = 0;
    while (num != 0) {
        rev = rev * 10 + num % 10;
        num /= 10;
    }
    return rev;
}
class Person {
    String name;
    int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void greet() {
        System.out.println("Hi, I'm " + name + ", age " + age);
    }
}
public static boolean isSorted(int[] arr) {
    for (int i = 0; i < arr.length - 1; i++) {
        if (arr[i] > arr[i + 1]) return false;
    }
    return true;
}public static Map<Character, Integer> countChars(String str) {
    Map<Character, Integer> map = new HashMap<>();
    for (char c : str.toCharArray()) {
        map.put(c, map.getOrDefault(c, 0) + 1);
    }
    return map;
}public static void bubbleSort(int[] arr) {
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
public static int linearSearch(int[] arr, int target) {
    for (int i = 0; i < arr.length; i++) {
        if (arr[i] == target) return i;
    }
    return -1;
}
public static void calculator(char operator, double a, double b) {
    switch (operator) {
        case '+': System.out.println(a + b); break;
        case '-': System.out.println(a - b); break;
        case '*': System.out.println(a * b); break;
        case '/': System.out.println(b != 0 ? a / b : "Divide by zero!"); break;
        default: System.out.println("Invalid operator");
    }
}


