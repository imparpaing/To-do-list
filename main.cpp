#include <iostream>
#include <string>

std::string get_user_name(std::string user_name) {
    std::string name;
    std::cin >> name;
    return name;
}

int main() {
    int store_user_selection;

    // Get name
    std::cout << "Hello!\nPlease enter you name: ";
    std::string store_user_name = get_user_name(store_user_name);

    // Welcome screen
    std::cout << "Welcome, " << store_user_name << std::endl;
    std::cout << "What would you like to do?\n\n";

    // Menu
    std::cout << "[ 1] Write to file\n";
    std::cout << "[ 2] Exit program\n";
    std::cout << "\n";

    // User input
    std::cout << "Select: ";
    std::cin >> store_user_selection;
    std::cout << "\n";

    switch(store_user_selection) {
        // Open and write to file
        case 1:
            std::cout << "Opening file...\n\n";
            break;
        
        // Exit program without editing
        case 2:
            std::cout << "Exiting...\n\n";
            break;
        
        // Exit on no user input
        default:
            std::cout << "\n\n";
            break;
    }
    return 0;
}