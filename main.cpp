#include <iostream>
#include <string>
#include <filesystem>
#include <fstream>

void make_directory() {
    std::string dir_name("Program files");

    std::filesystem::create_directory(dir_name) ?
    std::cout << "Created directory: " << dir_name << std::endl :
    std::cout << "Directory already exists" << std::endl;
}

void make_user_name() {
    std::ofstream MyFile("Program files\\user_name.txt");
    MyFile.close();
}

void check_file_existance() {
    // Files to look for
    int check_directory = std::filesystem::exists("Program files");
    int check_user_name = std::filesystem::exists("Program files\\user_name.txt");

    // Ugly - needs later rewrite
    if(check_directory) {
        std::cout << "Directory already exists\n";
        if(!check_user_name) {
            make_user_name();
        } else {
            std::cout << "File already exists\n";
        }
    } else if(!check_directory) {
        make_directory();
        if(!check_user_name) {
            make_user_name();
        } else {
            std::cout << "File already exists\n";
        }
    }
}

std::string get_user_name(std::string user_name) {
    std::string name;
    std::cin >> name;

    // Check if Program files folder and user_name file exist on sytsem
    // If not create them
    check_file_existance();
    return name;
}

int main() {
    int store_user_selection;

    // Store user name
    std::cout << "Hello!\nPlease enter you name: ";
    std::string store_user_name = get_user_name(store_user_name);
    std::cout << "\n";

    // Welcome screen
    std::cout << "Welcome, " << store_user_name << std::endl;
    std::cout << "What would you like to do?\n\n";

    // Menu
    std::cout << "[ 1] Write to file\n";
    std::cout << "[ 2] Exit program\n";
    std::cout << "\n";

    do {
        // Store user input
        std::cout << "Select: ";
        std::cin >> store_user_selection;

        switch(store_user_selection) {
            // Open and write to file
            case 1:
                std::cout << "Opening file...\n\n";
                break;
            
            // Exit program without editing
            case 2:
                std::cout << "Exiting...\n\n";
                break;
            
            // Prompt for correct option
            default:
                std::cout << "Select correct option\n";
                break;
        }
        } while(store_user_selection != 1 && store_user_selection != 2);
    return 0;
}