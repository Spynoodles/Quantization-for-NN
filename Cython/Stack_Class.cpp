#include <vector>


template<typename T>
class Stack {
private:
    int len;
    std::vector<T> Array;

public:
    Stack() : len(0) {}

    void push(const T& element) {
        Array.push_back(element);
        len++;
    }

    int getterlen() const {
        return len;
    }

    const std::vector<T>& getterArray() const {
        return Array;
    }

    T pop() {
        if (len == 0) {
            throw std::out_of_range("Cannot pop from an empty stack");
        }
        T popped_element = Array.back();
        Array.pop_back();
        len--;
        return popped_element;
    }

};