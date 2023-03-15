#include <stdio.h>
#include <string>
#include <unordered_map>

bool enoughCharactersWithHT(std::string s, std::string t) {
    if (s.length() != t.length()) return false;
    int n = s.length();
    std::unordered_map<char, int> counts;
    for (int i = 0; i < n; i++) {
        counts[s[i]]++;
        counts[t[i]]--;
    }
    for (auto count : counts)
        if (count.second) return false;
    return true;
}

int main(void){
    printf("My string program!\n");
    bool result = enoughCharactersWithHT("racecar", "ccaarre");
    printf("Result: %s\n", result ? "SUCCESS": "Try again :)");
    return 0;
}

// bool enoughCharactersWithoutHT(std::string s, std::string t) {
//     if (s.length() != t.length()) return false;
//     int n = s.length();
//     int counts[26] = {0};
//     for (int i = 0; i < n; i++) {
//         counts[s[i] - 'a']++;
//         counts[t[i] - 'a']--;
//     }
//     for (int i = 0; i < 26; i++)
//         if (counts[i]) return false;
//     return true;
// }