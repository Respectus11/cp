#include <iostream>
using namespace std;

class Person {
public:
    string name;
    Person* parent;
    Person* firstChild;
    Person* nextSibling;

    Person(string n) {
        name = n;
        parent = NULL;
        firstChild = NULL;
        nextSibling = NULL;
    }
};

class FamilyTree {
private:
    Person* root;

    Person* findPerson(Person* node, string name) {
        if (node == NULL) 
            return NULL;
        if (node->name == name) 
            return node;
        Person* child = node->firstChild;
        while (child != NULL) {
            Person* found = findPerson(child, name);
            if (found != NULL) 
                return found;
            child = child->nextSibling;
        }
        return NULL;
    }

public:
    FamilyTree() { root = NULL; }

    void addMember(string name, string parentName = "") {
        if (root == NULL) {
            root = new Person(name);
            return;
        }
        Person* parent = findPerson(root, parentName);
        if (parent == NULL) {
            cout << "Parent " << parentName << " is not found.\n";
            return;
        }
        Person* newMember = new Person(name);
        newMember->parent = parent;
        if (parent->firstChild == NULL) {
            parent->firstChild = newMember;
        } else {
            Person* sibling = parent->firstChild;
            while (sibling->nextSibling != NULL) {
                sibling = sibling->nextSibling;
            }
            sibling->nextSibling = newMember;
        }
    }

    void displayTree(Person* person, int level = 0) {
        if (person == NULL) return;
        cout << string(level * 4, ' ') << person->name << "\n";
        Person* child = person->firstChild;
        while (child != NULL) {
            displayTree(child, level + 1);
            child = child->nextSibling;
        }
    }

    void showTree() {
        if (root == NULL) cout << "Tree is empty.\n";
        else displayTree(root);
    }

    void search(string name) {
        Person* person = findPerson(root, name);
        if (person == NULL) {
            cout << name << " not found.\n";
            return;
        }
        cout << "Searching for: " << person->name << "\n";
        cout << "Parent: " << (person->parent ? person->parent->name : "None") << "\n";
        cout << "Children: ";
        Person* child = person->firstChild;
        while (child != NULL) {
            cout << child->name << " ";
            child = child->nextSibling;
        }
        cout << "\n";
        cout << "Siblings: ";
        if (person->parent != NULL) {
            Person* sib = person->parent->firstChild;
            while (sib != NULL) {
                if (sib != person) cout << sib->name << " ";
                sib = sib->nextSibling;
            }
        }
        cout << "\n";
    }

    void relationship(string name1, string name2) {
        Person* p1 = findPerson(root, name1);
        Person* p2 = findPerson(root, name2);
        if (!p1 || !p2) {
            cout << "One or both members not found.\n";
            return;
        }
        if (p1->parent && p1->parent == p2->parent) {
            cout << name1 << " and " << name2 << " are Siblings.\n";
            return;
        }
        if (p1->parent == p2) {
            cout << name1 << " is child of " << name2 << ".\n";
            return;
        }
        if (p2->parent == p1) {
            cout << name2 << " is child of " << name1 << ".\n";
            return;
        }
        if (p1->parent && p2->parent &&
            p1->parent->parent && p2->parent->parent &&
            p1->parent->parent == p2->parent->parent &&
            p1->parent != p2->parent) {
            cout << name1 << " and " << name2 << " are Cousins.\n";
            return;
        }
        cout << "No direct relationship found.\n";
    }
};

int main() {
    FamilyTree tree;
    int choice;
    string name, parent, name1, name2;
    do {
        cout << "\n--- Family Tree Menu ---\n";
        cout << "1. Add Member\n";
        cout << "2. Display Tree\n";
        cout << "3. Search Member\n";
        cout << "4. Relationship\n";
        cout << "5. Exit\n";
        cout << "Enter choice: ";
        cin >> choice;
        switch (choice) {
        case 1:
            cout << "Enter member name: ";
            cin >> name;
            cout << "Enter parent name (leave empty if root): ";
            cin.ignore();
            getline(cin, parent);
            tree.addMember(name, parent);
            break;
        case 2:
            tree.showTree();
            break;
        case 3:
            cout << "Enter name to search: ";
            cin >> name;
            tree.search(name);
            break;
        case 4:
            cout << "Enter first name: ";
            cin >> name1;
            cout << "Enter second name: ";
            cin >> name2;
            tree.relationship(name1, name2);
            break;
        case 5:
            cout << "Exiting\n";
            break;
        default:
            cout << "Invalid choice.\n";
        }
    } while (choice != 5);
    return 0;
}
